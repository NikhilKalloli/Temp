from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import logging
import os
from dotenv import load_dotenv
from together import Together

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

class KeywordRequest(BaseModel):
    keyword: str

# Load API key from environment variable
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
if not TOGETHER_API_KEY:
    raise RuntimeError("TOGETHER_API_KEY environment variable not set")

# Initialize Together client
client = Together(api_key=TOGETHER_API_KEY)

@app.get("/", response_class=HTMLResponse)
async def generate_form(request: Request):
    return templates.TemplateResponse("generate.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, keyword: str = Form(...)):
    # Create prompt for poem generation
    prompt = f"Create a poem using the word: {keyword}"

    try:
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": "You are a creative poet."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.7,
            top_p=0.7,
            top_k=50,
            repetition_penalty=1,
            stop=["<|eot_id|>"],
            stream=False  # Set to False to get the full response at once
        )
        generated_poem = response.choices[0].message.content
        return templates.TemplateResponse("generate.html", {"request": request, "poem": generated_poem, "keyword": keyword})
    except Exception as e:
        logging.error(f"Together API request failed: {e}")
        raise HTTPException(status_code=500, detail="Together API request failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
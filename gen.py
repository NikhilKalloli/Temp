from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
print(f"Generated key: {key.decode()}")
# jbYz8xn-EsAoIHCvnKRXfX1pvzmAuL_3C6j8wz1nR2g=

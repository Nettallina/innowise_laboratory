import uvicorn
import os 
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=True
    )
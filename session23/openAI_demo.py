from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("SECRET_KEY")
name = os.getenv("Name")


CLASS = os.getenv("CLASS")

print(CLASS)
client = OpenAI(api_key="sk")


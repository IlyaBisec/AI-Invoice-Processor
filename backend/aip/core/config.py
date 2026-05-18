# Configuration layer.
# Handles:
# - environment variables
# - application settings
# 18.05.2026 (c) ilya_bisec

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
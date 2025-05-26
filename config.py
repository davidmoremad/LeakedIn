import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_KEY = os.getenv("PHANTOMBUSTER_API_KEY")
ORG_ID = os.getenv("PHANTOMBUSTER_ORG_ID")
API_BASE_URL = "https://api.phantombuster.com/api/v2/"

# Script Configuration
DEFAULT_TIMEOUT = 300  # seconds
MAX_RETRIES = 3
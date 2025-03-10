import os

BASE_DIR = os.environ.get("APP_BASE_DIR", "")

# File paths
DATABASE_FILE = os.path.join(BASE_DIR, "data", "reference", "hcc_relevant_codes.db")
HCC_FILE = os.path.join(BASE_DIR, "data", "reference", "hcc_relevant_codes.csv")

# Data paths
INPUT_PATH = os.path.join(BASE_DIR, "data", "input")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output")

import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

# Load .env jika ada
if os.path.exists(".env"):
    load_dotenv()

CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
API_KEY = os.getenv("CLOUDINARY_API_KEY")
API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

if not CLOUD_NAME or not API_KEY or not API_SECRET:
    raise ValueError("CLOUDINARY credentials tidak ditemukan di environment!")

# Konfigurasi Cloudinary
cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET
)

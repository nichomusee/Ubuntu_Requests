import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    url = input("Enter the image URL: ").strip()
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename or "." not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        filepath = os.path.join(save_dir, filename)

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully saved at: {filepath}")

    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    fetch_image()


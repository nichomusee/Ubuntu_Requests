<!-- # Ubuntu_Requests

A Python script that fetches and saves images from the web, built around **Ubuntu principles**:
- **Community**: Connects to the wider web community by fetching online resources.
- **Respect**: Handles errors gracefully without crashing.
- **Sharing**: Stores all fetched images in an organized folder for later use.
- **Practicality**: Provides a real, useful tool for downloading and managing images.

---

## 📌 Features
- Prompts user for an image URL.
- Downloads the image using the `requests` library.
- Creates a directory called **Fetched_Images** if it doesn’t exist.
- Extracts filename from URL or generates one using `uuid`.
- Saves image in binary mode (`wb`).
- Handles common errors:
  - HTTP errors (404, 500, etc.)
  - Connection errors
  - Timeouts
  - Other request exceptions

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/Ubuntu_Requests.git
   cd Ubuntu_Requests -->

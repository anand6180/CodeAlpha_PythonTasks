import requests
import re

def scrape_title(url):
    response = requests.get(url)
    html = response.text
    title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
    if title_match:
        title = title_match.group(1)
        with open("title.txt", "w") as file:
            file.write(title)
        print(f"✅ Title saved: {title}")
    else:
        print("❌ Title not found.")

scrape_title("https://www.example.com")

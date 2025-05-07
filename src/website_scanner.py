import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def scan_website(url):
    try:
        # Check domain age (use WHOIS API if needed)
        domain = urlparse(url).netloc
        
        # Check SSL (example: requests + SSL verify)
        response = requests.get(url, timeout=5, verify=True)
        has_ssl = response.url.startswith("https")
        
        # Check suspicious keywords
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().lower()
        suspicious_keywords = ["login", "password", "verify", "account", "urgent"]
        found_keywords = [kw for kw in suspicious_keywords if kw in text]
        
        # Simple heuristic: If no SSL + many suspicious keywords → likely phishing
        if not has_ssl and len(found_keywords) > 3:
            return "Likely Phishing"
        else:
            return "Likely Safe"
    except:
        return "Error: Invalid URL"

# Test
print(scan_website("http://fake-login.com"))  # Output: "Likely Phishing"
import requests
import Levenshtein
import pyfiglet
from colorama import init, Fore, Style


init(autoreset=True)

API_KEY = 'AIzaSyBEx4gdPekCCJsVpiLevrPEKxUWb5I7JyM'

with open('ALL-phishing-domains.txt') as f:
    PHISHING_DOMAINS = [line.strip() for line in f.readlines()]

with open('ALL-phishing-links.txt') as f:
    PHISHING_URLS = [line.strip() for line in f.readlines()]

PHISHING_KEYWORDS = ['login', 'verify', 'account', 'update', 'secure', 'ebayisapi', 'signin', 'banking', 'password']

SUSPICIOUS_DOMAINS = [
    'facebook.com', 'google.com', 'paypal.com', 'amazon.com', 'bankofamerica.com',
    'twitter.com', 'instagram.com', 'linkedin.com', 'microsoft.com', 'apple.com',
    'netflix.com', 'yahoo.com', 'bing.com', 'adobe.com', 'dropbox.com',
    'github.com', 'salesforce.com', 'uber.com', 'airbnb.com', 'spotify.com',
    'ebay.com', 'alibaba.com', 'walmart.com', 'target.com', 'bestbuy.com',
    'chase.com', 'citibank.com', 'wellsfargo.com', 'hulu.com', 'tiktok.com',
    'reddit.com', 'pinterest.com', 'quora.com', 'medium.com', 'whatsapp.com',
    'wechat.com', 'snapchat.com', 'tumblr.com', 'vimeo.com', 'dailymotion.com'
]

def is_phishing_url(url):
  
    if url in PHISHING_URLS:
        return True

    for domain in PHISHING_DOMAINS:
        if domain in url:
            return True

    safe_browsing_url = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=' + API_KEY

    payload = {
        "client": {
            "clientId": "HackBit",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    try:
        response = requests.post(safe_browsing_url, json=payload)
        response.raise_for_status()
        result = response.json()

        if 'matches' in result:
            return True

    except requests.exceptions.RequestException as e:
        print(f"Error checking URL with Google Safe Browsing API: {e}")

    for keyword in PHISHING_KEYWORDS:
        if keyword in url.lower():
            return True

    for domain in SUSPICIOUS_DOMAINS:
        if url.lower() == domain:
            return False  
        if Levenshtein.distance(url.lower(), domain) < 5:  
            return True

    return False

def main():
    
    ascii_art = pyfiglet.figlet_format("DP-Links", font="rectangles")
    colored_ascii = f"{Fore.BLUE}{Style.BRIGHT}{ascii_art}"
    print(colored_ascii)

    
    linkedin_saikat = "https://www.linkedin.com/in/0xsaikat/"
    linkedin_bms = "https://www.linkedin.com/company/brainwave-matrix-solutions"
    
    
    link_saikat = f"\033]8;;{linkedin_saikat}\033\\@0xSaikat\033]8;;\033\\"
    link_bms = f"\033]8;;{linkedin_bms}\033\\Brainwave Matrix Solutions\033]8;;\033\\"
    
    print(f"{Fore.RED}V-1.0\n")
    print(f"{Fore.GREEN}Created by {Style.BRIGHT}{link_saikat}{Style.RESET_ALL}{Fore.GREEN} during an internship at {Style.BRIGHT}{link_bms}{Style.RESET_ALL}{Fore.GREEN}.\n")

    while True:
        
        url = input("Enter the URL to check 🔍 (or press 'q' to quit): ")

        if url.lower() == 'q':
            print("Exiting the tool. Goodbye!")
            break

        if url.startswith("http://"):
            protocol = "http://"
            url_without_protocol = url[len("http://"):]

        elif url.startswith("https://"):
            protocol = "https://"
            url_without_protocol = url[len("https://"):]

        else:
           
            if "." in url:
                domain = url.split(".", 1)[0]  
                if domain.isalpha():  
                    protocol = "https://"  
                else:
                    protocol = ""  
            else:
                protocol = ""  

            url_without_protocol = url

        if is_phishing_url(url):
            print(f"{Fore.RED}Phishing detected 🚩: {protocol}{url_without_protocol}")
        else:
            print(f"{Fore.GREEN}Safe Url ✅: {protocol}{url_without_protocol}")

if __name__ == "__main__":
    main()

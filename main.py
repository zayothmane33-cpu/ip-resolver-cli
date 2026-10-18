import socket
from urllib.parse import urlparse

def get_clean_domain(user_input: str) -> str:
    user_input = user_input.strip()
    if not user_input.startswith(('http://', 'https://')):
        user_input = 'http://' + user_input
    return urlparse(user_input).netloc

def resolve_ip():
    print("=" * 45)
    print("  Domain to IP Resolver | Security Tool")
    print("=" * 45)
    
    raw_input = input("\nEnter the Website (e.g., google.com or https://example.com): ")
    domain = get_clean_domain(raw_input)
    
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"\n[+] Target Domain : {domain}")
        print(f"[+] IP Address    : {ip_address}\n")
    except socket.gaierror:
        print(f"\n[-] Error: Could not resolve IP for '{domain}'. Check domain or network connection.\n")
    except Exception as e:
        print(f"\n[-] Unexpected Error: {e}\n")

if __name__ == "__main__":
    resolve_ip()
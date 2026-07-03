import argparse
import time
from urllib.parse import urljoin, urlparse
import requests

# Default paths list
DEFAULT_PATHS = [
    "/admin", "/login", "/config", "/uploads", "/backup", 
    "/.env", "/robots.txt", "/sitemap.xml", "/phpinfo.php", "/dashboard"
]

def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ("http", "https") and parsed.netloc

def load_paths_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {file_path}")
        return None

def scan_url(target_url, paths, timeout=5, delay=0.3, output_file="found_results.txt"):
    if not is_valid_url(target_url):
        print("[!] Invalid URL. Use http:// or https://")
        return

    headers = {"User-Agent": "Educational-Vulnerability-Scanner/1.0"}
    print(f"\n--- Scanning started for: {target_url} ---")
    print(f"--- Results will be saved to: {output_file} ---\n")

    for path in paths:
        full_url = urljoin(target_url.rstrip("/") + "/", path.lstrip("/"))
        try:
            response = requests.get(full_url, headers=headers, timeout=timeout, allow_redirects=False)
            status = response.status_code

            if status == 200:
                print(f"[+] Found: {full_url} | Status: {status}")
                with open(output_file, "a") as f:
                    f.write(full_url + "\n")
            elif status == 403:
                print(f"[!] Forbidden: {full_url} | Status: {status}")
            elif status == 401:
                print(f"[!] Auth Required: {full_url} | Status: {status}")
            elif status in (301, 302, 307, 308):
                location = response.headers.get("Location", "Unknown")
                print(f"[>] Redirect: {full_url} -> {location} | Status: {status}")

        except requests.exceptions.Timeout:
            print(f"[-] Timeout: {full_url}")
        except requests.exceptions.ConnectionError:
            print(f"[-] Connection error: {full_url}")
        except Exception as e:
            print(f"[-] Error scanning {full_url}: {e}")

        time.sleep(delay)

    print("\n--- Scan completed ---")

def main():
    parser = argparse.ArgumentParser(description="Web App Directory Scanner")
    parser.add_argument("url", help="Target URL (e.g., https://example.com)")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="Timeout in seconds")
    parser.add_argument("-d", "--delay", type=float, default=0.3, help="Delay between requests")
    parser.add_argument("-o", "--output", default="found_results.txt", help="Output file to save results")

    args = parser.parse_args()

    paths = load_paths_from_file(args.wordlist) if args.wordlist else DEFAULT_PATHS

    if paths is not None:
        scan_url(args.url, paths, args.timeout, args.delay, args.output)

if __name__ == "__main__":
    main()

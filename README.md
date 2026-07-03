# WebScan-Automator

WebScan-Automator is a simple, automated Python-based directory scanner designed for security enthusiasts and ethical hackers. It identifies hidden directories and sensitive files on a target web application by brute-forcing common paths.

## Features
- **Custom Wordlist Support:** Easily use your own wordlists via the `-w` flag.
- **Detailed Status Reporting:** Filters results based on HTTP status codes (200, 403, 401, 30x).
- **Automated Logging:** Automatically saves all successful discoveries (Status 200) to a text file for later analysis.
- **Customizable:** Adjust scan speed with delay and timeout settings.

## Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/WebScan-Automator.git](https://github.com/yourusername/WebScan-Automator.git)
   cd WebScan-Automator

## Installation
Ensure you have the `requests` library installed:
```bash
pip install requests

Usage
Run the script using the following command structure:

Bash
python3 scanner.py <target-url> [options]
Examples
Basic Scan:
Bash
python3 scanner.py [https://example.com](https://example.com)
Scan with a custom wordlist:
Bash
python3 scanner.py [https://example.com](https://example.com) -w paths.txt
Advanced Scan (with delay and timeout):
Bash
python3 scanner.py [https://example.com](https://example.com) -t 10 -d 0.5 -o results.txt
Options
-w, --wordlist: Path to your wordlist file.

-t, --timeout: Request timeout in seconds (default: 5).

-d, --delay: Delay between requests in seconds (default: 0.3).

-o, --output: File to save the discovered paths (default: found_results.txt).

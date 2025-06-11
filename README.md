# 🛡️ Python-Based Vulnerability Scanner

This is a basic vulnerability scanner written in Python that detects SQL Injection and Directory Traversal vulnerabilities. It also includes OWASP ZAP integration.

## How to Run

```bash
python scanner.py http://example.com/page.php
```

## OWASP ZAP Integration

Start ZAP:
```bash
zap.sh -daemon -port 8090 -config api.key=12345
```
Run:
```bash
python zap_scanner.py
```

Report saved to `reports/zap_report.html`

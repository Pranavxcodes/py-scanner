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

- ✅ Detects:
  - SQL Injection (`' OR '1'='1`)
  - Directory Traversal (`../../../etc/passwd`)
- 🔌 OWASP ZAP API Integration
- 📄 Generates HTML vulnerability reports
- 🧪 Tested on [OWASP Juice Shop](https://github.com/juice-shop/juice-shop)

---

## 🧪 Test Environment (OWASP Juice Shop)

To simulate real-world vulnerabilities, you can run [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) locally:

### 🔧 Step 1: Start Juice Shop using Docker

```bash
docker pull bkimminich/juice-shop
docker run --rm -d -p 3000:3000 bkimminich/juice-shop


Report saved to `reports/zap_report.html`

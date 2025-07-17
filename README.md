# 🛡️ Email IOC Extractor

This Python script extracts key Indicators of Compromise (IOCs) such as IP addresses, URLs, malware file references, and email addresses from raw email content.

## 📌 Features

- ✅ Extracts IP addresses
- ✅ Extracts URLs (including suspicious C2 domains)
- ✅ Detects malware-related file extensions in URLs (`.exe`, `.bat`, `.vbs`, `.js`, `.zip`, `.rar`)
- ✅ Extracts all email addresses found in the content

## 📂 How It Works

1. Reads a raw email file (`sample_email.txt`)
2. Uses regular expressions to extract:
   - IP addresses
   - URLs
   - Potential malware file links
   - Email addresses

## 🔧 Requirements

- Python 3.x (Tested on Python 3.12)
- No external libraries required (uses built-in `re` module)

## 🚀 Usage

1. Clone or download this repository
2. Add your email content to `sample_email.txt`
3. Run the script:

## 🧪 Future Enhancements (Planned)
1. Integrate with VirusTotal API to validate IOCs

2. Analyze email headers for spoofing or relay analysis

3. Detect email protection mechanisms like SPF/DKIM/DMARC

4. Integrate with SIEM tools like Splunk or Wazuh

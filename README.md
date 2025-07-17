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

## Sample_email Image 1
<img width="1559" height="935" alt="Screenshot 2025-07-17 090319" src="https://github.com/user-attachments/assets/aaa664b6-e813-4f8f-a34b-2ad7bb365de6" />

## Python_code Image 2
<img width="1566" height="747" alt="Screenshot 2025-07-17 090342" src="https://github.com/user-attachments/assets/aec8dd69-e23f-4d29-a303-d0f4eef1f565" />

## Output Image 3
<img width="1545" height="363" alt="Screenshot 2025-07-17 090417" src="https://github.com/user-attachments/assets/ffba500c-6d50-4389-a63e-497da06b93c9" />


## 🧪 Future Enhancements (Planned)
1. Integrate with VirusTotal API to validate IOCs

2. Analyze email headers for spoofing or relay analysis

3. Detect email protection mechanisms like SPF/DKIM/DMARC

4. Integrate with SIEM tools like Splunk or Wazuh

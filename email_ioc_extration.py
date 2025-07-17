import re
try:
    with open("sample_email.txt", "r") as file:
     email = file.read()
     malware_file=[".exe",".bat","vbs",".js","zip","rar"]
    mfiles=[]
    ip_address = re.findall(r"\d{0,255}\.\d{0,255}\.\d{0,255}\.\d{0,255}",email)
    urls=re.findall(r"http[s]?://\S+",email)
    for u in urls:
        for m in malware_file:
            if m in u :
               mfiles.append(u)
    email_add=re.findall(r"\S+@\S+",email)

     
    print("EXTRACTING IOC's")
    print(f" The Suspicious ips are \n {set(ip_address)}\n")
    print(f"The Suspicious C2 Domains are\n {set(urls)}\n")
    print(f"Malwares \n{set(mfiles)}\n")
    print(f"Email \n{set(email_add) }\n")

except FileNotFoundError:
    print("sample_email.txt not found. Please check the file path.")



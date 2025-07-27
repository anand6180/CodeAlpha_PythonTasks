import re

def extract_emails(file_path, output_path):
    with open(file_path, "r") as file:
        content = file.read()

    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content)

    with open(output_path, "w") as output:
        for email in emails:
            output.write(email + "\n")

    print(f"✅ Extracted {len(emails)} emails to {output_path}")

extract_emails("input.txt", "emails.txt")

"""
VERSION 1

"""
import csv
import urllib.parse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_whatsapp_message(driver, wait, phone_number, message):
    encoded_msg = urllib.parse.quote(message)
    url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_msg}"
    driver.get(url)

    try:
        send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]')))
        send_button.click()
        return True
    except Exception as e:
        print(f"❌ Error sending to {phone_number}: {e}")
        return False

def bulk_send_from_csv(csv_path, message_template):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=./User_Data")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 300)

    driver.get("https://web.whatsapp.com")
    wait.until(EC.presence_of_element_located((By.ID, "side")))

    with open(csv_path, newline='', encoding='utf-8-sig') as f, open('whatsapp_log.csv', 'w', newline='') as logf:
        reader = csv.DictReader(f)
        logwriter = csv.writer(logf)
        logwriter.writerow(['Name', 'Phone', 'Status'])

        for row in reader:
            name = row['Complete Name'].strip()
            phone_number = row['Phone'].strip().replace(" ", "")
            personalized_message = message_template.replace("[Artisan's Name]", name)

            for attempt in range(2):
                success = send_whatsapp_message(driver, wait, phone_number, personalized_message)
                if success:
                    print(f"✅ Message sent to {name} ({phone_number})")
                    logwriter.writerow([name, phone_number, "Sent"])
                    break
                elif attempt == 1:
                    print(f"❌ Failed to send after retries to {name} ({phone_number})")
                    logwriter.writerow([name, phone_number, "Failed"])

            time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    artisan_message = """Hello [Artisan's Name], 👋

We hope you're doing well!
Have you created your catalog on Artisans Circle yet?

📌 Why it matters:
Your catalog is your digital portfolio—it showcases your skills, past projects, and what you offer. It’s what clients see first before hiring you!

✅ What you gain:

More visibility to serious clients

Reordering of what you've done before by clients

Increased trust and professionalism

Better chances of winning job bids

A personalized page to share with anyone

Don't miss out on opportunities—let your work speak for you.

📷 Upload photos, list your services, and stand out from the crowd.
Let’s build your brand together on Artisans Bridge.

Need help getting started? We’re here to support you!

https://youtube.com/shorts/UbXpeqAfLkE?feature=share

— Team Artisans Bridge
https://artisansbridge.com
"""

    bulk_send_from_csv("contacts.csv", artisan_message)

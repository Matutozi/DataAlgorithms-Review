import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_contact(driver, wait, phone_number):
    try:
        # Click the search box
        search_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
        search_box.clear()
        search_box.click()
        time.sleep(1)
        search_box.send_keys(phone_number)
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)

        # Wait for chat to open
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//header[contains(@class, "_amie")]')))
        return True
    except Exception as e:
        print(f"❌ Could not find or open chat for {phone_number}: {e}")
        return False

def send_message(driver, wait, message):
    try:
        msg_box = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@data-tab and @spellcheck="true"]')))
        msg_box.click()
        msg_box.send_keys(message)
        msg_box.send_keys(Keys.ENTER)
        return True
    except Exception as e:
        print(f"❌ Could not send message: {e}")
        return False

def bulk_send_from_csv(csv_path, message_template):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=./User_Data")  # persist session
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 60)

    print("⏳ Please scan the QR code in the opened browser window...")
    driver.get("https://web.whatsapp.com")
    wait.until(EC.presence_of_element_located((By.ID, "side")))
    print("✅ Logged in to WhatsApp Web.")

    with open(csv_path, newline='', encoding='utf-8-sig') as f, open('whatsapp_log.csv', 'w', newline='') as logf:
        reader = csv.DictReader(f)
        logwriter = csv.writer(logf)
        logwriter.writerow(['Name', 'Phone', 'Status'])

        for row in reader:
            name = row['Complete Name'].strip()
            phone_number = row['Phone'].strip().replace(" ", "")
            personalized_message = message_template.replace("[Artisan's Name]", name)

            for attempt in range(2):
                if search_contact(driver, wait, phone_number):
                    if send_message(driver, wait, personalized_message):
                        print(f"✅ Message sent to {name} ({phone_number})")
                        logwriter.writerow([name, phone_number, "Sent"])
                        break
                    else:
                        print(f"❌ Failed to send message to {name} ({phone_number})")
                else:
                    print(f"❌ Failed to find/open chat with {name} ({phone_number})")

                if attempt == 1:
                    logwriter.writerow([name, phone_number, "Failed"])
            time.sleep(4)

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
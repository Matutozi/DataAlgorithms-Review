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
            personalized_message = message_template.replace("[President's Name]", name)

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
    ambassador_message = """Hi [President's Name], Good afternoon
I’m Sobowale Emmanuel a student of  University of Lagos, 
I am the Co-Lead for IEEEXtreme Nigeria Section.  

I'm reaching out regarding the *nomination of an IEEEXtreme Ambassador* for your Student Branch. Each SB is to select one active IEEE member who is also actively involved in the SB. The person will serve as the *main point of contact* and represent your SB in all IEEEXtreme activities.

Please fill out this short form to nominate a suitable person:  
👉 https://forms.gle/FyZSyJYLDSGAMkMr7  

*Deadline: 14th June 2025*  
you can also reach section lead 
👉 Jelili-Ibrahim Abdul-Azeez 2348089675226

Let me know if you have any questions. Thanks for your support!
"""

    bulk_send_from_csv("ieee.csv", ambassador_message)

import urllib.parse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_whatsapp_message(name: str, phone: str, message: str, attempts=2, delay=5):
    """
    Send WhatsApp message to a single contact
    
    Args:
        name: Recipient's name (for logging)
        phone: Phone number with country code (no spaces/special chars)
        message: Text message to send
        attempts: Number of sending attempts
        delay: Seconds to wait between attempts
    """
    
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=./User_Data")
    options.add_argument("--start-maximized")
    
    try:
        driver = webdriver.Chrome(options=options)
        wait = WebDriverWait(driver, 500)
        
        
        driver.get("https://web.whatsapp.com")
        wait.until(EC.presence_of_element_located((By.ID, "side")))
        
        
        encoded_msg = urllib.parse.quote(message)
        url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_msg}"
        
        
        for attempt in range(attempts):
            try:
                driver.get(url)
                send_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
                )
                time.sleep(2)
                send_button.click()
                print(f"✅ Message sent to {name} ({phone})")
                time.sleep(40)
                return True
            except Exception as e:
                print(f"❌ Attempt {attempt + 1} failed for {name} ({phone}): {e}")
                if attempt < attempts - 1:
                    time.sleep(delay)
        
        print(f"❌ Failed to send to {name} after {attempts} attempts")
        return False
    
    finally:
            driver.quit()

if __name__ == "__main__":
    recipient = "jane Bello Doe"
    send_whatsapp_message(
    name=recipient,
    phone="+2348130778827",
    message= f"""Hello {recipient}👋
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
)
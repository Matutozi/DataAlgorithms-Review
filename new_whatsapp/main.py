from whatsapp_bridge.bot import ApplicationBuilder

PHONE = "+2348130778827"
NAME = "Emmanuel"
USER_TYPE = "artisan"

def get_message(name, user_type):
    if user_type == "client":
        return f"""Hello {name}! 👋

Welcome to Artisans Bridge — we're excited to have you on board! 🎉
From home repairs to tech support, we connect you with verified artisans who'll get the job done.

🛠 Explore our catalog to post tasks or choose pre-defined services!

Cheers,  
The Artisans Bridge Team
"""
    elif user_type == "artisan":
        return f"""Hello {name}👋  
Have you created your catalog yet?

📌 Why it matters:  
It's your portfolio to win more jobs and build trust.  

✅ Benefits:  
• More visibility  
• Personal link to share  
• Better job matching  

Get started today!  
— Artisans Bridge Team  
https://artisansbridge.com  
"""
    return None

def send_message(name, phone, user_type):
    message = get_message(name, user_type)
    if not message:
        print("No message configured for this user type")
        return

    application = None
    try:
        # Initialize the application
        print("Initializing WhatsApp bridge...")
        application = ApplicationBuilder().build()
        
        # Connect (assuming connect() is available)
        print("Connecting to WhatsApp...")
        application.connect()

        # Send message
        print(f"Sending message to {phone}...")
        application.bot.send_message(phone, message)
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        # Attempt to reconnect once if the first try fails
        try:
            print("Attempting to reconnect and send...")
            if application:
                application.disconnect()
            application = ApplicationBuilder().build()
            application.connect()
            application.bot.send_message(phone, message)
            print("Message sent after reconnection!")
        except Exception as e2:
            print(f"Failed after retry: {str(e2)}")
    finally:
        # Clean up
        try:
            if application:
                print("Disconnecting...")
                application.disconnect()
        except Exception as e:
            print(f"Error during disconnection: {str(e)}")

if __name__ == "__main__":
    print("Starting message sending process...")
    send_message(NAME, PHONE, USER_TYPE)
    print("Process completed")
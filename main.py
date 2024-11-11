import smtplib
from email.mime.text import MIMEText
from ollama_llm import get_response  # Assuming this fetches responses from a language model
from whisper_speech_recognition import recognize_speech
from neuphonic_texttospeech import synthesize_speech

# Define trigger words
TRIGGER_WORDS = ["stress", "relapse", "craving", "alone", "tempted"]

# Email Notification Function to Sponsor
def notify_sponsor(message):
    sponsor_email = "sponsor@example.com"  # Replace with actual sponsor email
    subject = "Trigger Alert: Please Check on Your Sponsee"
    body = f"The assistant has detected a potential trigger in the user's message. Message: {message}"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "assistant@example.com"
    msg["To"] = sponsor_email

    # Configure SMTP (example uses Gmail)
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login("your-email@example.com", "your-password")  # Use secure method for credentials
    smtp.sendmail("assistant@example.com", sponsor_email, msg.as_string())
    smtp.quit()

# Detect if a trigger word is present in the message
def detect_trigger(message):
    for word in TRIGGER_WORDS:
        if word in message.lower():
            return True
    return False

# Generate a motivational response
def generate_motivational_response():
    prompt = "Provide a supportive, motivational message to help a recovering addict stay strong in their journey."
    response = get_response(prompt)
    return response

# Main Function to Engage in Conversation
def engage_conversation():
    print("Starting conversation...")

    # Recognize speech (convert voice input to text)
    user_message = recognize_speech()
    print(f"User said: {user_message}")

    # Check for triggers and notify the sponsor if any are found
    if detect_trigger(user_message):
        print("Trigger detected, notifying sponsor...")
        notify_sponsor(user_message)
    
    # Generate a motivational response for the user
    response_message = generate_motivational_response()
    print(f"Assistant: {response_message}")

    # Convert the response text to speech
    synthesize_speech(response_message)

# Run the assistant in a loop (or call engage_conversation once if only single interaction needed)
if __name__ == "__main__":
    engage_conversation()

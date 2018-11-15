# BruteForce_SSH

Two python scripts for bruteforcing SSH login: bf_multithreading_script_python2.py and bf_server_tmux.py.

## bf_multithreading_script_python2.py
This script's 'great purpose' is to bruteforce the password for an ssh connection that does not require a key. This script was designed to be executed from our own computers (since it allowed for more resources like RAM and CPU). We could therefore split the wordlist into as many smaller wordlists as we pleased and use threads to connect to ssh and check the output with password from its own wordlist as parameter. The only obstacle is that we could not execute more threads than the webserver allowed requests from one client.

## bf_server_tmux.py
This script was designed to use less RAM than the previous script in case it needs to be executed from a computer with a little amount of RAM.

# Disclaimer
This script is only for educational and ethical purposes, usage in other areas are not endorsed by BadNameException.

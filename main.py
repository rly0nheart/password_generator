# Author info:
# Github | rlyonheart
# Twitter| rly0nheart
# Instagram | rlyonheart

#import color module
import termcolor
from termcolor import colored,cprint

# import the random module
import random

# import the time module(not that important)
import time

# import sys module(using this to terminate the program)
import sys

cprint("\t\t --P4SSW0RD G3N3RAT0R-- \n\n",'red',attrs=['bold','underline'])

cprint("Generate password:\n",'white',attrs=['bold','underline'])

if __name__ == '__main__':
     ui=input().lower()
     chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYS1234567890"
     len = 10
     
     x = ''.join(random.sample(chars, len))
     if "passgen" in ui:
       time.sleep(1)
       cprint("\nPlease Wait",'blue',attrs=['bold'])
       time.sleep(1)
       cprint(".",'cyan',attrs=['bold'])
       time.sleep(1)
       cprint(".",'red',attrs=['bold'])
       time.sleep(1)
       cprint(".",'green',attrs=['bold'])
       time.sleep(1)
       cprint(".",'blue',attrs=['bold'])
       time.sleep(1)
       cprint(".",'yellow',attrs=['bold'])
       time.sleep(1)
       cprint("Password generated!..",'yellow',attrs=['bold'])
       time.sleep(2)
       cprint("\nyour new password is: ",'red',attrs=['bold'])
       time.sleep(0.7)
       print("\t\t\t",x)
       time.sleep(1)
       cprint('''\n\n\n\nTip: Do not show this password
to anyone, if you are going to use it.\n\n''','green',attrs=['bold'])

     else:
       time.sleep(1)
       cprint("\nProcessing",'blue',attrs=['bold'])
       time.sleep(1)
       cprint(".",'cyan',attrs=['bold'])
       time.sleep(1)
       cprint(".",'yellow',attrs=['bold'])
       time.sleep(1)
       cprint(".",'green',attrs=['bold'])
       time.sleep(1)
       cprint(".",'blue',attrs=['bold'])
       time.sleep(1)
       cprint(".",'red',attrs=['bold'])
       cprint("\nINVALID INPUT!",'red',attrs=['bold'])
       time.sleep(1.5)
       sys.exit(colored("program terminated due to invalid input by user.",'white','on_red',attrs=['bold']))
       
       
# ©2020
# thank you, for using Password generator!

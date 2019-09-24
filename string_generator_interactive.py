#! python3
# -*- coding: utf-8 -*-

import random
import sys
import pyperclip
import string

print("length of random string:")
N = int(float(sys.stdin.readline()))

flag_lowercase = False
txt_case = "_uppercase"
print("Do you use lowercase letters? (y or n)")
answer = sys.stdin.readline().strip()
if answer.lower()[0] == "y":
    flag_lowercase = True
    txt_case = "_lowercase"
#end if

flag_distinct = False
txt_isdistinct = ""

if N <= 26:
    print("Do you make every element distinct? (y or n)")
    answer = sys.stdin.readline().strip()
    if answer.lower()[0] == "y":
        flag_distinct = True
        txt_isdistinct = "_distinct"
    #end if
#end if

if flag_distinct:
    set_el = set()
#end if

path_output = "./"
filename_output = "randstring{}_size{}{}.txt".format(txt_case,N,txt_isdistinct)


str_clip = ""
for _ in range(N):

    if flag_lowercase:
        chgen = random.choice(string.ascii_lowercase)
    else:
        chgen = random.choice(string.ascii_uppercase)
    #end if

    while flag_distinct and (chgen in set_el):
        if flag_lowercase:
            chgen = random.choice(string.ascii_lowercase)
        else:
            chgen = random.choice(string.ascii_uppercase)
        #end if
    #end while
    str_clip += chgen

    if flag_distinct:
        set_el.add(chgen)
    #end if
#end for

str_clip += "\n"
print("Generated:\n")
print(str_clip)
pyperclip.copy(str_clip)
print("Copied to your clipboard!")
print("Do you write the output to a txt file? (y or n)")
answer = sys.stdin.readline().strip()

if answer.lower()[0] == "y":
    with open(path_output+filename_output,mode="w") as file_out:
        file_out.write(str_clip)
    #end with
#end if

print("Done.")

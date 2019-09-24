#! python3
# -*- coding: utf-8 -*-

import random
import sys
import string

Nleft = 2
Nright = 1e4
flag_lowercase = True
flag_distinct = False
flag_output = False


N = random.randint(Nleft,Nright)

if N <= 26:
    flag_distinct = False
#end if

if flag_distinct:
    set_el = set()
#end if

path_output = "./"
filename_output = "input.txt"


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

print(str_clip)

if flag_output:
    with open(path_output+filename_output,mode="w") as file_out:
        file_out.write(str_clip)
    #end with
#end if

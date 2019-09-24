#! python3
# -*- coding: utf-8 -*-

import random
import sys
import pyperclip

print("length of random bit sequence:")
N = int(float(sys.stdin.readline()))

path_output = "./"
filename_output = "randbitseq_size{}.txt".format(N)


str_clip = ""
for _ in range(N):
    str_clip += "{}".format(random.randint(0,1))
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

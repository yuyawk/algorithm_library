#! python3
# -*- coding: utf-8 -*-

import random
import sys
import pyperclip

print("minimum:")
left = int(float(sys.stdin.readline()))
right = left-1
while right < left:
    print("maximum (must be greater than or equal to the minimum value):")
    right = int(float(sys.stdin.readline()))
#end while

N = random.randint(left,right)

path_output = "./"
filename_output = "randoneint_from{}_to{}.txt".format(left,right)

str_clip = "{}\n".format(N)

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

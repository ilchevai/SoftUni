import string
from string import punctuation
o = False
n = False
c = False
word = ""
command = input()
while command != "End":
    if command in punctuation:
        command = input()
        continue
    if (command == "o" and o) or (command == "c" and c) or (command == "n" and n):
        word += command
    if command == "o" or command == "c" or command == "n":
        if command == "o":
            o = True
        if command == "n":
            n = True
        if command == "c":
            c = True
    else:
        word += command
    if o and n and c:
        o = False
        n = False
        c = False
        print(f"{word} ", end="")
        word = ""
    command = input()


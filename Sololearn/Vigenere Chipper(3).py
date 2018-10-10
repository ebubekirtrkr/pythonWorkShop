import sys
#Programmed by Ebubekir Turker
#Please enter values into separate lines
#First line is word
#Second line is maskingMessage
#"Please don't use special character"
word =input("")
key = input("\n")
lenw=len(word)
lenk=len(key)
h= ""
if lenw>lenk:
    wk=lenw-lenk
    for x in range(0,(wk)):
        key = key + key[x]
    for y in range(0,lenw):
        to1_26word=ord(word[y])-97
        to1_26key = ord(key[y])-97
        s= to1_26key+ to1_26word
        ms=s%26
        c= chr(ms+97)
        h= h+c
if lenw==lenk:
    for y in range(0,lenw):
        to1_26word=ord(word[y])-97
        to1_26key = ord(key[y])-97
        s= to1_26key+ to1_26word
        ms=s%26
        c= chr(ms+97)
        h= h+c
if lenw<lenk:
    kw=lenk-lenw
    for x in range(1,(kw+1)):
        key=key[:(lenk-x)]
    for y in range(0,lenw):
        to1_26word=ord(word[y])-97
        to1_26key = ord(key[y])-97
        s= to1_26key+ to1_26word
        ms=s%26
        c= chr(ms+97)
        h= h+c
print ("Original Message:{}\n".format(word))
print ("Masking Key     :{}\n".format(key))
print ("Decyrpted Text  :{}".format(h))
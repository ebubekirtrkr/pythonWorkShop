import sys
word = raw_input("please enter word\n")
key = raw_input("please enter key\n")
lenw=len(word)
lenk=len(key)
if lenw<lenk:
	kw=lenk-lenw
	for x in range(1,(kw+1)):
		key=key[:(lenk-x)]
		print key
# find email adresses in a text and count 
# how many of them were sent, with regex

# importing registry
import re
# variable to open the file
fname = open('mbox-short.txt')

# make a dictionary, also possible using {}
kamus = dict()

# build loop to find the lines in the opened file
for lines in fname :
	# variable line to stripping all lines
	lines = lines.strip()
	# using method re.findall in variable email 
	# to find email in the lines start with 'From'
	# and after that a words with '@' without withspace
	# before and after, to find email adress
	# in variable called 'lines'
	email = re.findall('^From (\S+@\S+)', lines)
	# if the variable email length is less than 1
	# which means zero then skip it and continue
	if len(email) < 1 : continue
	# loop email address in variable 'email'
	for mail in email :
		# to build dictionary and counting how many
		kamus[mail] = kamus.get(mail, 0) + 1

# How to sort a dict by value, 
# using key=lambda item: item[1]
for kunci, isi in sorted(kamus.items(), key=lambda item: item[1]) :
	print(kunci, isi)

'''
# results
wagnermr@iupui.edu 1
antranig@caret.cam.ac.uk 1
gopal.ramasammycook@gmail.com 1
ray@media.berkeley.edu 1
stephen.marquard@uct.ac.za 2
rjlowe@iupui.edu 2
louis@media.berkeley.edu 3
gsilver@umich.edu 3
zqian@umich.edu 4
david.horwitz@uct.ac.za 4
cwen@iupui.edu 5
# To sort the keys in reverse, add reverse=True 
# as a keyword argument to the sorted function.
'''
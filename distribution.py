"""
distribution.py
Author: Ethan Adner
Credit: David Wilson, Peyton Streanrs, Dennison

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
s=str(input("Please enter a string of text (the bigger the better):"))
ase=s
z=[]
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

s=s.lower()
for x in l:
    z.append(s.count(x))
tup=list(zip(z,l))
tups=sorted(tup)
print(tup)
print(tups)
#print(tups)
tups.reverse()
#print(tups)
tups = sorted(tup, key=lambda zsd:(-zsd[0], zsd[1]))
#print(tups)
x=0
z=[]

print(' The distribution of characters in "'+ase+'" is:')
while x<len(tups):
    print(tups[x][0]*tups[x][1])
    x=x+1
# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
star_wars=raw_input("Enter a string: ")
star_trek=[]
for letter in star_wars:
    star_trek.append(letter)


kirk=float(len(star_wars))
rey=star_trek[0]
spock=0
finn=star_trek[-1]
poe=-1
leia=0
luke=0
print kirk/2.0
while kirk/2.0>spock or kirk/2.0==spock: #this is where the problem is!!!
    rey=star_trek[spock+1]
    spock=spock+1
    finn=star_trek[poe-1]
    poe=poe-1
    if rey==finn:
        leia=leia+1
    if rey!=finn:
        luke=luke+1
if luke!=0:
    print star_wars,"is not a palindrome."
if luke==0:
    print star_wars,"is a palindrome."
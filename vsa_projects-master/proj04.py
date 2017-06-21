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
if kirk%2!=0:
    kirk=int(kirk+1)
if " " or "A" or"B" or"C" or"D" or"E" or"F" or"G" or"H" or"I"or"J"or"K"or"L"or"M"or"N"or"O"or"P"or"Q"or"R"or"S"or"T"or"U"or"V"or"W"or"X"or"Y"or"Z" in star_trek:
    print star_trek
else:
    while kirk/2.0>spock or kirk/2.0==spock:
        rey=star_trek[spock]
        spock=spock+1
        finn=star_trek[poe]
        poe=poe-1
        if rey==finn:
            leia=leia+1
        if rey!=finn:
            luke=luke+1
    if luke!=0:
        print star_wars,"is not a palindrome."
    if luke==0:
        print star_wars,"is a palindrome."
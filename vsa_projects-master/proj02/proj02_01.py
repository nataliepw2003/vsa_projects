# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")
print "the birthday variable = ", birthday


if birthday== "Y" or "y":
    year=2017
    print "already had a birthday, year = ", year
    while year<((2017-age)+101):
        print year
        year=year+1
elif birthday== "n" or "N":
    print "No birthday yet, first year =", year
    year=2016
    print "No birthday yet, second year =", year
    while year<((2016-age)+100):
        print year
        year=year+1
else:
    print "try again"

print name, " will turn 100 in the year ", year-1, "."
print (2016-23)+100
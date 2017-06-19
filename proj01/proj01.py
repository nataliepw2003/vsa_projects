# Name: Natalie Wright
# Date: June 19, 2017

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
#print "Hello world!"

x= raw_input("Name: ")
y= raw_input("Age: ")
z=raw_input("Have you had a birthday this year? (y/n)")

y=int(y)

year= 2017

if z=="yes":
    print x,
    print "will turn 100 in the year",
    print (year-y)+100

else:
    print x,
    print "will turn 100 in the year",
    print (year-y)+
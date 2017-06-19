# Name: Natalie Wright
# Date: June 19, 2017

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
#print "Hello world!"

x= raw_input("Name: ")
y= raw_input("Age: ")
z=raw_input("Have you had a birthday this year? (yes or no) ")

y=int(y)
year= 2017

if z=="yes"or"y":
    if y<100:
        print x[0].upper()+x[1:100].lower() +", you will turn 100 in the year",
        print (year-y)+100
    else:
        print x[0].upper()+x[1:100].lower() +", you turned 100 in the year",
        print (year - y) + 100
else:
    print x,
    if y<100:
        print x[0].upper()+x[1:100].lower() +", you will turn 100 in the year",
        print (year-y)+99
    else:
        print x[0].upper()+x[1:100].lower() +", you turned 100 in the year",
        print (year - y) +99

if (y==13) and (y<18) or (y>13) and (y<18):
    print "You may watch G, PG, and PG13 rated movies."
elif y>18 and y<100 or y==18:
    print "You may watch G, PG, PG13, and R rated movies."
elif y>100:
    print "You may watch whatever you want; you're 100(+) years old!"
elif y==100:
    print "You may watch whatever you want; you're 100 years old!"
else:
    w=raw_input("Do your parents allow you to watch PG movies? (yes or no) ")
    if w=="yes":
        print "You may watch G and PG rated movies."
    else:
        print "You may only watch G rated movies."








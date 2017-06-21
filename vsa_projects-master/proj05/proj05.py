# Name:
# Date:

# proj05: functions and lists

"Part I"
#num=int(raw_input("insert num: "))

def divisors(num):
    list1=[]
    for b in range (1,num+1):
        if num%b==0:
            list1.append(b)
    return list1
#print divisors(num)


def prime(num):
    mylist=divisors(num)
    length=len(mylist)
    if length>2:
        print num, "is NOT PRIME."
        return False
    else:
        print num, "is PRIME."
        return True

#prime(7)

    #"""
    #Takes a number and returns all divisors of the number, ordered least to greatest
   # param num: int
    #return: list (int)
#"""
    #return 0

#def prime(num):
    #"""
    #Takes a number and returns True if the number is prime, otherwise False
    #:param num: int
    #:return: bool
    #"""
   # return False

# Part II
lista = []
listb = []
item=0
def intersection(lista, listb):
    output_list = []
    for item in lista:
        if item in listb:
            if item not in output_list:
                output_list.append(item)
                #print output_list
        #item=item+1
    print output_list
    return output_list



#def intersection(lst1, lst2):
    #return ["test"]


# """
#    Takes two lists and returns a list of the elements in common between the lists
#    :param lst1: list, any type
#     :param lst2: list, any type
#     :return: list, any type
#   """

Part III
side1=int(raw_input("side1: "))
side2=int(raw_input("side2: "))
side3=int(raw_input("side3: "))
def find_ab(side1, side2, side3):
    if side1>side2:
        if side1>side3:
            print side2,"and",side3,"are the smallest sides."
            return side2,side3
        elif side1<side3:
            print side1,"and",side2,"are the smallest sides."
            return side1,side2
        elif side1==side3:
            print side2,"is the smallest side."
            return side2
    elif side1 < side2:
        if side2 > side3:
            print side1, "and", side3, "are the smallest sides."
            return side1,side3
        elif side2 < side3:
            print side1, "and", side2, "are the smallest sides."
            return side1,side2
        elif side2 == side3:
            print side1, "is the smallest side."
            return side1
    elif side1==side2:
        print side3, "is the smallest side."
        return side3
    elif side1==side2 and side1==side3:
        print side1,",",side2,",and",side3,"are all equal."
        return side1,side2,side3
print find_ab(side1, side2, side3)

   # """
   # Takes three side lengths an returns two smallest in a list
    #:param side1: int or float
    #:param side2: int or float
    #:param side3: int or float
    #:return: list of 2 ints or floats
   # """
   # return [0, 0]
# side1=int(raw_input("side1: "))
# side2=int(raw_input("side2: "))
# side3=int(raw_input("side3: "))

#
#
# print find_c(side1, side2, side3)
   # """
   # Takes three side lengths an returns the largest
   # :param side1: int or float
   # :param side2: int or float
   # :param side3: int or float
   # :return: int or float
   # """
   # return 0
side=int(raw_input("side: "))
def square(side):
    area=side**2
    return area
print square(side)
   """
   Takes a side length and returns the side length squared
   :param side: int or float
   :return: int or float
   """
   return 0
sidea=int(raw_input("smallest side: "))
sideb=int(raw_input("middle side: "))
sidec=int(raw_input("largest side: "))
def pythagorean(sidea,sideb,sidec):
    if sidea<sideb and sideb<sidec:
        if (sidea**2)+(sideb**2)==sidec**2:
            print "This triangle is right."
            return True
        elif (sidea**2)+(sideb**2)!=sidec**2:
            print "This triangle is not right."
            return False
    else:
        print "Please restart the program, and put the sides in order from smallest to largest."
        return ":I"
print pythagorean(sidea,sideb,sidec)

  #  """
  #  Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
  #  :param a: int or float
  # :param b: int or float
    #:param c: int or float
  # :return: bool
 #   """
   # return False

#def is_right(side1, side2, side3):
sidea=int(raw_input("smallest side: "))
sideb=int(raw_input("middle side: "))
sidec=int(raw_input("largest side: "))
side1=sidea
side2=sideb
side3=sidec
def is_right(sidea,sideb,sidec):
    if sidea<sideb and sideb<sidec:
        if (sidea**2)+(sideb**2)==sidec**2:
            print "This triangle is right."
            return True
        elif (sidea**2)+(sideb**2)!=sidec**2:
            print "This triangle is not right."
            return False
    else:
        side1=side1+0

print is_right(sidea,sideb,sidec)

   # """
    #Takes three side lengths and returns true if triangle is right
    #:param side1: int or float
    #:param side2: int or float
    #:param side3: int or float
    #:return: bool
  #  """
   # return False

# TESTS
# Feel free to add your own tests as needed!

# print ("Divisors Tests")
# "Test 1"
# if divisors(1) == [1]:
#     print("Test 1: PASS")
# else:
#     print("Test 1: FAIL")
#
# "Test 2"
# if divisors(8) == [1,2,4,8]:
#     print("Test 2: PASS")
# else:
#     print("Test 2: FAIL")
#
# "Test 3"
# if divisors(9) == [1,3,9]:
#     print("Test 3: PASS\n")
# else:
#     print("Test 3: FAIL\n")

"""print("Prime Tests")
"Test 4"
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

"Test 5"
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")
"""
L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]
""""""
# print("Intersection Tests")
# "Test 6"
# if intersection(L1, L2) == []:
#     print("Test 6: PASS")
# else:
#     print("Test 6: FAIL")
# #
# "Test 7"
# if intersection(L2, L3) == [3]:
#     print("Test 7: PASS")
# else:
#     print("Test 7: FAIL")
#
# "Test 8"
# if intersection(L2, L4) == []:
#     print("Test 8: PASS")
# else:
#     print("Test 8: FAIL")
#
# "Test 9"
# if intersection(L3, L4) == ["a"]:
#     print("Test 9: PASS")
# else:
#    print("Test 9: FAIL")
#
# "Test 10"
# if intersection(L4, L5) == [5, 7]:
#   print("Test 10: PASS\n")
# else:
#   print("Test 10: FAIL\n")

#print("Is_Right Tests")
#"Test 11"
#if is_right(5, 3, 4):
#  print("Test 11: PASS")
#else:
 #   print("Test 11: FAIL")

#"Test 12"
#if is_right(9, 3, 4):
#  print("Test 12: FAIL")
#else:
#    print("Test 12: PASS")


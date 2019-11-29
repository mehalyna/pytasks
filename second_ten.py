"""1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
import math


def one():
    lst = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 == 0:
            lst.append(str(i))
    return ','.join(lst)


# print(one())


"""2. Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def two(num):
    return 1 if num == 0 else num * two(num - 1)


# num = int(input())
# print(two(num))


"""3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""


def three(i):
    return {i: i * i for i in range(1, 9)} # why only up to 9 ?


# i = int(input())
# print(three(i))


"""4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""


def four(x):
    return x.split(','), tuple(x.split(','))


#
# x = input()
# print(four(x))


"""5. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class Five:
    def __init__(self):
        self.string = ""

    def input(self):
        self.string = input()

    def to_upper(self):
        print(self.string.upper())


# five = Five()
# five.input()
# five.to_upper()


"""6. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""


def six(d):
    c, h = 50, 30
    res = []
    for i in d.split(","):
        print(int(i))
        res.append(math.sqrt((2 * c * int(i)) / h))
    return str(res)


# d = input()
# print(six(d))


""""
7. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th
 row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,...Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""


# X = int(input("Enter x = "))
# Y = int(input("Enter y = "))


def seven(x, y):
    lst = [[i * j for j in range(y)] for i in range(x)]
    return lst


# print(seven(X, Y))


"""8. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
 sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""


def eight(x):
    x = x.split(",")
    x.sort()
    return ",".join(x)


# print(eight("without,hello,bag,world"))


"""
9. Write a program that accepts sequence of lines as input and prints the lines after making all characters 
in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""


def nine(x):
    return x.upper()


# print(nine("Hello world Practice makes perfect"))


"""10. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""


def ten(x):
    x = x.split(" ")
    return " ".join(sorted(set(x)))


print(ten("hello world and practice makes perfect and hello world again"))

"""11. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
"""
import itertools
import re
import math
import zlib
from timeit import Timer
import random


def task_11(x):
    res = []
    for i in x.split(","):
        if int(i, 2) % 5 == 0:
            res.append(i)
    return ",".join(res)


# print(task_11("0100,0011,1010,1001"))


"""
Question 12
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each 
digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def task_12():
    res = []
    for i in range(1000, 3001):
        i = str(i)
        if (int(i[0]) % 2 == 0) and (int(i[1]) % 2 == 0) and (int(i[2]) % 2 == 0) and (int(i[3]) % 2 == 0):
            res.append(i)

    return ",".join(res)


# print(task_12())


"""Question 13
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""


def task_13(x):
    num, let = 0, 0
    for i in x:
        if i.isalpha():
            let = let + 1
        elif i.isdigit():
            num = num + 1
    return "LETTERS " + str(let) + '\n' + "DIGITS " + str(num)


# print(task_13("hello world! 123"))


"""Question 14
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""


def task_14(x):
    upp, low = 0, 0
    for i in x:
        if i.islower():
            low = low + 1
        elif i.isupper():
            upp = upp + 1
    return "UPPER CASE " + str(upp) + '\n' + "LOWER CASE " + str(low)


# print(task_14("Hello world!"))


"""Question 15
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""


def task_15(x):
    x = str(x)
    return int(x) + int(x * 2) + int(x * 3) + int(x * 4)


# print(task_15(9))


"""Question 16
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
"""


def task_16(x):
    res = []
    x = x.split(",")
    for i in x:
        if int(i) % 2 == 1:
            res.append(int(i) * int(i))
    return str(res)[1:-1]


# print(task_16("1,2,3,4,5,6,7,8,9"))


"""Question 17
Write a program that computes the net amount of a bank account based a transaction log from console input.
 The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

# def task_17(x):


"""Question 18
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""


def task_18(x):
    res = []
    x = x.split(",")
    for i in x:
        if 6 > len(i) > 12:
            continue
        else:
            pass
        if not re.search("[a-z]", i):
            continue
        elif not re.search("[0-9]", i):
            continue
        elif not re.search("[A-Z]", i):
            continue
        elif not re.search("[$#@]", i):
            continue
        elif re.search('\s', i):
            continue
        else:
            pass
        res.append(i)
    return ",".join(res)


# print(task_18("ABd1234@1,a F1#,2w3E*,2We3345"))


"""Question 19
You are required to write a program to sort the (name, age, height) tuples 
by ascending order where name is string, age and height are numbers. The tuples are input by console. 
The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
"""


def task_19(x):
    lst = []
    while True:
        x = input().split(',')
        if not x[0]:
            break
        lst.append(tuple(x))
    lst.sort(key=lambda x: (x[0], x[1], x[2]))
    return lst


# print(task_19(input()))


"""Question 20
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
"""


class Iterator(object):
    def __init__(self, n):
        super(Iterator, self).__init__()
        self.n = n

    def div_by_seven(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i


# for num in Iterator(100).div_by_seven():
#     print(num)


"""Question 21
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, 
DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current 
position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""


def task_21(s):
    x, y = 0, 0
    while True:
        s = s.split("")
        if not s:
            break
        if s[0] == 'UP':
            x -= int(s[1])
        if s[0] == 'DOWN':
            x += int(s[1])
        if s[0] == 'LEFT':
            y -= int(s[1])
        if s[0] == 'RIGHT':
            y += int(s[1])
    return round(math.sqrt(pow(x, 2) + pow(y, 2)))


# s = input()
# print(task_21(s))


"""Question 22
Write a program to compute the frequency of the words from the input. The output should output after sorting
 the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""


def task_22(x):
    x = x.split()
    st = sorted(set(x))
    for i in st:
        print("{0}:{1}".format(i, st.count(i)))


task_22("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")

"""Question 23
Write a method which can calculate square value of number
"""


def task_23(x):
    """
    :param x: main parameter that must be calculate square value
    :return: square value of x number
    """
    return x ** 2


"""Question 24
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. 
But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
"""

# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# print(task_23.__doc__)


"""Question 25
Define a class, which have a class parameter and have a same instance parameter.
"""


class Task25:
    x = "Person"

    def __init__(self, x=None):
        self.x = x


"""Question 26
Define a function which can compute the sum of two numbers.
"""


def task_26(x, y):
    return x + y


"""Question 27
Define a function that can convert a integer into a string and print it in console.
"""


def task_27(x):
    return str(x)


print(task_27(9999))

"""Question 29
Define a function that can receive two integral numbers in string form
 and compute their sum and then print it in console.
"""


def task_29(x):
    x = x.split(" ")
    return int(x[0]) + int(x[1])


# print(task_29("10 20"))


"""Question 30
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""


def task_30(x, y):
    return x + y


# print(task_30("hey", "world"))


"""Question 31
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print al l strings line by line.
"""


def task_31(x, y):
    if len(x) > len(y):
        return x
    elif len(x) < len(y):
        return y
    else:
        return x + '\n' + y


# print(task_31("hey", "world"))


"""Question 32
Define a function that can accept an integer number as input and print the "It is an even number" 
if the number is even, otherwise print "It is an odd number".
"""


def task_32(x):
    return "It is an even number" if x % 2 == 0 else "It is an odd number"


# print(task_32(6))


"""Question 33
Define a function which can print a dictionary where the keys are numbers between 1 and 3 
(both included) and the values are square of keys.
"""


def task_33():
    d = dict()
    for i in range(1, 4):
        d[i] = pow(i, 2)
    print(d)


# task_33()


"""
Question 34
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
 and the values are square of keys.
"""


def task_34():
    d = dict()
    for i in range(1, 21):
        d[i] = pow(i, 2)
    print(d)


# task_34()


"""Question 35
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
 and the values are square of keys. The function should just print the values only.
"""


def task_35():
    d = dict()
    for i in range(1, 21):
        d[i] = pow(i, 2)
    print(d.values())


# task_35()


"""Question 36
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
(both included) and the values are square of keys. The function should just print the keys only.
"""


def task_36():
    d = dict()
    for i in range(1, 21):
        d[i] = pow(i, 2)
    return d.keys()


# print(task_36())


"""Question 37
Define a function which can generate and print a list where the values are square of numbers
 between 1 and 20 (both included).
"""


def task_37():
    res = []
    for i in range(1, 21):
        res.append(pow(i, 2))
    print(res)


# task_37()


"""Question 38
Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print the first 5 elements in the list.
"""


def task_38():
    res = []
    for i in range(1, 21):
        res.append(pow(i, 2))
    print(res[:5])


# task_38()


"""Question 39
Define a function which can generate a list where the values are square of numbers between 1 and 20 
(both included). Then the function needs to print the last 5 elements in the list.
"""


def task_39():
    res = []
    for i in range(1, 21):
        res.append(pow(i, 2))
    print(res[-5:])


# task_39()


"""Question 40
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
 Then the function needs to print all values except the first 5 elements in the list.
"""


def task_40():
    res = []
    for i in range(1, 21):
        res.append(pow(i, 2))
    print(res[5:])


# task_40()


"""Question 41
Define a function which can generate and print a tuple where the value are square of numbers between 
1 and 20 (both included). 
"""


def task_41():
    tpl = tuple(pow(i, 2) for i in range(1, 21))
    print(tpl)


# task_41()


"""Question 42
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line
 and the last half values in one line. 
"""


def task_42():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    first = t[:(len(t) // 2)]
    second = t[(len(t) // 2):]
    print(first, '\n', second)


# task_42()


"""Question 43
Write a program to generate and print another tuple whose values are even numbers in the given tuple 
(1,2,3,4,5,6,7,8,9,10). 
"""


def task_43():
    t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    new_t = tuple(i for i in t if i % 2 == 0)
    print(new_t)


# task_43()


"""Question 44
Write a program which accepts a string as input to print "Yes" 
if the string is "yes" or "YES" or "Yes", otherwise print "No". 
"""


def task_44(x):
    if x == "yes" or x == "YES" or x == "Yes":
        print("Yes")
    else:
        print("No")


# task_44("Yes")


"""Question 45
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
"""


def task_45():
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(filter(lambda x: x % 2 == 0, seq))
    return result


# print(task_45())


"""Question 46
Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""


def task_46():
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(map(lambda x: x ** 2, seq))
    return result


# print(task_46())


"""Question 47
Write a program which can map() and filter() to make a list whose elements are square of even number in 
[1,2,3,4,5,6,7,8,9,10].
"""


def task_47():
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, seq)))
    return result


# print(task_47())


"""Question 48
Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
"""


def task_48():
    result = list(filter(lambda x: x % 2 == 0, [i for i in range(1, 21)]))
    return result


# print(task_48())


"""Question 49
Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
"""


def task_49():
    result = list(map(lambda x: x ** 2, [i for i in range(1, 21)]))
    return result


# print(task_49())


"""Question 50
Define a class named American which has a static method called printNationality.
"""

# class American:
#     @staticmethod
#     def printNationality():
#         print("american")


"""Question 51
Define a class named American and its subclass NewYorker. 
"""


class American():
    def __init__(self):
        pass


class NewYorker(American):
    def __init__(self):
        super().__init__()


"""Question 52
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# circle = Circle(5)
# print(circle.area())


"""Question 53
Define a class named Rectangle which can be constructed by a length and width. 
The Rectangle class has a method which can compute the area. 
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length + self.width) * 2


# rect = Rectangle(5, 4)
# print(rect.area())


"""Question 54
Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
"""


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


# sq = Square(3)
# print(Square().area())
# print(sq.area())


"""Question 55
Write a function to compute 5/0 and use try/except to catch the exceptions.
"""


def task_55():
    try:
        return 5 / 0
    except ZeroDivisionError:
        return 0


# print(task_55())


"""Question 56
Define a custom exception class which takes a string message as attribute.
"""


class CustomException(Exception):
    def __init__(self, message):
        self.message = message


"""Question 57
Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address. 
Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_57(x):
    return x[:x.find('@')]


# x = input()
# print(task_57(x))


"""Question 58
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print 
the company name of a given email address. Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_58(x):
    return x[x.find('@') + 1:x.find('.com')]


# x = input()
# print(task_58(x))


"""Question 59
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed 
of digits only.Example:
If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_59(x):
    x = x.split()
    return [i for i in x if i.isdigit()]


# print(task_59("2 cats and 3 dogs."))


"""Question 60
Print a unicode string "hello world".
"""


def task_60():
    return u"hello world!"


# print(task_60())


"""Question 61
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
"""


# s = input()

def task_61(s):
    u = s.encode('utf-8')
    return u


# print(task_61(s))

"""Question 62
Write a special comment to indicate a Python source code file is in unicode.
"""

# -*- coding: utf-8 -*-

"""Question 63
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


# n = int(input())


def task_63(n):
    sum = 0
    for i in range(1, n + 1):
        sum += float(float(i) / (i + 1))
    return sum


# print(task_63(n))

"""Question 64
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_64(n):
    if n == 0:
        return 1
    return task_64(n - 1) + 100


# print(task_64(5))


"""Question 65
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
13
In case of input data being supplied to the question, it should be assumed to be a console input.
"""


def task_65(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return task_65(n - 1) + task_65(n - 2)


# print(task_65(7))
"""Question 66
The Fibonacci Sequence is computed based on the following formula:


f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
"""


def task_66(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return task_65(n - 1) + task_65(n - 2)


# print(task_66(7))


"""Question 67
Please write a program using list comprehension to print the Fibonacci Sequence 
in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
"""


def task_67(n):
    if n == 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        print(task_65(n - 1) + task_65(n - 2))
        return task_65(n - 1) + task_65(n - 2)


# print(task_67(7))


"""Question 68
Please write a program using generator to print the even numbers between 0 and n in comma separated
 form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
"""


def task_68(n):
    res = []
    for i in range(0, n + 1):
        if i % 2 == 0:
            res.append(str(i))
    return ",".join(res)


# print(task_68(int(input())))


"""Question 69
Please write a program using generator to print the numbers which can be divisible 
by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
"""


def task_69(n):
    res = []
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            res.append(str(i))
    return ",".join(res)


# print(task_69(int(input())))


"""Question 70
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
"""


def task_70():
    li = [2, 4, 6, 8]
    for i in li:
        assert i % 2 == 0


# print(task_70())
"""Question 71
Please write a program which accepts basic mathematic expression from console and print the evaluation result.
Example:
If the following string is given as input to the program:
35+3
Then, the output of the program should be:
38
"""


def task_71(expression):
    return eval(expression)


# print(task_71(input()))

"""Question 72
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.
"""


def task_72(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index


# print(task_72([2, 5, 7, 9, 11, 17, 222], 5))


"""Question 73
Please write a binary search function which searches an item in a sorted list. 
The function should return the index of element to be searched in the list.
"""


def task_73(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index


# print(task_73([2, 5, 7, 9, 11, 17, 222], 5))


"""Question 74
Please generate a random float where the value is between 10 and 100 using Python math module.
"""


def task_74():
    return random.uniform(10.0, 100.0)


# print(task_74())


"""Question 75
Please generate a random float where the value is between 5 and 95 using Python math module.
"""


def task_75():
    return random.uniform(5.0, 95.0)


# print(task_75())


"""
Question 76
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
"""


def task_76():
    return [random.randrange(0, 10, 2)]


# print(task_76())


"""Question 77
Please write a program to output a random number, which is divisible by 5 and 7,
 between 0 and 10 inclusive using random module and list comprehension.
"""


def task_77():
    return random.choice([i for i in range(0, 11) if i % 5 == 0 and i % 7 == 0])


# print(task_77())

"""Question 78
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
"""


def task_78():
    return random.sample(range(100, 201), 5)


# print(task_78())


"""Question 79
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
"""


def task_79():
    return random.sample([i for i in range(100, 201) if i % 2 == 0], 5)


# print(task_79())


"""Question 80
Please write a program to randomly generate a list with 5 numbers, 
which are divisible by 5 and 7 , between 1 and 1000 inclusive.
"""


def task_80():
    return random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5)


# print(task_80())


""""Question 81
Please write a program to randomly print a integer number between 7 and 15 inclusive.
"""


def task_81():
    return random.randrange(7, 16)


# print(task_81())


"""Question 82
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
"""


def task_82():
    s = 'hello world!hello world!hello world!hello world!'.encode()
    k = zlib.compress(s)
    print(k)
    print(zlib.decompress(k))


# print(task_82())


"""Question 83
Please write a program to print the running time of execution of "1+1" for 100 times.
"""


def task_83():
    t = Timer("for i in range(0,101):1+1")
    return t.timeit()


# print(task_83())


"""Question 84
Please write a program to shuffle and print the list [3,6,7,8]
"""


def task_84():
    lst = [3, 6, 7, 8]
    random.shuffle(lst)
    return lst


print(task_84())

"""Question 85
Please write a program to shuffle and print the list [3,6,7,8]
"""


def task_85():
    lst = [3, 6, 7, 8]
    random.shuffle(lst)
    return lst


print(task_85())

"""Question 86
Please write a program to generate all sentences where subject is in ["I", "You"] 
and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
"""


def task_86():
    for i in ["I", "You"]:
        for j in ["Play", "Love"]:
            for k in ["Hockey", "Football"]:
                print(i + " " + j + " " + k)


# task_86()


"""Question 87
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
"""


def task_87():
    lst = [5, 6, 77, 45, 22, 12, 24]
    for i in lst:
        if i % 2 == 0:
            lst.remove(i)
    return lst


# print(task_87())


"""Question 88
By using list comprehension, please write a program to print the list after
 removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""


def task_88():
    lst = [12, 24, 35, 70, 88, 120, 155]
    for i in lst:
        if i % 5 == 0 and i % 7 == 0:
            lst.remove(i)
    return lst


# print(task_88())


"""Question 89
By using list comprehension, please write a program to print the list after removing the 0th,
 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
"""


def task_89():
    lst = [12, 24, 35, 70, 88, 120, 155]
    return [lst[i] for i in range(len(lst)) if i not in [0, 2, 4, 6]]


# print(task_89())


"""Question 90
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
"""


def task_90():
    return [[[0 for col in range(8)] for col in range(5)] for row in range(3)]


print(task_90())

"""Question 91
By using list comprehension, please write a program to print the list after
 removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
"""


def task_91():
    lst = [12, 24, 35, 70, 88, 120, 155]
    return [lst[i] for i in range(len(lst)) if i not in [0, 4, 5]]


# print(task_91())


"""Question 92
By using list comprehension, please write a program to print the list after removing the 
value 24 in [12,24,35,24,88,120,155].
"""


def task_92():
    lst = [12, 24, 35, 24, 88, 120, 155]
    return list(filter(lambda a: a != 24, lst))


# print(task_92())


"""
Question 93
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements are intersection of the above given lists.
"""


def task_93():
    lst = [1, 3, 6, 78, 35, 55]
    lst1 = [12, 24, 35, 24, 88, 120, 155]
    res = []
    for i in lst:
        for j in lst1:
            if i == j:
                res.append(i)
    return res


# print(task_93())


"""Question 94
With a given list [12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing all duplicate values with original order reserved.
"""


def task_94():
    lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res


# print(task_94())


"""
Question 95
Define a class Person and its two child classes: Male and Female.
 All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""


class Person:
    def getGender(self):
        print("Person")


class Male(Person):
    def getGender(self):
        print("Male")


class Female(Person):
    def getGender(self):
        print("Female")


male = Male()
female = Female()
# male.getGender()
# female.getGender()


"""Question 96
Please write a program which count and print the numbers of each character in a string input by console.
Example:
If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""


def task_96(string):
    st = set(string)
    dict = {i: string.count(i) for i in st}
    dict = {key: dict[key] for key in sorted(dict.keys())}
    for i in dict.keys():
        print(str(i) + "," + str(dict[i]))


# task_96(input())

"""Question 97
Please write a program which accepts a string from console and print it in reverse order.
Example:
If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:
ris etov ot esir
"""


def task_97(x):
    return x[::-1]


# print(task_97(input()))


"""Question 98
Please write a program which accepts a string from console and print the characters that have even indexes.
Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
"""


def task_98(x):
    return x[::2]


# print(task_98(input()))


"""Question 99
Please write a program which prints all permutations of [1,2,3]
"""


def task_99():
    return list(itertools.permutations([1, 2, 3]))


# print(task_99())


"""Question 100
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
 How many rabbits and how many chickens do we have?
"""


def task_100(head, leg):
    print("rabbits "+str(94//2-35)+" chikens " + str(35-(94//2-35)))


print(task_100(35, 94))

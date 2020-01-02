
import sys
import string

tabus = list(string.ascii_lowercase[13:])


def printer_error(s):
    counter = 0
    for x in range(len(tabus)):
        counter += s.count(tabus[x])

    return "" + str(counter) + "/" + str(len(s))


print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))


# Simple, given a string of words, return the length of the shortest word(s).

# tring will never be empty and you do not need to account for different data types.

def find_short(s):
    listOfString = s.split()
    l = len(s)
    for i in listOfString:
        temp = len(i)
        if temp < l:
            l = temp

    return l  # l: shortest word length


find_short("bitcoin take over the world maybe who knows perhaps")


'''A digital root is the recursive sum of all the digits in a number.
Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers.'''


digit = []


def get_digit(num):
    digit.clear()
    if num < 10:
        digit.append(num)
    else:
        get_digit(num // 10)
        digit.append(num % 10)
    return digit


def digital_root(n):
    mylist = get_digit(n)
    while len(mylist) != 1:
        sum = 0
        for i in mylist:
            sum += i

        mylist = []
        mylist = get_digit(sum)

    return sum


digital_root(493193)

'''
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word(not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

'''


def order(sentence):

    solution = ''
    counter = 1
    for k in sentence.split():
        for i in sentence.split():
            if i.count(str(counter)) == 1:
                solution += ' ' + i
                counter += 1

    return solution


order("is2 Thi1s T4est 3a")


'''Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet:
a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.'''


def high(x):
    bestscore = 0
    winner = ''
    for i in x.split():
        score = 0

        for k in i:

            score += int(string.ascii_lowercase.index(k)) + 1


int(string.ascii_lowercase.index(k))
        if score > bestscore:
            bestscore = score
            winner = i

    return winner


high('man i need a taxi up to ubud')
'''
Write a function that when given a URL as a string, 
parses out just the domain name 
and returns it as a string. For example:
'''


def domain_name(url):
    url = url.replace('www', '')
    url = url.replace('http://', '')
    url = url.replace('https://', '')
    url = url.replace('ftp', '')

    return url[0:url.index('.')]


print(domain_name("www.ibg.com.tr"))



'''''''''''''''''''''
'''''''''''''''''''''
def anagrams(word, words):
    mylist = []
    word = sorted(word)
    for i in words:
        if word == sorted(i):
            mylist.append(i)

    return mylist


anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])


'''''
ROT13 is a simple letter substitution cipher that replaces a letter 
with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and 
returns the string ciphered with Rot13. If there are numbers or special characters included 
in the string, they should be returned as they are. Only letters 
from the latin/english alphabet should be shifted,
 like in the original Rot13 "implementation".
''''

import string


def rot13(message):
    cyriptedMessage = ''
    for i in message:
        if i.isalpha():
            if i.isupper():
                if (int(string.ascii_uppercase.index(i)) + 13) < 25:
                    cyriptedMessage += string.ascii_uppercase[int(string.ascii_uppercase.index(i)) + 13]
                else:
                    cyriptedMessage += string.ascii_uppercase[int( string.ascii_uppercase.index(i)) + 13 - 26]
            else:
                if (int(string.ascii_lowercase.index(i)) + 13) < 25:
                    cyriptedMessage += string.ascii_lowercase[int(string.ascii_lowercase.index(i)) + 13]
                else:
                    cyriptedMessage += string.ascii_lowercase[int(string.ascii_lowercase.index(i)) + 13 - 26]
        else:
            cyriptedMessage += i

    return cyriptedMessage


rot13('Test')



# Pete, the baker

def cakes(recipe, available):
    a = 0
    while True:
        for k in recipe:
            try:
                if available[k] - recipe[k] >= 0:
                    available[k] = available[k] - recipe[k]
                else:
                    return a
            except KeyError:
                return 0
        a += 1


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

cakes(recipe, available)

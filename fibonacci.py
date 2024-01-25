- 👋 Hi, I’m @prachisharma19
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
prachisharma19/prachisharma19 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
***Display Fibonacci Sequence using recusrion***
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n = int(input("Enter a number here: "))

if n<= 0 :
    print("Enter opposite number")
else:
    print("Fibonacci sequence")
    for i in range(n):
        print(fibo(i))

***Python program to find sum of natural numbrers using recursion***
    def NNS(n):
    if n <= 1:
        return n 
    else:
        return (n)+NNS(n-1)
n = int(input("Enter a number here: "))

if n <= 0:
    print("Enter a positive number: ")
else:
    print("the sum of natural number upto given number is", NNS(n))

***Python program to find factorial of number using recursion***
def fact(n):
    if n == 1:
        return 1
    else:
        return (n* fact(n-1))
        
        
n = int(input("Enter a number here : "))
if n <= 0:
    print("Factorial of number less than 1 does not exists")
else:
    print("Factorial of the given number is", fact(n))
*** Convert decimal into binary**
def ConvertBinary(n):
    if n > 1:
        ConvertBinary(n//2)
    print(n%2,end = "")
print("The binary of the given number is: ")
ConvertBinary(15)
***Python Program to transpose a matrix***
A = [[1,5,8],
     [4,6,7],
     [7,2,3]]
B = [[4,5,6],
     [8,9,1],
     [3,5,6]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result [i][j] = A[i][j] + B[i][j]
        
for r in result:
  print(r)
***Palindrome***
a = input("enter a  word here")

rev = a[::-1]

if a ==  rev:
    print("It is a palindrome number")
else:
    print("It is not a palindrome")
***Python program to remove punctuations from a string***
punc = """!()-[ {;'"\,<>./?@#$^*"""

string = input("Enter anything here: ")
empty_str = ""

for  i in string:
    if i not in punc:
        empty_str += i
print(empty_str)

***Display a program to multiply two matrices***
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = [[1,2,1,1],
     [4,2,1,2],
     [6,3,4,1]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]    
          
          
for i in range (len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
for i in result:
  print(i)
***Display python program to sort words in alphabetic order***
    a = "Harry potter and the goblet of fire"

w = a.split()
print(w)
for i in range(len(w)):
    w[i] = w[i].lower()
print(w)
w.sort()
print(w)
for i in w:
    print(i)
***Display python program to Illustrate Different set operations***
A = {1,2,3,6,8,9}
B = {3,4,5,6,7,8}

print("The union is ", A|B)

print("The intersection is ", A & B)

print("The Difference is ", A - B)

print("The Symmetric Difference is ", A ^ B)
***Display current time***
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
***Display python program to count the number of each vowel using dictionary***
    a = "Harry Potter and the Prisoner of Azkaban"

vowels = "aeiou"
a = a.casefold()
print(a)

count = {}.fromkeys(vowels,0)

for char in a:
    if char in count:
        count[char]+=1
        
print(count)
***Display python program to count the number of each vowel using list and dictionary comprehen***
a = "Harry Potter and the Prisoner of Azkaban"

vowels = "aeiou"
a = a.casefold()
print(a)

count = {key:sum([1 for char in a if char == key]) for key in vowels}
print(count)
***Display python program to find the size (resolution) of a image***
import PIL
from PIL import image

img =PIL.image.open("https://unsplash.com/photos/a-bunch-of-pink-donuts-are-stacked-on-top-of-each-other-obyYZVKwCNI")
width, height = img.size

print(width,"x", height)

***Python program to merge two dictionaries using operator***
dict1 = {"John":89, "Lisa": 99}
dict2 = {"Lisa":94, "Peter":78}

print(dict1|dict2)
***Python program to merge two dictionaries using update method***
dict1 = {"John":89, "Lisa": 99}
dict2 = {"Lisa":94, "Peter":78}

dict3 = dict2.copy()
print(dict3.update(dict1))

print(dict3)

***Display program to safely create a nested directory***
from pathlib import Path
Path("").mkdir(parents=True,exist_ok=True)

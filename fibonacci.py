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

***
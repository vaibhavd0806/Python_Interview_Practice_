 # =========================================================
# 01.What is __init__ in python?
# class student:
#     def __init__(self,Name,Age,Salary):
#         self.name = Name
#         self.age = Age
#         self.salary = Salary
#
#     def display(self):
#         print(f'Name of the student is: {self.name}')
#         print(f'Name of the student is: {self.age}')
#         print(f'Name of the student is: {self.salary}')
#
# s1 = student('Vaibhav',19,55000)
# s1.display()


# =======================================================================
# 02.What is difference between array and list?
# Array =>  Element in the array are of same data type
#      => We have to import module "Import array" before performing any
#           operation on array which increses the overall performance.

# List => Element in the list can be of different data types

# Bilkul Vaibhav! 😎
# Neeche maine **Array vs List in Python** ka comparison **Hindi-English mix** mein simple aur interview-ready **notes** format mein likha hai — short, clean, and clear:

# ### 🔹 **1. Data Type:**
# - **Array** ➤ Sirf **same data type** ke elements store karta hai.
#   > Example: `[1, 2, 3, 4]` (All integers)

# - **List** ➤ **Different data types** ke elements store kar sakta hai.
#   > Example: `[1, "hello", 3.5]`

# ### 🔹 **2. Module Requirement:**
# - **Array** ➤ Python ka built-in `array` module import karna padta hai.
#   > Syntax: `from array import array`

# - **List** ➤ Built-in data structure hai. Koi module import karne ki zarurat nahi.

# ### 🔹 **3. Performance:**
# - **Array** ➤ Jab sab elements same type ke hote hain, to **virtual machine ko type check nahi karna padta baar-baar**, isliye operations **fast** hote hain.
#   > Especially useful in **numerical & mathematical calculations**.

# - **List** ➤ Thoda slow hota hai kyunki har element ka type alag ho sakta hai — interpreter ko har element ka type check karna padta hai.

# ### 🔹 **4. Memory Efficiency:**
# - **Array** ➤ Zyada **memory-efficient** hota hai, kyunki fixed-type data store karta hai.
# - **List** ➤ Flexible hota hai, but **thoda zyada memory use karta hai**.

# ### 🔹 **5. Use Case:**
# - **Array** ➤ Jab **large amount of numerical data** handle karna ho aur performance important ho.
# - **List** ➤ Jab data mixed ho ya general-purpose kaam ho.

# ### 🔹 **6. Example Code:**
# #### ✅ Array:
# ```python
# from array import array
# arr = array('i', [1, 2, 3, 4])  # 'i' = integer type
#
#
# #### ✅ List:
# ```python
# lst = [1, "hello", 3.5, True]

# ## 🔚 Summary Line for Interview:
# > "Array is used when we want **faster computation** with **same data types**, while List is more **flexible** and used for **general purposes**, even though it's a bit **slower** and uses **more memory**."

# Agar tu chahe toh main iska **PDF version** bhi bana deta hoon ya tujhe ek **PowerPoint slide-style** presentation format mein bhi ready kar deta hoon!



# ========================================================================
# 03. What is slicing?
# Slicing name itself suggest is to slice the data
# Slicing can be done on strings, arrays, lists, and tuples.

# for example
# Syntax => a[First index : lastindex + 1 : Step]
# a = (1,2,4,3,5)
# print(a[1:3])



###################################################################
# 04. What is break, continue and pass in Python?



###################################################################
# 05. How is class is created in the python?
# =====>
# class createclass:
#     class_attribute = "I am the class attribute"
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def display(self):
#         print('Addition of the number: ', self.a + self.b)
#
#
# obj = createclass(12,34)
# obj.display()


##################################################################
#  06. Print fibonacci series of n elements

# ==============> Way 01 <=========================

# n = int(input("Enter the value of n: "))
# # a,b = map(int,input("Enter the value of a,b: ").split())
# a = int(input("Enter the value of a:"))
# b = int(input("Enter the value of b:"))
#
# for i in range(n):
#     print(a, end = " ")
#     a, b = b , a + b

# ==============> Way 02 Using OOPS <=========================

# class FibonacciSeries :
#     def __init__(self,n_term):
#         self.n = n_term
#
#     def Generate(self):
#         a = int(input("Enter the value of a: "))
#         b = int(input("Enter the value of b: "))
#
#         for i in range(self.n):
#             print(a,end =" ")
#             a,b = b , a+b
#
# terms = int(input("Enter the value of n terms:"))
#
# if terms < 0:
#     print("Enter the positive value")
# else:
#     obj = FibonacciSeries(terms)
#     obj.Generate()



##################################################################
# 07. Palindrome
# abc = cba => racecar is a palindrome string

# ==================> FOR STRING <===========================
# s = input("Enter the string: ")
# start = 0
# end = len(s) - 1
#
# while start < end:
#     if s[start] == s[end]:
#         start += 1
#         end -= 1
#     else:
#         break
# if start >= end:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")


# class ispalindrome :
#     def __init__(self,string):
#         self.s = string
#
#     def ispalindromecheck(self):
#         start = 0
#         end = len(self.s) - 1
#
#         while start < end:
#             if self.s[start] == self.s[end]:
#                 start += 1
#                 end -= 1
#             else:
#                 print("It is not palindrome")
#                 return
#
#         print("It is palindrome")
#
# string = input("Enter the string: ")
# obj = ispalindrome(string)
# obj.ispalindromecheck()


# ==================> FOR INTEGER <===========================

# num = int(input("Enter the value of number: "))
# s = str(num)
#
# start = 0
# end = len(s) - 1
#
# while start < end:
#     if s[start] == s[end]:
#         start += 1
#         end -= 1
#     else:
#         break
#
# if start >= end:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

### USING OOPS
# class ispalindrome :
#     def __init__(self,num):
#         self.n = num
#
#     def ispalindromecheck(self):
#         start = 0
#         end = len(self.n) - 1
#
#         while start < end:
#             if self.n[start] == self.n[end]:
#                 start += 1
#                 end -= 1
#             else:
#                 print("It is not palindrome")
#                 return
#
#         print("It is palindrome")
#
# a = int(input("Enter the string: "))
# num = str(a)
# obj = ispalindrome(num)
# obj.ispalindromecheck()



#=========================================================
# 08, Armstrong Number => A number is called an Armstrong number
# if sum of each digit raised to the power of total digits
# is equal to the original number.

#  153 => 1^3 + 5^3 + 3^3
#      => 1 + 125 + 27
#      => 153
#  153 is a Armstrong Number


#============ Way 01 without using OOPS ============================

# num = int(input("Enter the number: "))
# temp = num
# n = len(str(num))
# sum = 0
#
# while temp > 0:
#     digit =  temp % 10
#     sum += digit ** n
#     temp //= 10
#
# if sum == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")


#============ Way 02 with using OOPS ============================
# class armstrong_num:
#
#     def __init__(self,num):
#         self.n = num
#
#     def generate(self):
#         temp = self.n
#         a = len(str(self.n))
#         sum = 0
#
#         while temp > 0:
#             digit = temp % 10
#             sum += digit ** a
#             temp = temp // 10
#
#         if sum == self.n:
#             print("Number is armstrong")
#         else:
#             print("Number is not armstrong")
#
# num = int(input("Enter the number :"))
# obj = armstrong_num(num)
# obj.generate()



#=========================================================
#  09. Swapping two numbers without using third variable and a,b = b,a
# No tuple unpacking shortcut

# a,b = map(int,input("Enter the Number: ").split())
# print(f'Before Swapping a = {a} and b = {b}')
# a = a + b
# b = a - b
# a = a - b
# print(f'Before Swapping a = {a} and b = {b}')


#========================== Way 02 Using OOPS =========================
# class Swapper:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def swap(self):
#         print(f"Before swapping: a = {self.a}, b = {self.b}")
#
#         self.a = self.a + self.b
#         self.b = self.a - self.b
#         self.a = self.a - self.b
#
#         print(f"After swapping: a = {self.a}, b = {self.b}")
#
# a,b = map(int,input("Enter the Number: ").split())
# obj = Swapper(a, b)
# obj.swap()

#======================= Way 03 Using Bitwise XOR ==========================
# class BitwiseSwapper:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def swap(self):
#         print(f"Before swapping: a = {self.a}, b = {self.b}")
#
#         self.a = self.a ^ self.b
#         self.b = self.a ^ self.b
#         self.a = self.a ^ self.b
#
#         print(f"After swapping: a = {self.a}, b = {self.b}")
#
# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
#
# obj = BitwiseSwapper(a, b)
# obj.swap()


# ===========================================================
# 10. Factorial

# ################### Way 1 : Using FOR Loop ################
# num = int(input("Enter the number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print("Factorial is:", fact)

# # ################# Way 2 : Using FOR Loop (OOPS) ###########

# Yahan self.name mein Vaibhav gaya, aur self ne manager ko bataya ki kis bande se baat ho rahi hai.

# class Factorial:
#      def __init__(self, num):
#          self.n = num
#
#      def generate(self):
#          fact = 0
#
#          for i in range(1, self.n + 1):
#              fact = fact * i
#
#          print(f'Factorial of the number: ', fact)
#
# num = int(input("Enter the value of the number: "))
# s1 = Factorial(num)
# s1.generate()


# ################## Way 3 : Using recursion method ###########
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# num = int(input("Enter the number: "))
# print("Factorial is:", factorial(num))


# 11. Can you write a Python program to count the number of vowels in a string?

# ===============> Way 01 : Using simple for loop <======================
# l = input("Enter the string: ")
# a = 'aeiouAEIOU'
# count = 0
# for ch in l:
#     if ch in a:
#         count += 1
# print(f'Count of the vowels in the string is: {count}')

# ==============> Way 02 : Using list comprehension <===================
# l = input("Enter the string: ")
# a = 'aeiouAEIOU'
# count = len([ch for ch in l if ch in a])
# print(f'Count: {count}' )


# n = int(input("Enter the value: "))
# l = []
#
# fr i in range(n+1):
#     a = input("Enter the names: ")
#     l.append(a)
#
# print(f'Names of the employeee are: {l}'


# ==================================================================
# 12. Count the frequency of each character in a string

# ===============> Using simple way <=======================
# s = input("Enter the string: ")
# freq = {}
#
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
#
# # print(f'frequency of each char in the string is :{freq}')
# for k,v in freq.items():
#     print(f'{k} : {v}')


# ===============> Way 2 Uisng OOPS <=======================
# class charfrequency:
#     def __init__(self,string):
#         self.s = string
#
#     def generate(self):
#         freq = {}
#         for ch in self.s:
#             if ch in freq:
#                 freq[ch] += 1
#             else:
#                 freq[ch] = 1
#
#         for k,v in freq.items():
#             print(f'Frequency of {k} is {v}')
#
# string = input("Enter the string: ")
# obj = charfrequency(string)
# obj.generate()


# ================================================================
# 13. Write a Python program using OOPS to take a list of integers from the user, remove the duplicates, and return the list in sorted order (ascending).
# n = list(map(int, input("Enter the list of integers: ").split()))
#
# n.sort()  # Sorting the list first
# output = [] # To store unique values
#
# for i in n: # Loop for adding unique elements
#     if i not in output:
#         output.append(i)
# print("Sorted list without duplicates:", output)






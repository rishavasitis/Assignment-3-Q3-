#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def Letter(str):
    a1,a2=0,0
    for i in s:
        if i.isupper():
            a1+=1
        elif i.islower():
            a2+=1
    print("No. of Upper case characters :-",a1)
    print("No. of Lower case Characters:-",a2)
s=input("Enter Something:(string only)---->")
Letter(s)   
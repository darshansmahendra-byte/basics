a=input("Enter the surname: ")
print("============NET WORTH CALCULATOR============")
print("Surname: ", a)
if a=="jena":
    d=10000000
else:
    b=int(input("Enter the total income: "))
    c=int(input("Enter the total expenses: "))
    d=b-c

print("Networth: ",d,"dollars")
choice=input("Do you want to calculate networth in rupees? (yes/no): ")
if choice=="yes":
    d=d*92.91
    print("Networth in rupees: ",d)
else:
    print("Thank you for using the net worth calculator.")
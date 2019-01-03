print("----------Welcome to GST Calculator-------------")
print("================================================")
print("Input Tax Calculation")
def a():
    print("Enter the Product id:")
    p = int(input())
    if p == 100:
        globals()['x'] = 0.05
    else:
        print("You Have entered wrong Id")
        a()

a()
print("Tax for the product is", x)
print("Enter the price of 1 Raw material Bought:")
RPrice = int(input())
print("Enter the Quantity of raw material")
n = int(input())

RTax = RPrice * x
ITax =RTax * n
Q=RPrice*n
ITax =ITax+Q
print("Raw material price with tax :", ITax)
print("Output tax Calculation")
def b():
    print("Enter the Product Id of Manufactured")
    a =int(input())
    if a==101:
        globals()["Tax"]=0.08
    else:
        print("Renter The Id..")
        b()
b()
print("Tax for the Manufactured Material is:", Tax)
print("Enter the selling price of your Product:")
s = int(input())
print("Enter the Quantity of Items sold:")
t=int(input())

Mtax = s * Tax
GTax = Mtax * t
W=s*t
GTax=GTax+W

print("Output Tax is:", GTax)

if GTax > ITax:
    GST=GTax-ITax
    Credits=0
elif GTax < ITax:
    Credits=ITax-GTax
    GST=0
else:
    GST=0
    Credits=0

print("GST TO BE PAID IS:", GST)
print("YOUR CREDIT BALANCE:", Credits)





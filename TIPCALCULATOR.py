print("This is a tip calculator. The tip amount would be 1% of your order size.")
a = float(input("Enter the value of your meal order"))
b = a*0.01
print("The order value of the meal is"+" "+str(a))
print("The tip amount shall be"+" "+str(b))
print("In total you would have to pay"+" "+str(float(a)+float(b)))
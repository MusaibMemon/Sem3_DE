# Write a prog that given an amount of change less than 1$ it will print out exactly how many quarters, dimes, nickels and pennies will needed to efficiently manage
# Quarter = 25cent
# Dime = 10cent
# Nickel = 5cent
# Penny = 1cent

def change(amount):
    cent = int(amount*100)
    q = cent//25
    cent%=25
    d = cent//10
    cent%=10
    n = cent//5
    cent%=5
    p = cent
change= float(input("Enter amount < 1$ = "))
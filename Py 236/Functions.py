# # Variable Argument
def sum(*n):
    total=0
    for i in n :
        total+=i
    print("The Sum is ",total)
sum(1,2)

#  Variable Number of Argument
def display(**kwards):
    for key,value in kwards.items():
        print(key, ":", value)
display(name="python")
display(name="java", age=100)
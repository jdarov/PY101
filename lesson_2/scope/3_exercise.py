num = 5

def my_func():
    global num
    num = 10

my_func()
print(num) #prints 10, global variables will change variable assignment even with the local f(x)
#reassignment
def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func() #'Inner 1: 25, Inner 2:15', x is not defined in local scope of inner func2
#and two seperate functions can not access each others local variables

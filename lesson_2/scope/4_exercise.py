def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer() #prints 'Hello World' as outer scope can be accessed within the inner function
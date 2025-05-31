def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (1 or "no")

print(bar(foo()))
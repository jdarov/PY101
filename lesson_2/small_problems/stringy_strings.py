def stringy(integer):
    return ''.join([str(x%2) for x in range(1, integer+1)])

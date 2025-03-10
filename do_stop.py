def stop_zero():
    x = 1 / 0

def stop_recursion():
    stop_recursion()

def stop_type():
    x = 1 + '1'

def stop_index():
    x = [1, 2, 3]
    x[3]

if __name__ == '__main__':
    pass
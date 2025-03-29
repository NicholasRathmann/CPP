def do_nothing():
    pass

def do_nothing_for_a_while():
    for i in range(1000000):
        for j in range(1000000):
            for k in range(1000000):
                pass

if __name__ == '__main__':
    do_nothing()
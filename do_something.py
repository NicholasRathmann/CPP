def elastic(m1, v1, m2, v2):
    vcm = (m1 * v1 + m2 * v2) / (m1 + m2)
    print("vcm: " + str(vcm))
    v1cm = v1 - vcm
    print("v1cm: " + str(v1cm) + "\nv1fcm: " + str(-1 * v1cm))
    v1f = (-1 * v1cm) + vcm
    print("v1f: " + str(v1f))
    v2cm = v2 - vcm
    print("v2cm: " + str(v2cm) + "\nv2fcm: " + str(-1 * v2cm))
    v2f = (-1 * v2cm) + vcm
    print("v2f: " + str(v2f))
    pass

if __name__ == '__main__':
    while(True):
        try:
            m1 = float(input("enter value for m1\n"))
            break
        except ValueError:
            print("needs to be a float\n")
    while(True):
        try:
            v1 = float(input("enter value for v1\n"))
            break
        except ValueError:
            print("needs to be a float\n")
    while(True):
        try:
            m2 = float(input("enter value for m2\n"))
            break
        except ValueError:
            print("needs to be a float\n")
    while(True):
        try:
            v2 = float(input("enter value for v2\n"))
            break
        except ValueError:
            print("needs to be a float\n")

    elastic(m1, v1, m2, v2)
    pass
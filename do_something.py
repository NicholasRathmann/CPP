def elastic(m1, v1, m2, v2):
    vcm = (m1 * v1 + m2 * v2) / (m1 + m2)
    print("vcm: " + str(vcm))
    v1cm = v1 - vcm
    print("v1cm: " + str(v1cm) + "\nv1fcm: " + str(-1 * v1cm))
    v1f = (-1 * v1cm) + vcm
    print("v1f: " + str(v1f))
    v2cm = v2 - vcm
    print("v2cm: " + str(v2cm) + "\n v2fcm: " + str(-1 * v2cm))
    v2f = (-1 * v2cm) + vcm
    print("v2f: " + str(v2f))
    pass

if __name__ == '__main__':
    m1 = 4000
    v1 = 0.095
    m2 = 7500
    v2 = -0.095
    elastic(m1, v1, m2, v2)
    pass
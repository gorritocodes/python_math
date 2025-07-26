# put a zero in or the unknown value
n1 = 1
d1 = 2
n2 = 0
d2 = 16

original = [n1,d1]
newArr = [n2,d2]
def proportion(n1,d1,n2,d2):
    if n2 == 0:
        answer = d2 * n1 / d1
        print("n2 = ", answer)
    if d2 == 0:
        answer = d1*n2/n1
        print("d2 = ", answer)

proportion(n1,d1,n2,d2)
proportion(n1,d1,d2,n2)
proportion(*original,*newArr)
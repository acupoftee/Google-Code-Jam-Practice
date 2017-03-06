fin = open("A-large-practice.in", "r")
fout = open("A-large-practice.out", "w")
T = int(fin.readline())


def get_discount_prices(P):
    disc = []
    original = []
    for p in P:
        if p in original:
            original.remove(p)
        else:
            disc.append(p)
            original.append(p * (4 / 3))
    return disc

for t in range(T):
    N = int(fin.readline())
    P = map(int, fin.readline().split(" "))
    disc = get_discount_prices(P)
    output = " ".join(map(str, disc))
    outStr = "Case #{0}: {1}".format(t + 1, output)
    print(outStr)
    fout.write(outStr + "\n")

def num2rom(cur, one, five, ten):
    if cur <= 3:
        return cur * one
    elif cur == 4:
        return one + five
    elif cur >= 5 and cur <= 8:
        return five + (cur - 5) * one
    else:
        return one + ten
def num2rom2(cur, one, five):
    if cur <= 4:
        return cur * one
    else:
        return five + (cur - 5) * one
print "Integer to Roman  (Type 'end' to quit)"
while True:
    o = raw_input("Type a numer up to 1.000.000: ")
    if o == "end":
        break
    try:
         int(o)
    except ValueError:
        print "Error"
    else:
        if int(o) > 1000000:
            print "I need smaller or equal to one million"
            continue
        nym = list(o)
        if len(nym) != 7:
            for i in range (7 - len(nym)):
                nym.insert(0, 0)
        a = int(nym [0]) * "M"
        b = num2rom(int(nym[1]), "C", "D", "M")
        c = num2rom(int(nym[2]), "X", "L", "C")
        d = num2rom2(int(nym[3]), "M", "V")
        e = num2rom(int(nym[4]), "C", "D", "M")
        f = num2rom(int(nym[5]), "X", "L", "C")
        g = num2rom(int(nym[6]), "I", "V", "X")
        h = int(nym[0]) * "_"
        i = num2rom(int(nym[1]), "_", "_", "_")
        j = num2rom(int(nym[2]), "_", "_", "_")
        k = num2rom2(int(nym[3]), " ", "_")
        print(h + i + j + k)
        print a + b + c + d + e + f + g 
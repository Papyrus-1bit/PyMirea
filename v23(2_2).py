def toBin(x) -> str:
    val = bin(x).lstrip('0b')
    if len(val) < 32:
        for i in range(0,32 - len(val)):
            val = '0' + val
    A = val[22:]
    B = val[14:22]
    C = val[13]
    D = val[11:13]
    E = val[9:11]
    F = val[4:9]
    G = val[2:4]
    H = val[0:2]
    kal = A + E + H + G + B + C + D + F
    h = hex(int(kal, base=2))

    return h

def main():
    print(
       toBin(0x570fcdea) 
    )

if __name__ == '__main__':
    main()
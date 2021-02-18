def f(x) -> str:
    arg = bin(x).lstrip('0b')
    
    if len(arg) < 32:   
        arg = '0'*(32 - len(arg)) + arg
    A = arg[16:32]
    B = arg[10:16]
    C = arg[2:10]
    D = arg[1]
    E = arg[0]
    
    _string = B + E + A +  D + C 
 
    h = hex(int(_string, base=2))
    print('f('+str(hex(x))+') = '+h)
    return h

def main():
    f(0x152d9e53)
    f(0xbd606178)
    

if __name__ == '__main__':
    main()
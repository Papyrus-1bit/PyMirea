def f(arr:list):
    if arr[1]==1991:
        return 4
    elif arr[1]==2012:
        return 5
    elif arr[1]==2006:
        if arr[2]==1980:
            return 3
        elif arr[2]==1966:
            if arr[0]=='hack':
                return 0
            elif arr[0]=='tcsh':
                if arr[3]==1959:
                    return 2
                elif arr[3]==1997:
                    return 1

def main():
    print(f(['hack', 1991, 1980, 'less', 1959]))
    print(f(['hack', 2012, 1966, 'less', 1959]))

if __name__ == '__main__':
    main()
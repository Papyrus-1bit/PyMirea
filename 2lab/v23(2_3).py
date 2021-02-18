from array import *


array_1 = [[None,None,None,None],
    [0.09,"aleksandr10[at]gmail.com","13/08/04","(572) 522‐89‐52"],
    [None,None,None,None],
    [0.46,"tufozak87[at]gmail.com","28/04/99","(695) 737‐35‐82"],
    [0.86,"vugegij75[at]yandex.ru","09/07/03","(228) 441‐18‐45"],
    [0.48,"mazuk35[at]yahoo.com","24/06/04","(373) 063‐14‐08"]]

array_2 = [[0.64,"sazutij34[at]rambler.ru","13/06/03","(572) 522‐89‐52"],
    [None,None,None,None],
    [0.56,"anatolij66[at]mail.ru","18/09/99","(156) 098‐03‐86"],
    [None,None,None,None],
    [0.04,"safibanz50[at]yahoo.com","19/06/99","(945) 379‐01‐90"],
    [0.72,"dovifli87[at]yahoo.com","22/01/99","(980) 755‐77‐08"]]
                

def clear_empty_str(arr:list)->list:
    b = list()
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if(arr[i][j]!=None):
                b.append(arr[i])
            break
    arr = b.copy()
    b.clear()
    return arr


def transpose(arr:list)->list:
    b = [list(i) for i in zip(*arr)]
    arr = b.copy()
    b.clear()
    return arr


def reformat_list(arr:list)->list:
    a = clear_empty_str(arr)
    b :list = a.copy()
    s = list()
    for i in range(0,len(b)):
        s = b[i]
        s[0] = '{:.1f}'.format(s[0])
        s[1] = s[1].replace("[at]","@")
        s[2] = s[2].replace("/",".")
        b[i] = s
        s = list()
    arr = b.copy()
    b.clear()
    arr = transpose(arr)
    return arr


def out_format(arr:list):
    arr = reformat_list(arr)
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            print(arr[i])
            break
    print("\n")


def main():
    out_format(array_1)
    out_format(array_2)

if __name__ == '__main__':
    main()

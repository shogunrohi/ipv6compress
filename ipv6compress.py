v6list = []
def seperate(ipv6):
    deconstruct = ""
    for i in range(len(ipv6)):
        if ipv6[i] == ":" or (i == len(ipv6) - 1):
            if i == (len(ipv6) - 1):
                deconstruct += ipv6[i]
            v6list.append(deconstruct)
            deconstruct = ""
            continue
        else:
            deconstruct += ipv6[i]

def compress():
    temp = ""
    count = 0
    indexes = checker()
    for i in range(len(v6list)):
        if v6list[i][0] != "0":
            temp += v6list[i]
            temp += ":"
            continue
        elif (v6list[i] == "0000" and (v6list[i - 1] != "0000" and v6list[i + 1] != "0000")):
            temp += "0:"
            continue
        elif i in indexes:
            temp += "0:"
        elif v6list[i][0] == "0":
            con = False
            for j in v6list[i]:
                if j == "0" and con == False:
                    temp += ""
                else:
                    temp += j
                    con = True

            if temp[-1] == ":" and temp[-2] == ":":
                temp += ""
            elif i == 7 or (temp[-1] == ":" and count == 0):
                count += 1
                temp += ""
            else:
                temp += ":"
    if temp[-1] == ":":
        temp = temp[:len(temp) - 1]
    return temp
    
def checker():
    z = []
    ts = []
    code = ""
    for i in v6list:
        if i == "0000":
            code += "0"
        else:
            code += "1"
        
    for i in range(len(code)):
        if code[i] == "0":
            ts += [i]
        elif i == 0:
            continue
        else:
            z.append(ts)
            ts = []
    
    if len(z) <= 1:
        return []
    else:
        if len(z[0]) > len(z[1]):
            return z[1]
        else:
            return z[0]

def main():
    choices = ['y','n']
    ipv6 = input("Enter an ipv6 address: ")
    seperate(ipv6)
    c_ipv6 = compress()
    print(f"Compressed version: {c_ipv6}")
    again = input("Want to compress another (y or n)? ")
    while again not in choices:
        again = input("Give a valid input (y or n)? ")
    if again == "y":
        v6list.clear()
        main()
    else:
        print("Bye!")

if __name__ == "__main__":
    main()


                
            

    



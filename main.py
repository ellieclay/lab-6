

def encode(s):
    result = ""
    for i in s:
        if int(i) < 6:
            result += str(int(i) + 3)
        else:
            result += str(abs((int(i)+3) - 10))
    return result



def main():
    running = True
    pw = "None"
    opw = ''
    while running:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        sel = input("Please enter an option: ")
        if sel == '1':
            opw = input("Please enter your password to encode: ")
            pw = encode(opw)

        elif sel == '2':
            if pw != 'None':
                print(f"The encoded password is {pw}, and the original password is {opw}")
        elif sel == '3':
            running = False


main()





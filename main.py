

def encode(s):
    result = ""
    for i in s:
        if int(i) < 6:
            result += str(int(i) + 3)
        else:
            result += str(abs((int(i)+3) - 10))
    return result

t = "12345555"

print(encode(t))
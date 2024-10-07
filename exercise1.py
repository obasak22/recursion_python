import math
def calculate(f, x):
    if "*" not in f and "(" not in f:
        if len(f) == 1:
            return x
        elif len(f) == 2:
            return -x
        elif f[-2] == "n" or ((len(f) > 4) and (f[-5] == "-")):
            x = math.sin(x)
            f = f[:-4] + "x"
            return calculate(f, x)
        elif f[-2] == "s":
            x = math.cos(x)
            f = f[:-4] + "x"
            return calculate(f, x)
        elif (f[-2] == "n") and (len(f) > 4) and (f[-5] == "-"):
            x = -math.sin(x)
            f = f[:-5] + "x"
            return calculate(f, x)
        else:
            x = -math.cos(x)
            f = f[:-5] + "x"
            return calculate(f, x)
    list1 = f.split("*")
    result = 1
    for i in range(len(list1)):
        f = list1[i].replace("(","")
        f = f.replace(")","")
        result *= calculate(f, x)
    return result
    pass

def derivative(f, x):
    if "*" not in f and "(" not in f:
        if len(f) == 1:
            return "x"
        elif len(f) == 4 and f[-2] == "n":
            return "cosx"
        elif len(f) == 5 and f[-2] == "n":
            return "-cosx"
        elif len(f) == 4 and f[-2] == "s":
            return "-sinx"
        elif len(f) == 5 and f[-2] == "s":
            return "sinx"
        elif f[0] == "s":
            return "cos" + f[3:] + "*" + derivative(f[3:], x)
        elif f[1] == "s":
            return "-cos" + f[4:] + "*" + derivative(f[4:], x)
        elif f[0] == "c":
            return "-sin" + f[3:] + "*" + derivative(f[3:], x)
        else:
            return "sin" + f[4:] + "*" + derivative(f[4:], x)
    list1 = f.split("*")
    list_normal = []
    list_derivative = []
    for i in range(len(list1)):
        f = list1[i].replace("(","")
        f = f.replace(")","")
        list_normal.append(f)
        list_derivative.append(derivative(f, x))
    if len(list_normal) == 1:
        return calculate(derivative(f, x), x)
    else:
        total_result = 0
        for i in range(len(list_normal)):
            result = calculate(list_derivative[i], x)
            for j in range(len(list_normal)):
                if i != j:
                    result *= calculate(list_normal[j], x)
            total_result += result
        return total_result
    pass

if __name__ == '__main__':
    # You can uncomment each line after implementing the corresponding function
    print(round(calculate('sin(cos(x))', 0.7), 3))  # 0.692
    print(round(calculate('sin(cos(x))*sin(cos(sin(x)))*cos(x)', 1.2), 3))  # 0.072
    print(round(derivative('sin(cos(x))', 0.7), 3))  # -0.465
    print(round(derivative('sin(cos(x))*sin(cos(sin(x)))*cos(x)', 1.2), 3))  # -0.394
    pass
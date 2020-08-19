def complex_math(num, op, num1):
    while True:
        try:
            if op == "+":
                result = int(num + num1)
                break
            elif op == "-":
                result = int(num - num1)
                break
            elif op == "*" or op == "x":
                result = int(num * num1)
                break
            elif op == "/" or op == ":":
                result = num // num1
                break
            else:
                Invalid = "invalid operator, please try again."
                return Invalid
                break
        except ZeroDivisionError:
            Invalid = "Tried to divide by ZERO."
            return Invalid
            break
        except TypeError:
            Invalid = "Invalid type."
            return Invalid
            break

    return result

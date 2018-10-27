#!/usr/bin/env python3
import operator

op = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.floordiv,
}

def calculate(arg):
    # stack for calculator
    stack = []

    # tokenize input
    tokens = arg.split()

    # process tokens
    for token in tokens:
        if token in op:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = op[token](arg1, arg2)
                stack.append(result)
        else:
                stack.append(int(token))

        # try:
        #         value = int(token)
        #         stack.append(value)
        # except ValueError:
        #         val2 = int(stack.pop())
        #         val1 = int(stack.pop())

        #         # Look up function in table
        #         func = op[token]
        #         result = func(val1, val2)

                # stack.append(str(result))

    return stack.pop() 
        

def main():     
    while True:
        result = calculate(input('rpn calc> '))
        print(result)

if __name__ == '__main__':
    main()
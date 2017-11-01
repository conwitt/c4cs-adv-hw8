#!/usr/bin/env python3
"""
Reverse polish notation calculator
c4cs-f17-rpn
"""
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    """
    Calculate expression described in `myarg`
    """
    stack = []
    tokenized = myarg.split()
    for token in tokenized:
        try:
            stack.append(int(token))
        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            function = ops[token]
            result = function(arg1, arg2)
            stack.append(result)
    print(stack)
    return stack.pop()

def main():
    """
    Main execution loop
    """
    while True:
        calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()

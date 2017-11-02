#!/usr/bin/env python3
"""
Reverse polish notation calculator
c4cs-f17-rpn
"""
import operator
import readline
from termcolor import colored

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def colorize(token):
    """
    Color operators yellow, positive nums blue, and negative nums red.
    """
    if token in OPS:
        return colored(token, 'yellow')
    elif isinstance(token, (int, float)):
        if token >= 0:
            return colored(token, 'blue')
        return colored(token, 'red')
    return colored(token, 'green')

def cast_whole_float(num):
    """
    Casts a float to an int if whole number
    """
    if isinstance(num, float):
        return int(num) if num.is_integer() else num
    return num

class Calculator(object):
    """
    Reverse polish notation calculator
    """
    def __init__(self):
        self.stack = []
        self.log_stack = []
        self.last_result = 0

    def calculate(self, in_calc):
        """
        Calculate expression described in `in_calc`
        """
        tokenized = in_calc.split()
        for token in tokenized:
            try:
                self.stack.append(int(token))
            except ValueError:
                if token in OPS and len(self.stack) >= 2:
                    arg2 = self.stack.pop()
                    arg1 = self.stack.pop()
                    function = OPS[token]
                    result = cast_whole_float(function(arg1, arg2))
                    self.stack.append(result)
                    self.last_result = result

                    self.log_stack.append([
                        colorize(token) for token in [arg1, arg2, token, result]
                    ])
                    print(colorize(self.last_result))
                else:
                    self.print_log()

        return self.last_result

    def print_log(self):
        """
        prints the log stack
        """
        for equation in self.log_stack:
            print(' '.join(equation))

def main():
    """
    Main execution loop
    """
    calc = Calculator()
    while True:
        calc.calculate(input('rpn calc> '))

if __name__ == '__main__':
    main()

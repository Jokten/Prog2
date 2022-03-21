import io
import math
from tokenize import TokenError
from tokenizer import TokenizeWrapper


class CalculatorException(Exception):
    def __init__(self, arg):
        self.arg = arg


def assignment(wtok, var):
    result = expression(wtok, var)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            var[wtok.get_current()] = result
    return result


def expression(wtok, var):
    result = term(wtok, var)

    while wtok.get_current() in ['+', '-']:
        b = True
        while wtok.get_current() in ['+', '-']:
            if wtok.get_current() == '-':
                b = not b
            wtok.next()
        if b:
            result = result + term(wtok, var)
        else:
            result = result - term(wtok, var)

    return result


def term(wtok, var):
    result = factor(wtok, var)
    while wtok.get_current() in ['*', '/']:
        a = wtok.get_current()
        wtok.next()  # bypass *
        if a == '/':
            result = result / factor(wtok, var)
        else:
            result = result * factor(wtok, var)
    return result


def factor(wtok, var):
    if wtok.get_current() == '(':
        wtok.next()  # bypass (
        result = assignment(wtok, var)
        wtok.next()  # bypass )
    elif wtok.is_number():  # should be a number
        result = float(wtok.get_current())
        wtok.next()  # bypass the number
    elif wtok.get_current() in var.keys():
        result = var[wtok.get_current()]
        wtok.next()
    elif wtok.get_current() in ['sin', 'cos', 'exp', 'log']:
        cur = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            wtok.next()  # bypass (
            x = assignment(wtok, var)
            wtok.next()
        else:
            raise CalculatorException(
                f"Expected a parentheses but got'{wtok.get_current()}'")
        if cur == 'sin':
            result = math.sin(x)
        elif cur == 'cos':
            result = math.cos(x)
        elif cur == 'exp':
            result = math.exp(x)
        elif cur == 'log':
            result = math.log(x)
    else:
        raise CalculatorException(
            f"Expected a left parentheses/number/variable or function but found '{wtok.get_current()}'")
    return result


def statement(wtok, var):
    if wtok.get_current() == 'quit':
        print('Bye!')
        print(var)
        exit()
    elif wtok.get_current() == 'vars':
        for e in var.items():
            print(e[0], '=', e[1])
    else:
        return assignment(wtok, var)


def main():
    print("Very simple calculator")
    var = {}
    while True:
        line = input('> ')
        try:
            wtok = TokenizeWrapper(line)
            result = statement(wtok, var)
            if result is not None:
                print('Result: ', result)
        except TokenError:
            print('*** Error. Unbalanced parentheses')
        except CalculatorException as e:
            print(e)


if __name__ == "__main__":
    main()

"""
Solutions to module 2 - A calculator
Student: Jonathan Berntsson
Mail: Jokten123@gmail.com
Reviewed by: Simon
Reviewed date: 25/4 -22
""" 

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper

def fib(n):
    if not n.is_integer() or n <= 0:
        raise EvaluationError(f"fib only takes positive intergers and got ({n})")
    else:
        n = int(n)
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    old = 1
    new = 1
    for i in range(n-2):
        updated = new + old
        old = new
        new = updated
    return new

def mean(x):
    return sum(x)/len(x)

function_1 = {'sin':math.sin, 'cos': math.cos, 'exp':math.exp, 'log':math.log, 'fib':fib, 'fac':math.factorial}
function_n = {'max': max, 'min':min, 'sum':sum, 'mean':mean}
class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)



def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            cur = wtok.get_current()
            wtok.next()
            if wtok.get_current() not in ['',')','=']:
                raise SyntaxError(f'Invalid Expression')
            variables[cur] = result
        else:
            raise SyntaxError(f"Expected name")
    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    if wtok.get_current() in ['-']:
        result = 0
    else:
        result = term(wtok, variables)
    while wtok.get_current() in ['+', '-']:
        b = True
        while wtok.get_current() in ['+', '-']:
            if wtok.get_current() == '-':
                b = not b
            wtok.next()
        if b:
            result = result + term(wtok, variables)
        else:
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while wtok.get_current() in ['*', '/']:
        a = wtok.get_current()
        wtok.next()  # bypass *
        if a == '/':
            try:
                result = result / factor(wtok, variables)
            except ZeroDivisionError:
                raise EvaluationError(f'Division by zero not allowed')
        else:
            result = result * factor(wtok, variables)
    return result

def arglist(wtok, variables):
    result = []

    if wtok.get_current() != '(':
        raise SyntaxError("Expected '('")
    else:
        wtok.next()
        result.append(assignment(wtok,variables))
        while wtok.get_current() == ',':
            wtok.next()
            result.append(assignment(wtok,variables))
        if wtok.get_current() != ')':
            raise SyntaxError(f"Expected ')' or ',' but got {wtok.get_current()}")
        else:
            return result

        
def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
    
    elif wtok.get_current() in function_1.keys():
        func = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            wtok.next()  # bypass (
            x = assignment(wtok, variables)
            wtok.next()
        else:
            raise SyntaxError(
                f"Expected a parentheses but got'{wtok.get_current()}'")
        if func == 'log' and x <= 0:
            raise EvaluationError(f"log can't take negative input numbers")
        if func == 'fac' and (x <= 0 or not x.is_integer()):
            raise EvaluationError(
                 f"fac only takes positive intergers and got {x}")
        else:
            return function_1[func](x)                

    elif wtok.get_current() in function_n.keys():
        cur = wtok.get_current()
        wtok.next()
        args = arglist(wtok, variables)
        return function_n[cur](args)
    
    elif wtok.is_name():
        if wtok.get_current() in variables.keys():
            result = variables[wtok.get_current()]
            wtok.next()
        else:
            raise EvaluationError(f'Variable not defined')

    else:
        raise SyntaxError(
            "Expected expression or function")  
    
    return result


         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    
    init_file = '2\MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        print('Ingen fil hittades')

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            for i in variables.items():
                print(f'{i[0]: <16}:{i[1]}')
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
            
            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")
 


if __name__ == "__main__":
    main()

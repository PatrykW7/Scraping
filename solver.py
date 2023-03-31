from sympy import *
import re

class Solver():
    def __init__(self):
        pass
    
    def solve_eq(self, equation):
        x = Symbol('x')
        y = Function('y')(x)
        left_expr = equation[:equation.rfind('=')]
        right_expr = equation[equation.rfind('=')+1:]
        parsed_left = parse_expr(left_expr,local_dict=locals())
        parsed_right = parse_expr(right_expr, local_dict = locals())
        self.diffeq = Eq(parsed_left, parsed_right)
        self.eq_solution = dsolve(self.diffeq, y, ics = self.ics)
    
    # test warunku poczatkowego
    def parse_ics(self, init_condition):
        int_ics = re.findall('[-]?\d+', init_condition)
        self.ics_arg = int_ics[0]
        self.ics_value = int_ics[1]
        print(int_ics)

    def set_init_condition(self):
        x = Symbol('x')
        y = Function('y')(x)
        self.ics = {y.subs(x, self.ics_arg) : self.ics_value}

    def eq_to_png(self):
        preview(self.diffeq, viewer='file', filename='equation.png', dvioptions=['-D','180','-bg','Transparent'] )
        preview(self.eq_solution, viewer='file', filename='solution.png', dvioptions=['-D','180','-bg','Transparent'])

        


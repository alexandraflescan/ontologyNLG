import ast
import random
import inflect
from ontologyGeneration import *
from patternManagement import *
from postProcessor import PostProcessor

from problemGeneration import Problem




class WalkThisWay(ast.NodeVisitor):
    def __init__(self):
        self.prop = ''
        self.domain_range = get_domain_range()
        self.problem = Problem()
        self.grm_agreement_engine = inflect.engine()
        print(self.domain_range)
        self.establish_operation = 'add'

    def recursive(func):
        def wrapper(self, node):
            if isinstance(node, ast.BinOp):
                self.visit(node.left)
                self.visit(node.right)
                func(self, node)

                # else:
                #     func(self, node)

        return wrapper

    @recursive
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            self.establish_operation = 'add'
            if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
                self.two_addition(node)
            elif (isinstance(node.left, ast.Num) and isinstance(node.right, ast.BinOp)) or (
                        (isinstance(node.left, ast.BinOp)) and isinstance(node.right, ast.Num)):
                self.one_addition(node)

        elif isinstance(node.op, ast.Sub):
            self.establish_operation = 'sub'
            if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
                self.two_subtraction(node)
            elif (isinstance(node.left, ast.Num) and isinstance(node.right, ast.BinOp)) or (
                        (isinstance(node.left, ast.BinOp)) and isinstance(node.right, ast.Num)):
                self.one_subtraction(node)

        elif isinstance(node.op, ast.Mult):
            self.establish_operation = 'add'
            if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
                self.two_multiplication(node)
            elif (isinstance(node.left, ast.Num) and isinstance(node.right, ast.BinOp)) or (
                        (isinstance(node.left, ast.BinOp)) and isinstance(node.right, ast.Num)):
                self.one_multiplication(node)

        elif isinstance(node.op, ast.Div):
            self.establish_operation = 'sub'
            if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
                self.two_division(node)
            elif (isinstance(node.left, ast.Num) and isinstance(node.right, ast.BinOp)) or (
                        (isinstance(node.left, ast.BinOp)) and isinstance(node.right, ast.Num)):
                self.one_multiplication(node)


    def two_addition(self, node):
        pattern = PatternManagement.get_pattern_addition_two()
        ed_pattern_add = {}
        ed_pattern_add['nr1'] = node.left.n
        ed_pattern_add['nr2'] = node.right.n
        if pattern.number_properties == 1:
            ed_pattern_add['property'] = self.domain_range['property']
        for i in range(1, pattern.number_ranges + 1):
            ed_pattern_add['range' + str(i)] = self.get_grm_agreement(self.domain_range['range'][i - 1], ed_pattern_add['nr' + str(i)])
        for i in range(1, pattern.number_domains + 1):
            ed_pattern_add['domain' + str(i)] = self.domain_range['domain'][i - 1]
        ed_pattern_add['nr1'] = self.grm_agreement_engine.number_to_words(ed_pattern_add['nr1'])
        ed_pattern_add['nr2'] = self.grm_agreement_engine.number_to_words(ed_pattern_add['nr2'])
        self.problem.text += pattern.text.format(**ed_pattern_add)


    def one_addition(self, node):
        pattern = PatternManagement.get_pattern_addition_one()
        ed_pattern_add = {}
        if isinstance(node.left, ast.Num):
            ed_pattern_add['nr1'] = node.left.n
        else:
            ed_pattern_add['nr1'] = node.right.n
        if pattern.number_properties == 1:
            ed_pattern_add['property'] = self.domain_range['property']
        for i in range(1, pattern.number_ranges + 1):
            ed_pattern_add['range' + str(i)] = self.get_grm_agreement(self.domain_range['range'][i - 1],  ed_pattern_add['nr' + str(i)])
        for i in range(1, pattern.number_domains + 1):
            ed_pattern_add['domain' + str(i)] = self.domain_range['domain'][i - 1]

        ed_pattern_add['nr1'] = self.grm_agreement_engine.number_to_words(ed_pattern_add['nr1'])
        self.problem.text += pattern.text.format(**ed_pattern_add)

    def two_subtraction(self, node):
        pattern = PatternManagement.get_pattern_subtraction_two()
        ed_pattern_subtract = {}


        if pattern.number_properties == 1:
            ed_pattern_subtract['property'] = self.domain_range['property']
        ed_pattern_subtract['nr1'] = node.left.n
        ed_pattern_subtract['nr2'] = node.right.n

        for i in range(1, pattern.number_ranges + 1):
            ed_pattern_subtract['range' + str(i)] = self.get_grm_agreement(self.domain_range['range'][i - 1], ed_pattern_subtract['nr' + str(i)])
        for i in range(1, pattern.number_domains + 1):
            ed_pattern_subtract['domain' + str(i)] = self.domain_range['domain'][i - 1]

        ed_pattern_subtract['nr1'] = self.grm_agreement_engine.number_to_words(ed_pattern_subtract['nr1'])
        ed_pattern_subtract['nr2'] = self.grm_agreement_engine.number_to_words(ed_pattern_subtract['nr2'])
        self.problem.text += pattern.text.format(**ed_pattern_subtract)

    def one_subtraction(self, node):
        pattern = PatternManagement.get_pattern_subtraction_one()
        ed_pattern_subtract = {}
        if pattern.number_properties == 1:
            ed_pattern_subtract['property'] = self.domain_range['property']
        for i in range(1, pattern.number_ranges + 1):
            ed_pattern_subtract['range' + str(i)] = self.get_grm_agreement(self.domain_range['range'][i - 1], ed_pattern_subtract['nr' + str(i)])
        for i in range(1, pattern.number_domains + 1):
            ed_pattern_subtract['domain' + str(i)] = self.domain_range['domain'][i - 1]
        if isinstance(node.left, ast.Num):
            ed_pattern_subtract['nr1'] = node.left.n
        else:
            ed_pattern_subtract['nr1'] = node.right.n

        ed_pattern_subtract['nr1'] = self.grm_agreement_engine.number_to_words(ed_pattern_subtract['nr1'])
        self.problem.text += pattern.text.format(**ed_pattern_subtract)

    def two_multiplication(self, node):
        pattern = PatternManagement.get_pattern_multiplication_two()
        ed_pattern_multiply = {}
        ed_pattern_multiply['nr1'] = node.left.n
        ed_pattern_multiply['nr2'] = node.right.n
        if pattern.number_properties == 1:
            ed_pattern_multiply['property'] = self.domain_range['property']
        for i in range(1, pattern.number_ranges + 1):
            ed_pattern_multiply['range' + str(i)] = self.get_grm_agreement(self.domain_range['range'][i - 1], ed_pattern_multiply['nr' + str(i)])

        for i in range(1, pattern.number_domains + 1):
            ed_pattern_multiply['domain' + str(i)] = self.domain_range['domain'][i - 1]
        ed_pattern_multiply['nr1'] = self.grm_agreement_engine.number_to_words(ed_pattern_multiply['nr1'])
        ed_pattern_multiply['nr2'] = self.grm_agreement_engine.number_to_words(ed_pattern_multiply['nr2'])
        self.problem.text += pattern.text.format(**ed_pattern_multiply)

    def one_multiplication(self, node):
        pattern = PatternManagement.get_pattern_multiplication_one()
        ed_pattern_multiply = {}
        if pattern.number_properties == 1:
            ed_pattern_multiply['property'] = self.domain_range['property']
        for i in range(1, pattern.number_ranges + 1):
            ed_pattern_multiply['range' + str(i)] = self.get_grm_agreement(self.domain_range['range'][i - 1], ed_pattern_multiply['nr' + str(i)])
        for i in range(1, pattern.number_domains + 1):
            ed_pattern_multiply['domain' + str(i)] = self.domain_range['domain'][i - 1]
        if isinstance(node.left, ast.Num):
            ed_pattern_multiply['nr1'] = node.left.n
        else:
            ed_pattern_multiply['nr1'] = node.right.n

        ed_pattern_multiply['nr1'] = self.grm_agreement_engine.number_to_words(ed_pattern_multiply['nr1'])
        self.problem.text += pattern.text.format(**ed_pattern_multiply)

    def two_division(self, node):
        pattern = PatternManagement.get_pattern_division_two()
        ed_pattern_divide = {}
        ed_pattern_divide['nr1'] = node.left.n
        ed_pattern_divide['nr2'] = node.right.n
        if pattern.number_properties == 1:
            ed_pattern_divide['property'] = self.domain_range['property']
        for i in range(1, pattern.number_ranges + 1):
            ed_pattern_divide['range' + str(i)] = self.get_grm_agreement(self.domain_range['range'][i - 1], ed_pattern_divide['nr' + str(i)])
        for i in range(1, pattern.number_domains + 1):
            ed_pattern_divide['domain' + str(i)] = self.domain_range['domain'][i - 1]
        ed_pattern_divide['nr1'] = self.grm_agreement_engine.number_to_words(ed_pattern_divide['nr1'])
        ed_pattern_divide['nr2'] = self.grm_agreement_engine.number_to_words(ed_pattern_divide['nr2'])
        self.problem.text += pattern.text.format(**ed_pattern_divide)

    def one_division(self, node):
        pattern = PatternManagement.get_pattern_division_one()
        ed_pattern_divide = {}
        if pattern.number_properties == 1:
            ed_pattern_divide['property'] = self.domain_range['property']
        for i in range(1, pattern.number_ranges + 1):
            ed_pattern_divide['range' + str(i)] = self.get_grm_agreement(self.domain_range['range'][i - 1], ed_pattern_divide['nr' + str(i)])
        for i in range(1, pattern.number_domains + 1):
            ed_pattern_divide['domain' + str(i)] = self.domain_range['domain'][i - 1]
        if isinstance(node.left, ast.Num):
            ed_pattern_divide['nr1'] = node.left.n
        else:
            ed_pattern_divide['nr1'] = node.right.n

        ed_pattern_divide['nr1'] = self.grm_agreement_engine.number_to_words(ed_pattern_divide['nr1'])
        self.problem.text += pattern.text.format(**ed_pattern_divide)

    def get_grm_agreement(self, text, count):
        words = text.split()
        words[-1] = self.grm_agreement_engine.plural(words[-1], count)
        return " ".join(words)


def get_problem_text(problemString):

    mathExpression = ast.parse(problemString, " ", "eval")
    test = ast.dump(mathExpression)
    global objective_text
    tree = WalkThisWay()
    tree.visit(mathExpression)
    if tree.establish_operation == 'add':
        objective_text = PatternManagement.get_obj_pattern_addition()
    else:
        objective_text = PatternManagement.get_obj_pattern_subtraction()
    if objective_text.number_generic == 1:
        generic_variable = tree.domain_range['generic']
        generic_variable = tree.get_grm_agreement(generic_variable, 2)
        objective_text.text = objective_text.text.format(generic=generic_variable)
    tree.problem.text += objective_text.text
    processor = PostProcessor(tree.problem.text)
    processor.capitalise_words()
    with open("samples.txt", "a") as text_file:
        print(processor.text)
        text_file.write(processor.text + "\n")
    return processor.text


 # print(processor.text)
get_problem_text('55/5*5')
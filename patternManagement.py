from patterns import Pattern
import random

class PatternManagement:
    @staticmethod
    def get_pattern_addition_two():
        patterns = [
            Pattern('{domain1} {property} {nr1} {range1} and {nr2} {range2}.', 2, 1, 1),
            Pattern('if {nr1} {range1} are added to {nr2} {range2}', 1, 0, 0)

        ]
        return random.choice(patterns)

    @staticmethod
    def get_pattern_addition_one():

        patterns = [
            Pattern(' {nr1} of them are added. ', 0, 0, 0),
            Pattern('to those {range1}, we add {nr1} more', 1, 0, 0)
        ]
        return random.choice(patterns)

    @staticmethod
    def get_pattern_subtraction_two():

        patterns = [
            Pattern('There is {domain1} that {property} {nr1} {range1}, but {nr2} of them disappear.', 1, 1,  1),
            Pattern( 'From {nr1} {range1} someone decides to remove {nr2}.', 1, 0, 0)
        ]
        return random.choice(patterns)


    @staticmethod
    def get_pattern_subtraction_one():
        patterns = [
            Pattern(' and from that amount {nr1} is removed from the total'),
            Pattern(' somehow, {nr1} dissapear')
        ]
        return random.choice(patterns)

    @staticmethod
    def get_pattern_multiplication_two():
        patterns = [
            Pattern('There is {domain1} that {property} {nr1} {range1}. If we add {nr2} times the same quantity to {domain1}', 1, 1, 1, 0),
            Pattern( 'Being given {nr1} {range1}, someone decides to multiply this by {nr1}', 1, 0, 0, 0)
        ]
        return random.choice(patterns)

    @staticmethod
    def get_pattern_multiplication_one():
        patterns = [
            Pattern(' after, we multiply all by {nr1}'),
            Pattern('if we add {nr1} times the same amount')
        ]
        return random.choice(patterns)

    @staticmethod
    def get_pattern_division_two():
        patterns = [
            Pattern('There is {domain1} that {property} {nr1} {range1}. {range1} is divided by {nr2}.', 1, 1, 1, 0),
            Pattern('We have {nr1} {range1}, but we are told that we have to divide all by {nr2}', 1, 0, 0, 0)
        ]
        return random.choice(patterns)


    @staticmethod
    def get_pattern_division_one():
        patterns = [
            Pattern(' and at the end, it is decided to share all to {nr1} friends'),
            Pattern( 'finally, we need to divide all this by {nr1}')
        ]
        return random.choice(patterns)


    @staticmethod
    def get_obj_pattern_addition():
        patterns = [
            Pattern(' what is the total now?'),
            Pattern(' how many do we have now?')
        ]
        return random.choice(patterns)

    @staticmethod
    def get_obj_pattern_subtraction():
        patterns = [
        Pattern(' how many {generic} are left?', number_generic=1),
        Pattern(' this being given, what is the left number?')
        ]
        return random.choice(patterns)










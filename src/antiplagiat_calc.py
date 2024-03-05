import re

from AntiPlagiat.src.antiplagiat_utils import AntiPlagiat
from .ast_utils import ASTUtils


class AntiPlagiatCalc:
    def __init__(self):
        self.ap = AntiPlagiat()
        self.astu = ASTUtils()

    def calc_jaccard(self, code_one, code_two) -> float:
        code_one = code_one.split("\n")
        code_two = code_two.split("\n")
        code_one = [line.strip() for line in code_one if line]
        code_two = [line.strip() for line in code_two if line]
        metric = self.ap.find_jaccard_similarity(code_one, code_two)
        return metric

    def calc_ast(self, code_one, code_two):
        metric = self.astu.run_ast(code_one, code_two)
        return metric

    def calc_levenshtein(self, code_one, code_two) -> float:
        lev = self.ap.find_levenshtein(code_one, code_two)
        return lev

    def calc_hash(self, code_one, code_two) -> bool:
        pattern = "^[ ]{0,}#[\w|\W]{0,}\n$"
        code_one = re.sub(pattern, "", code_one)
        code_two = re.sub(pattern, "", code_two)
        if self.ap.find_hash(code_one, code_two):
            return True
        return False


def check_plagiat(code_one, code_two, state = None) -> float:
    apc = AntiPlagiatCalc()
    hashed_check = apc.calc_hash(code_one, code_two)

    if hashed_check:
        return 100.0

    if state == 'jaccard':
        jaccard_check = apc.calc_jaccard(code_one, code_two)
        return jaccard_check
    elif state == 'levenshtein':
        levenshtein_check = apc.calc_levenshtein(code_one, code_two)
        return levenshtein_check
    elif state == 'ast':
        ast_metric = apc.calc_ast(code_one, code_two)
        return ast_metric
    else:
        raise ValueError("Wrong method! Use either jaccard, levenshtein or ast")

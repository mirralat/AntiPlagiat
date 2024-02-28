import re

from AntiPlagiat.src.antiplagiat_utils import AntiPlagiat


class AntiPlagiatCalc:
    def __init__(self):
        self.jaccard = 0
        self.ast = 0
        self.sorenson = 0
        self.levenshtein = 0

    def _calc_jaccard(self, code_one, code_two):
        code_one = code_one.split("\n")
        code_two = code_two.split("\n")
        code_one = [line.strip() for line in code_one if line]
        code_two = [line.strip() for line in code_two if line]

        ap = AntiPlagiat()

        metric = ap.find_jaccard_similarity(code_one, code_two)
        self.jaccard = metric

        return metric

    def _calc_sorenson(self, code_one, code_two):
        metric = 0.2
        self.metric = 0.2
        return metric

    def _calc_ast(self):
        pass

    def _calc_levenshtein(self, code_one, code_two):
        ap = AntiPlagiat()
        lev = ap.find_levenshtein(code_one, code_two)
        # берем результат левенштейна, делим на количество символов в младшем коде, умножаем на 100%

        minimum = len(code_one) if len(code_one) < len(code_two) else len(code_two)

        no_match = (lev / minimum) * 100
        matched = 100 - no_match
        return matched


    def _calc_hash(self, code_one, code_two):
        pattern = "^[ ]{0,}#[\w|\W]{0,}\n$"
        code_one = re.sub(pattern, "", code_one)
        code_two = re.sub(pattern, "", code_two)
        ap = AntiPlagiat()
        if ap.find_hash(code_one, code_two):
            return True
        return False

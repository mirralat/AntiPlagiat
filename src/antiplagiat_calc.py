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

        ap = AntiPlagiat(code_one, code_two)

        metric = ap.calc_jaccard_similarity()
        self.jaccard = metric

        return metric

    def _calc_sorenson(self, code_one, code_two):
        metric = 0.2
        self.metric = 0.2
        return metric

    def _calc_ast(self):
        pass

    def _calc_levenshtein(self):
        pass


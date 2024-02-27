class AntiPlagiat:
    def __init__(self, file_one, file_two):
        self.file_one = file_one
        self.file_two = file_two

    def calc_jaccard_similarity(self):
        set_one = set(self.file_one)
        set_two = set(self.file_two)

        intersection = len(set_one.intersection(set_two))
        union = len(set_one.union(set_one))

        return intersection / union

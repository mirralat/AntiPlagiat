import hashlib
import re

import Levenshtein
from Levenshtein import distance as lev
from rapidfuzz import fuzz


class AntiPlagiat:
    def __init__(self):
        pass

    def find_jaccard_similarity(self, file_one, file_two):
        set_one = set(file_one)
        set_two = set(file_two)

        intersection = len(set_one.intersection(set_two))
        union = len(set_one.union(set_one))

        return intersection / union

    def find_levenshtein(self, file_one, file_two):
        return fuzz.partial_ratio(file_one, file_two)

    def find_hash(self, file_one, file_two):
        if hashlib.sha512(file_one) == hashlib.sha512(file_two):
            return True
        return False

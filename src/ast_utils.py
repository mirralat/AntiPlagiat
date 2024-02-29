import ast

from _ast import *
from munkres import Munkres


class ASTUtils:
    def compare_ASTs(self, ast_a: AST, ast_b: AST, reorder_depth: int) -> int:

        children_a = list(ast.iter_child_nodes(ast_a))
        children_b = list(ast.iter_child_nodes(ast_b))

        if (
                (type(ast_a) == type(ast_b))
                and len(list(children_a)) == 0
                and len(list(children_b)) == 0
        ):
            return 1

        if (type(ast_a) != type(ast_b)) or (len(children_a) != len(children_b)):
            return 0

        if reorder_depth == 0:
            match_index = sum(
                map(
                    lambda pairs: self.compare_ASTs(pairs[0], pairs[1], reorder_depth),
                    zip(children_a, children_b),
                )
            )
            return match_index + 1

        elif reorder_depth > 0:
            match_index = self.reorder_children_compare(ast_a, ast_b, reorder_depth - 1)
            return match_index + 1

        return 0

    def reorder_children_compare(self, ast_a: AST, ast_b: AST, reorder_depth: int) -> int:
        comparison_matrix = []
        cost_matrix = []
        best_match_value = 0
        children_a = list(ast.iter_child_nodes(ast_a))
        children_b = list(ast.iter_child_nodes(ast_b))

        if len(children_a) <= 1 or len(children_b) <= 1:
            for child_a in children_a:
                for child_b in children_b:
                    best_match_value += self.compare_ASTs(child_a, child_b, reorder_depth)
        else:
            for child_a in children_a:
                row = []
                cost_row = []
                for child_b in children_b:
                    similarity = self.compare_ASTs(child_a, child_b, reorder_depth)
                    row.append(similarity)

                    cost_row.append(10000000 - similarity)

                comparison_matrix.append(row)
                cost_matrix.append(cost_row)

            m = Munkres()
            indices = m.compute(cost_matrix)

            for row, col in indices:
                best_match_value += comparison_matrix[row][col]

        return best_match_value

    def compare_subtrees(self, sig_subtrees_p1: list, sig_subtrees_p2: list, reorder_depth: int) -> tuple:

        comparison_matrix = []
        cost_matrix = []
        best_match = []
        best_match_value = 0
        best_match_weight = 0
        children_a = sig_subtrees_p1.copy()
        children_b = sig_subtrees_p2.copy()

        if len(children_a) <= 1 or len(children_b) <= 1:
            for child_a in children_a:
                best_match += [child_a]
                for child_b in children_b:
                    print('add')
                    best_match_value += self.compare_ASTs(child_a, child_b, reorder_depth)
                    best_match += [child_b]
        else:
            for child_a in children_a:
                row = []
                cost_row = []
                for child_b in children_b:
                    similarity = self.compare_ASTs(child_a, child_b, reorder_depth)
                    row.append(similarity)
                    cost_row.append(10000000 - similarity)

                comparison_matrix.append(row)
                cost_matrix.append(cost_row)

            m = Munkres()
            indices = m.compute(cost_matrix)

            for row, col in indices:
                best_match_weight += self.apply_weights_to_subtrees_mult(
                    comparison_matrix[row][col], sig_subtrees_p1[row], sig_subtrees_p2[col]
                )
                best_match += [sig_subtrees_p1[row], sig_subtrees_p2[col]]

        all_subtrees_weight = sum(
            map(
                lambda tree: self.apply_weights_to_subtrees(self.get_num_nodes(tree), tree),
                sig_subtrees_p1,
            )
        ) + sum(
            map(
                lambda tree: self.apply_weights_to_subtrees(self.get_num_nodes(tree), tree),
                sig_subtrees_p2,
            )
        )

        similarity = 2 * best_match_weight / all_subtrees_weight

        return round(similarity, 4), best_match

    def get_significant_subtrees(self, root: AST) -> list:

        significant_subtrees = []
        for node in ast.walk(root):
            if self.is_significant(node):
                significant_subtrees.append(node)
        return significant_subtrees

    def is_significant(self, root: AST) -> bool:

        return (
                isinstance(root, Import)
                or isinstance(root, FunctionDef)
                or isinstance(root, If)
                or isinstance(root, ClassDef)
                or isinstance(root, While)
                or isinstance(root, For)
                or isinstance(root, comprehension)
                or isinstance(root, Return)
        )

    def get_num_nodes(self, root: AST) -> int:

        return len(list(ast.walk(root)))

    def apply_weights_to_subtrees(self, weight: float, subtree: AST) -> float:

        new_weight = weight
        if isinstance(subtree, Import):
            new_weight *= 0.3
        elif isinstance(subtree, Module):
            new_weight *= 1
        elif isinstance(subtree, FunctionDef):
            new_weight *= 1.2
        elif isinstance(subtree, If):
            new_weight *= 0.5
        elif isinstance(subtree, ClassDef):
            new_weight *= 1
        elif isinstance(subtree, While):
            new_weight *= 1
        elif isinstance(subtree, For):
            new_weight *= 1
        elif isinstance(subtree, comprehension):
            new_weight *= 1
        elif isinstance(subtree, Return):
            new_weight *= 1
        return new_weight

    def apply_weights_to_subtrees_mult(self, weight: float, ast_1: AST, ast_2: AST) -> float:

        if weight == 0:
            return 0
        else:
            return (
                    self.apply_weights_to_subtrees(weight, ast_1)
                    + self.apply_weights_to_subtrees(weight, ast_2)
            ) / 2

    def _compare_many(self, programs: list) -> list:

        tree_list = list(
            map(lambda prog: self.get_significant_subtrees(ast.parse(prog)), programs)
        )

        matrix = []
        for program_1_tree_num in range(0, len(tree_list)):
            for program_2_tree_num in range(program_1_tree_num, len(tree_list)):
                if program_1_tree_num == program_2_tree_num:
                    continue
                print(f"comparing {program_1_tree_num} to {program_2_tree_num}")

                subtrees1 = tree_list[program_1_tree_num]
                subtrees2 = tree_list[program_2_tree_num]

                result = self.compare_subtrees(subtrees1, subtrees2, 1000)[0]

                matrix.append((program_1_tree_num, program_2_tree_num, result))
                matrix.append((program_2_tree_num, program_1_tree_num, result))

        return matrix

    def run_ast(self, code_one, code_two) -> float:
        subtree_list1 = self.get_significant_subtrees(code_one)
        subtree_list2 = self.get_significant_subtrees(code_two)
        similarity = self.compare_subtrees(subtree_list1, subtree_list2, 10000)
        return similarity[0]

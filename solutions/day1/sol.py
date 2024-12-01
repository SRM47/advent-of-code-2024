from ..base import SolutionBase


class Day1Solution(SolutionBase):
    def process_input(self):
        if hasattr(self, "_left") and hasattr(self, "_right"):
            return
        left = []
        right = []
        for line in self.file:
            left_loc, right_loc = line.split()
            left.append(int(left_loc))
            right.append(int(right_loc))
        self._left = left
        self._right = right

    @SolutionBase.solver
    def solve_1(self):
        self._left.sort()
        self._right.sort()
        return sum(abs(item1 - item2) for item1, item2 in zip(self._left, self._right))

    @SolutionBase.solver
    def solve_2(self):
        return None

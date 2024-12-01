from ..base import SolutionBase

class Day1Solution(SolutionBase):
    def solve_1(self):
        list1 = []
        list2 = []
        for line in self.file:
            left, right = line.split()
            list1.append(int(left))
            list2.append(int(right))
        list1.sort()
        list2.sort()
        return sum(abs(item1-item2) for item1, item2 in zip(list1, list2))

    def solve_2(self): return None



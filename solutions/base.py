import argparse
from abc import ABC, abstractmethod


class SolutionBase(ABC):
    """
    An abstract base class for solving problems.
    """

    def __init__(self, input_file: str):
        self.file = open(input_file, "r")

    def cleanup(self):
        self.file.close()

    def solver(func):
        """Decorator to process the file input"""

        def wrapper(self, *args, **kwargs):
            if self.file != None:
                self.process_input()
            return func(self, *args, **kwargs)

        return wrapper

    @abstractmethod
    def process_input(self): ...

    @abstractmethod
    def solve_1(self): ...

    @abstractmethod
    def solve_2(self): ...

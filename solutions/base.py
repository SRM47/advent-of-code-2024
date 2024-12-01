import argparse
from abc import ABC, abstractmethod

class SolutionBase(ABC):
    """
    An abstract base class for solving problems.
    """
    def __init__(self, input_file: str):
        self.file = open(input_file, 'r')   

    def validate(func):
        """
        Decorator to ensure the file is loaded and close it after execution.
        """
        def wrapper(self, *args, **kwargs):
            if self.file is None:
                raise ValueError("Input file is not loaded. Call get_input() first.")
            output = func(self, *args, **kwargs)
            self.file.close()
            return output
        return wrapper

    @abstractmethod
    def solve_1(self):...

    @abstractmethod
    def solve_2(self):...


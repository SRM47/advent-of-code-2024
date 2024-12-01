import argparse
import importlib
import os

BASE_DIR = "./solutions"
def solve(day: int, filename: str):
    solution_module_name = f"solutions.day{day}.sol"
    solution_class_name = f"Day{day}Solution"
    solution_file_name = filename or f"./solutions/day{day}/input"

    try:
        solution_module = importlib.import_module(solution_module_name)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            f"Couldn't find the module {solution_module_name} :/. Either the module isn't named by the conventioned used in this script or the solution for Day 2 hasn't been implemented yet."
        )
    solution_class = getattr(solution_module, solution_class_name)

    solver = solution_class(solution_file_name)
    print(f"~~Answer~~\nPart 1: {solver.solve_1()}\nPart 2: {solver.solve_2()}")
    solver.cleanup()

def generate(day: int):
    new_folder_dir = os.path.join(BASE_DIR, f"day{day}")
    try:
        os.makedirs(new_folder_dir, exist_ok=False)
    except OSError:
        print(f"A folder for Day {day} ({new_folder_dir}) already exists.")

    new_solution_file = os.path.join(new_folder_dir, "sol.py")

    if os.path.exists(new_solution_file):
        print(f"A solution file for Day {day} already exists!") 
        replace_option = input("Replace its contents [y/N]: ").lower()
        while replace_option != '' and replace_option != 'y' and replace_option != 'n':
            print("Invalid option, enter either y, n, or leave blank (for 'No').")
            replace_option = input("Replace its contents [y/N]: ").lower()
        if replace_option != 'y': return
        
    with open(new_solution_file, 'w') as f:
        f.write(f"""
from ..base import SolutionBase

class Day{day}Solution(SolutionBase):
    
    def process_input(self) -> None:
        # TODO: Implement this method process the input file, self.file.
        # This method is used to store instance variables to be accessed by both solve_1 and solve_2.
        
    @SolutionBase.solver
    def solve_1(self):
        # TODO: Solve part 1 of Day {day}'s problem, and return the answer directly
        return 47

    @SolutionBase.solver
    def solve_2(self):
        # TODO: Solve part 2 of Day {day}'s problem, and return the answer directly
        return "Chirp Chirp"
"""
        )

def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2024 by Sameer R. Malik :)")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    solve_subparser = subparsers.add_parser("solve", help="Solve the problem for a specific day")
    solve_subparser.add_argument(
        "day",
        type=int,
        choices=range(1, 31),
        help="Day number of the solution to solve (1-30)",
    )
    solve_subparser.add_argument("--input", type=str, required=False, help="Path to the input file")

    generate_subparser = subparsers.add_parser("generate", help="Generate the code for the problem for a specific day")
    generate_subparser.add_argument(
        "day",
        type=int,
        choices=range(1, 31),
        help="Day number of the solution to solve (1-30)",
    )

    args = parser.parse_args()

    if args.command == "solve":
        solve(args.day, args.input)
    elif args.command == "generate":
        generate(args.day)


if __name__ == "__main__":
    main()

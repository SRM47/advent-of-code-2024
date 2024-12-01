import argparse
import importlib


def main():
    parser = argparse.ArgumentParser(description="Solve the problem for the given day.")
    parser.add_argument(
        "day",
        type=int,
        choices=range(1, 31),
        help="Day number of the solution to solve (1-30)",
    )
    parser.add_argument("--input", type=str, help="Path to the input file")
    args = parser.parse_args()

    solution_module_name = f"solutions.day{args.day}.sol"
    solution_class_name = f"Day{args.day}Solution"
    solution_file_name = args.input or f"./solutions/day{args.day}/input"

    try:
        solution_module = importlib.import_module(solution_module_name)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            f"Couldn't find the module {solution_module_name} :/. Either the module isn't named by the conventioned used in this script or the solution for Day 2 hasn't been implemented yet."
        )
    solution_class = getattr(solution_module, solution_class_name)

    solver = solution_class(solution_file_name)
    print(f"~~Answer~~\nPart 1: {solver.solve_1()}\nPart 2: {solver.solve_2()}")


if __name__ == "__main__":
    main()

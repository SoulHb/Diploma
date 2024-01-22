from agent import *
import sys
sys.path.append('src')
def main():
    equation = input("Enter differential equation:")
    solution = equation_solver(equation)
    print(solution)
main()
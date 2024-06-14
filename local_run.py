from main import *
import random
from qiskit.primitives import StatevectorSampler

if __name__ == "__main__":
    num_tests = 10
    sampler = StatevectorSampler()

    for test in range(num_tests):
        data, element = setup(10)
        a = grovers_algorithm(data, element, sampler)
        print("Test:", test + 1)
        print("Data:", data)
        print("Element:", element)

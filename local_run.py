from main import *
import random
from qiskit.primitives import StatevectorSampler

if __name__ == "__main__":
    num_tests = 10
    sampler = StatevectorSampler()

    for test in range(num_tests):
        data, element = setup(random.randint(2, 1000))
        a = grovers_algorithm(data, element, sampler)
        print("Test:", test + 1)
        print("Data:", data)
        print("Element:", element)

from main import *
import random
from qiskit.primitives import StatevectorSampler

if __name__ == "__main__":
    num_tests = 10
    sampler = StatevectorSampler()

    grovers_algorithm([0, 1, 2, 3], 4, sampler)
    for test in range(num_tests):
        data, element = setup(random.randint(2, 1000))
        print("Data:", data)
        print("Element:", element)
        a = grovers_algorithm(data, element, sampler)
from main import *
import random
from qiskit_aer import AerSimulator
import pandas as pd

if __name__ == "__main__":
    num_tests = 10
    sampler = AerSimulator()
    dataframe = pd.DataFrame(columns=['Data Length', 'Element'])
    for test in range(num_tests):
        data, element = setup(5)
        a = grovers_algorithm(data, element, sampler)

        result = sampler.run(a, shots=10000).result()

        counts = result.get_counts(a)
        plot_distribution(counts).show()

        max_index_length = len(bin(len(data) - 1)[2:])
        marked_index = data.index(element)
        marked_state = format(marked_index, f'0{max_index_length}b')

        dataframe.loc[len(dataframe)] = [len(data), marked_state]
        dataframe.to_csv('test_data.csv', index=False)


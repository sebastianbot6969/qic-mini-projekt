from main import *
import azure.quantum
from azure.quantum.qiskit import AzureQuantumProvider
from azure.quantum import Workspace
import json
import pandas as pd


if __name__ == "__main__":
        with open('resource.json') as resource_file:
        resource = json.load(resource_file)
        workspace = Workspace(
        resource_id=resource['id'],
        location=resource['location']
        )
        provider = AzureQuantumProvider(workspace)
        backend = provider.get_backend("rigetti.sim.qvm")
        dataframe = pd.DataFrame(columns=['Data Length', 'Element'])

        data, element = setup(10)
        a = grovers_algorithm(data, element, backend)

        result = sampler.run(a, shots=10000).result()

        counts = result.get_counts(a)
        plot_distribution(counts).show()

        max_index_length = len(bin(len(data) - 1)[2:])
        marked_index = data.index(element)
        marked_state = format(marked_index, f'0{max_index_length}b')

        dataframe.loc[len(dataframe)] = [len(data), marked_state]
        dataframe.to_csv('test_data.csv', index=False)


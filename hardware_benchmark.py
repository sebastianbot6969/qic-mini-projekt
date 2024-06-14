from main import *
import azure.quantum
from azure.quantum.qiskit import AzureQuantumProvider
from azure.quantum import Workspace
import json

if __name__ == "__main__":
    with open('resource.json') as resource_file:
        resource = json.load(resource_file)
    workspace = Workspace(
        resource_id=resource['id'],
        location=resource['location']
    )
    provider = AzureQuantumProvider(workspace)
    backend = provider.get_backend("rigetti.sim.qvm")

    num_tests = 1
    for test in range(num_tests):
        data, element = setup(10)
        a = grovers_algorithm(data, element, backend)
        print("Test:", test + 1)
        print("Data:", data)
        print("Element:", element)


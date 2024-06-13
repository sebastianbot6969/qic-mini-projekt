from main import *
import random
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

    num_tests = 10
    for test in range(num_tests):
        data, element = setup(random.randint(2, 1000))
        grovers_algorithm(data, element, backend)

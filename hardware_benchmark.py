from main import *
from azure.quantum.qiskit import AzureQuantumProvider
from azure.quantum import Workspace
import json
import pandas as pd
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler

from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager


if __name__ == "__main__":
    service = QiskitRuntimeService(channel="ibm_quantum", token="99fa61109656c3291b5a12d338aca024efa329af72bc93416cebe887757b280f324be720e2947d2c83f038ea990c6750c04689fe20cb2906fb68f84b221904e2")
    #backend = service.least_busy(operational=True, simulator=False)
    backend = service.backend("ibm_brisbane")
    pass_manager = generate_preset_pass_manager(optimization_level=1, backend=backend)


    dataframe = pd.DataFrame(columns=['Data Length', 'Element'])

    data, element = setup(5)

    a = grovers_algorithm(data, element, backend)
    sampler = Sampler(backend)
    result = sampler.run([a])

    max_index_length = len(bin(len(data) - 1)[2:])
    marked_index = data.index(element)
    marked_state = format(marked_index, f'0{max_index_length}b')

    dataframe.loc[len(dataframe)] = [len(data), marked_state]
    dataframe.to_csv('rigetti_test_data.csv', index=False)



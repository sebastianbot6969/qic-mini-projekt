from qiskit.primitives import StatevectorSampler
from main import *
from qiskit_aer import AerSimulator


def test_generate_random_str():
    string_length = 5
    random_string = generate_random_str(string_length)
    assert len(random_string) == string_length
    assert all(char in string.ascii_lowercase for char in random_string)


def test_setup():
    length = 10
    string_length = 5
    generated_list, chosen_element = setup(length, string_length)
    assert len(generated_list) == length
    assert chosen_element in generated_list


def test_brute_force_search():
    data = ['abc', 'def', 'ghi']
    existing_element = 'def'
    non_existing_element = 'xyz'
    assert brute_force_search(data, existing_element) == True
    assert brute_force_search(data, non_existing_element) == False


def test_grover_oracle():
    marked_states = ['011', '101']
    qc = grover_oracle(marked_states)
    assert isinstance(qc, QuantumCircuit)
    assert qc.num_qubits == 3


def test_grovers_algorithm():
    data = ['abc', 'def', 'ghi']
    element = 'def'
    sampler = AerSimulator()
    result = grovers_algorithm(data, element, sampler)
    assert isinstance(result, QuantumCircuit)


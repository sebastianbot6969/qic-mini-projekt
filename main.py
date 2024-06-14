import math
import random
import string
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator, MCMT, ZGate


def generate_random_str(string_length) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=string_length))


def setup(length, string_length=5):
    generated_list = [generate_random_str(string_length) for _ in range(length)]
    return generated_list, random.choice(generated_list)


def brute_force_search(data, element):
    for index, data_element in enumerate(data):
        if data_element == element:
            return True
    return False


def grover_oracle(marked_states) -> QuantumCircuit:
    if not isinstance(marked_states, list):  # If marked_states is not a list, convert it to a list
        marked_states = [marked_states]

    num_qubits = max(len(state) for state in marked_states)  # Determine the number of qubits needed

    qc = QuantumCircuit(num_qubits)  # Create a quantum circuit with the determined number of qubits

    # Apply X gates to the qubits that correspond to the marked states
    for target in marked_states:
        rev_target = target[::-1]
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
        if zero_inds:
            qc.x(zero_inds)

    # Apply a multi-controlled Z gate
    if num_qubits >= 2:
        qc.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)

    # Apply X gates to the qubits that correspond to the marked states
    for target in marked_states:
        rev_target = target[::-1]
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
        if zero_inds:
            qc.x(zero_inds)
    # Return the quantum circuit
    return qc


def grovers_algorithm(data, element, sampler):
    if element not in data:  # If the element is not in the data, return None
        return False

    max_index_length = len(bin(len(data) - 1)[2:])  # Determine the maximum length of the index in binary representation
    marked_index = data.index(element)  # Find the index of the marked element
    marked_state = format(marked_index, f'0{max_index_length}b')  # Pad with leading zeros
    marked_states = [marked_state]  # Create a list of marked states

    # Create Grover oracle circuit
    grover_oracle_circuit = grover_oracle(marked_states)

    # Create Grover operator
    grover_op = GroverOperator(grover_oracle_circuit)

    # Calculate optimal number of iterations
    optimal_num_iterations = math.floor(
        math.pi / (4 * math.asin(math.sqrt(len(marked_states) / 2 ** grover_op.num_qubits)))
    )

    # Create quantum circuit
    qc = QuantumCircuit(grover_op.num_qubits)
    # Apply Hadamard gates
    qc.h(range(grover_op.num_qubits))
    # Apply Grover operator
    qc.compose(grover_op.power(optimal_num_iterations), inplace=True)
    # Measure all qubits
    qc.measure_all()

    # Select backend and execute
    result = sampler.run([qc], shots=1).result()
    print("Found element:", element)
    return True

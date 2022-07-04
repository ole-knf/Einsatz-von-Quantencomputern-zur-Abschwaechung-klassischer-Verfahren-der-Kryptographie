from qiskit import QuantumCircuit
from qiskit import Aer
from qiskit.algorithms import AmplificationProblem
from qiskit.algorithms import Grover


def find_11_with_grover():
    w = ['11']
    oracle = QuantumCircuit(2)
    oracle.cz(0, 1)
    problem = AmplificationProblem(oracle, is_good_state=w)

    aer_simulator = Aer.get_backend('aer_simulator')
    grover = Grover(quantum_instance=aer_simulator)
    result = grover.amplify(problem)

    print('Success!' if result.oracle_evaluation else 'Failure!')
    print('Top measurement:', result.top_measurement)


find_11_with_grover()

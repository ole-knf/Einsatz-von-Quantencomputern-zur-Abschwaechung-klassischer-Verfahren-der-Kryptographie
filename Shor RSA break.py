#Folgender Codeabschnitt stammt teils aus https://qiskit.org/documentation/tutorials/algorithms/08_factorizers.html

import time
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor


def factor_finding_shor(num):
    backend = Aer.get_backend('aer_simulator')
    quantum_instance = QuantumInstance(backend, shots=1024)
    shor = Shor(quantum_instance=quantum_instance)
    result = shor.factor(num)

    print(f"The list of factors of {num} as computed by the Shor's algorithm is {result.factors[0]}.")
    return result.factors[0]


def factor_finding_shor_timer(num):
    start_time = time.time()
    factor_finding_shor(num)
    end_time = time.time()
    total_time = round(end_time - start_time, 3)
    print("Execution time: " + str(total_time) + " seconds")


def rsa_key_break(e, n):
    factors = factor_finding_shor(n)
    p = factors[0]
    q = factors[1]
    d = pow(e, -1, (p-1)*(q-1))
    print(f"The public key ({e},{n}) requires the public key to be ({d},{n})")


rsa_key_break(3, 15)
factor_finding_shor_timer(15)

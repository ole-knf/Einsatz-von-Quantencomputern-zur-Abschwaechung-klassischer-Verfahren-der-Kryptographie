# The following code is based on https://qiskit.org/documentation/tutorials/algorithms/08_factorizers.html
import time
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.algorithms import Shor


# A function which calculates the factors of the number "num" by using Shor's algorithm
def factor_finding_shor(num):
    # Create a backend which will simulate Shor's algorithm
    backend = Aer.get_backend('aer_simulator')
    quantum_instance = QuantumInstance(backend, shots=1024)
    # Copy the quantum circuit of Shor's algorithm
    shor = Shor(quantum_instance=quantum_instance)
    # Use the quantum circuit to calculate the factors of "num"
    result = shor.factor(num)
    # Print both factors and return them as a list
    print(f"The list of factors of {num} as computed by the Shor's algorithm is {result.factors[0]}.")
    return result.factors[0]

# A function which times the call of factor_finding_shor for a number "num"
# This function was only used to compare the runtime of the brute force method to Shor's algorithm
def factor_finding_shor_timer(num):
    # Create a timestamp as the start time
    start_time = time.time()
    # Call the function factor_finding_shor for "num"
    factor_finding_shor(num)
    # Create a timestamp as the end time and calculate the diffrence to the start time
    end_time = time.time()
    total_time = round(end_time - start_time, 3)
    # Print the total time needed
    print("Execution time: " + str(total_time) + " seconds")


# A function which takes a public RSA key and returns the corresponding private key
def rsa_key_break(e, n):
    # Find the factors of n by using the function factor_finding_shor
    factors = factor_finding_shor(n)
    p = factors[0]
    q = factors[1]
    # Calculate d of the private key by using all information gathered
    d = pow(e, -1, (p-1)*(q-1))
    # Print the public and private key pair
    print(f"The public key ({e},{n}) requires the public key to be ({d},{n})")

# Calls the function above to calculate the corresponding private key to the public key (3, 15)
rsa_key_break(3, 15)
# Measure the time it takes to find both factors of 15 when using Shor's algorithm
factor_finding_shor_timer(15)

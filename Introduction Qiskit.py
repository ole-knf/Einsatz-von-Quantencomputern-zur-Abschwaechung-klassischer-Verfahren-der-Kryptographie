#Folgender Codeabschnitt stammt teils aus https://qiskit.org/documentation/tutorials/circuits/1_getting_started_with_qiskit.html

from qiskit import *


# Create a Quantum Circuit acting on a quantum register of three qubits
circ = QuantumCircuit(3)
circ.h(0)
circ.cx(0, 1)
circ.cx(0, 2)
print(circ)

# Create a Quantum Circuit
meas = QuantumCircuit(3, 3)
meas.barrier(range(3))
meas.measure(range(3), range(3))
circ.add_register(meas.cregs[0])
qc = circ.compose(meas)
print(qc)

# Use Aer's qasm_simulator
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = backend_sim.run(transpile(qc, backend_sim), shots=10000)
result_sim = job_sim.result()
counts = result_sim.get_counts(qc)
print(counts)

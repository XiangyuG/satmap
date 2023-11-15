from qiskit import QuantumCircuit

#TODO: N = 2 - 15
# N = 2
qc = QuantumCircuit(N)
qc = QuantumCirqc.h(0)
qc = QuantumCirqc.cx(0,1)
qc.h(1)
qc.draw()

# N = 3
'''
qc = QuantumCircuit(N)
qc.h(0)
qc.cx(0,1)
qc.cx(0,2)
qc.h(1)
qc.cx(1,2)
qc.h(2)
qc.draw()
'''

'''
# N = 4
qc = QuantumCircuit(N)
qc.h(0)
qc.cx(0,1)
qc.cx(0,2)
qc.cx(0,3)
qc.h(1)
qc.cx(1,2)
qc.cx(1,3)
qc.h(2)
qc.cx(2,2)
qc.h(3)
qc.draw()
'''

print(qc.qasm())

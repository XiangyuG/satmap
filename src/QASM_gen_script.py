from qiskit import QuantumCircuit


f = open('qasm.txt','w')

for N in range(3,16):
    print("N = ", N, file=f)
    print("qc = QuantumCircuit(N)", file=f)
    for i in range(0,N):
        print("qc.h(", i, ")", file=f)
        for j in range(i+1, N):
            print("qc.cx(", i,",",j, ")", file=f)
    print("qc.draw()\n", file=f)
    

#TODO: N = 2 - 15
# N = 2
'''
N = 2
qc = QuantumCircuit(N)
qc.h(0)
qc.cx(0,1)
qc.h(1)
qc.draw()
'''

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




# print(qc.qasm())

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import circuit as C
import base64
import io

Circuit = C.Circuit
Gate = C.Gate

def getActionParams(qc: QuantumCircuit, gate: Gate):
    actions = {
        "barrier": qc.barrier,
        "H": qc.h,
        "CX": qc.cx,
        "Z": qc.z,
        "X": qc.x
    }
    action = actions.get(gate.name)
    source = gate.option == "control" or (gate.option != "target" and action != None)
    target = gate.option == "target"
    return action, source, target

def runSimulation(circuit: Circuit):
    nbRegisters = len(circuit.registers)
    nbGates = len(circuit.registers[0].gates)

    qc = QuantumCircuit(nbRegisters, nbRegisters)

    for i_gate in range(nbGates):
        source = -1
        target = -1
        action = None
        for i_reg in range(len(circuit.registers)):
            register = circuit.registers[i_reg]
            gate = register.gates[i_gate]
            if gate != None:
                a, s, t = getActionParams(qc, gate)
                if a != None:
                    action = a
                if s == True:
                    source = i_reg
                if t == True:
                    target = i_reg
        if action != None and target == -1:
            action(source)
        elif action != None:
            action(source, target)

    job = execute(qc, Aer.get_backend("statevector_simulator"))
    statevector = job.result().get_statevector()

    for i in range(nbRegisters):
        qc.measure(i, i)

    backend = Aer.get_backend("qasm_simulator")
    job = execute(qc, backend, shots=1024)
    result = job.result()
    count = result.get_counts(qc)
    return count, statevector

def getBase64Plot(count, statevector, level):
    ioBytes = io.BytesIO()
    if level == 1:
        fig = plot_bloch_multivector(statevector)
    else:
        fig = plot_histogram(count)
    fig.savefig(ioBytes, format = 'png')
    ioBytes.seek(0)
    encodedPlot = base64.b64encode(ioBytes.read())
    return encodedPlot.decode('utf-8')

from flask import Flask, request
import circuit as C
import quantum as qu
import json
import pprint

Circuit = C.Circuit
solutionCircuitsByLevel = C.allCircuitsByLevel

app = Flask(__name__)


@app.route('/getCircuits')
def getCircuits():
    circuits = list(solutionCircuitsByLevel.values())
    return json.dumps(circuits, default = lambda o: o.__dict__, indent = 4)

@app.route('/checkCircuit', methods = ['POST'])
def checkCircuit():
    circuit = Circuit.from_json(request.get_json())
    solutionsCircuits = solutionCircuitsByLevel[circuit.level]
    if circuit in solutionsCircuits:
        return 'SUCCESS'
    else:
        return 'FAILURE'

@app.route('/runOnQiskit', methods = ['POST'])
def runOnQiskit():
    circuit = Circuit.from_json(request.get_json())
    count = qu.runSimulation(circuit)
    app.logger.info(count)
    encodedPlot = qu.getBase64Plot(count)
    return encodedPlot

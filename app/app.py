from flask import Flask, request
from flask_cors import CORS, cross_origin
import circuit as C
import quantum as qu
import json
import pprint

Circuit = C.Circuit
solutionCircuitsByLevel = C.allCircuitsByLevel

app = Flask(__name__)
CORS(app)

@app.route('/getCircuits')
@cross_origin()
def getCircuits():
    circuits = list(solutionCircuitsByLevel.values())
    return json.dumps(circuits, default = lambda o: o.__dict__, indent = 4)

@app.route('/checkCircuit', methods = ['POST'])
@cross_origin()
def checkCircuit():
    circuit = Circuit.from_json(request.get_json())
    solutionsCircuits = solutionCircuitsByLevel[circuit.level]
    if circuit in solutionsCircuits:
        return 'SUCCESS'
    else:
        return 'FAILURE'

@app.route('/runOnQiskit', methods = ['POST'])
@cross_origin()
def runOnQiskit():
    circuit = Circuit.from_json(request.get_json())
    count, statevector = qu.runSimulation(circuit)
    app.logger.info(count)
    encodedPlot = qu.getBase64Plot(count, statevector, circuit.level)
    response = {
        'count': count,
        'img': encodedPlot
    }
    return json.dumps(response)

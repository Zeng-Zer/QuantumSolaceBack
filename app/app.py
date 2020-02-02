from flask import Flask, request
import json

app = Flask(__name__)

class Circuit:
    def __init__(self, id, type, option):
        self.id = id
        self.type = type
        self.option = option

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


@app.route('/getCircuits')
def getCircuits():
    test = Circuit(1, "type", "option")
    return test.toJSON()

@app.route('/getQTP')
def getQTP():
    return 'QTP'

@app.route('/checkCircuit', methods = ['POST'])
def checkCircuit():
    print(request.get_json())
    return 'SUCCESS'

@app.route('/runOnQiskit', methods = ['POST'])
def runOnQiskit():
    print(request.get_json())
    return 'QISKIT'

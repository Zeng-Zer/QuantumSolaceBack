from flask import Flask, request

app = Flask(__name__)


@app.route('/getCircuits')
def getCircuits():
    return 'CIRCUITS'

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

from typing import List
import os
import itertools
import json

class Gate:
    @classmethod
    def from_json(cls, data):
        if data == None:
            return None
        else:
            return cls(**data)

    def __init__(self, name: str, option: str):
        self.name = name
        self.option = option

    def __eq__(self, other):
        return (self is None and other is None) or \
            (self != None and other != None and self.name == other.name and self.option == other.option)

    def __ne__(self, other):
        return (self is None and other is not None) or (self is not None and other is None) or \
            self.gates != other.gates or self.option != other.option


class Register:
    @classmethod
    def from_json(cls, data):
        gates = list(map(Gate.from_json, data))
        return cls(gates)

    def __init__(self, gates: List[Gate]):
        self.gates = gates

    def __eq__(self, other):
        return self.gates == other.gates

    def __ne__(self, other):
        return self.gates != other.gates


class Circuit:
    @classmethod
    def from_json(cls, data):
        level = data["level"]
        registers = list(map(Register.from_json, data["registers"]))
        if "explanation" in data:
            explanation = data["explanation"]
        else:
            explanation = ""
        return cls(level, registers, explanation)

    def __init__(self, level: int, registers: List[Register], explanation: str):
        self.level = level
        self.registers = registers
        self.explanation = explanation

    def __eq__(self, other):
        return self.level == other.level and self.registers == other.registers and self.explanation == other.explanation

    def __ne__(self, other):
        return self.level != other.level or self.registers != other.registers or self.explanation != other.explanation


def getAllCircuitsByLevel():
    circuitsByLevel = {}
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../res/circuits.json')
    with open(filename) as f:
        data = json.load(f)
        circuits = map(lambda x: Circuit.from_json(x), data)
        grouped = itertools.groupby(circuits, key = lambda x: x.level)
        for level, cs in grouped:
            circuitsByLevel[level] = list(cs)
    return circuitsByLevel

allCircuitsByLevel = getAllCircuitsByLevel()

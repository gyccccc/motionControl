import socket
import threading
import json
import time

"""change testjson to control metahuman expression"""

paramArrary = []
boneArrary = []
jsonResult = {}
jsonFinal = {}

for i in range(10):
    obj = {'Name': "right name", 'Value': "right value"}
    paramArrary.append(obj)

headBone = {'Name': "Head",
            'Parent': -1,
            'Location': [0, 0, 0],
            'Rotation': [0, 0, 0],
            'Scale': [1, 1, 1]}

boneArrary.append(headBone)
jsonResult['Bone'] = boneArrary
jsonResult['Parameter'] = paramArrary
jsonFinal['android'] = jsonResult

ipaddress = ("192.168.1.152", 11111)
cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# cli.connect(ipaddress)
print(jsonFinal)

testjson = {"android": {"Bone": [{"Name": "Head", "Parent": -1, "Location": [0, 0, 0],
                                  "Rotation": [-0.044215605, 0.018701324, -0.08034033, 0.9956107], "Scale": [0, 0, 0]}],
                        "Parameter": [{"Name": "browOuterUpLeft", "Value": 0.13270485},
                                      {"Name": "browInnerUpLeft", "Value": 0.0217743},
                                      {"Name": "browDownLeft", "Value": 0.030909928},
                                      {"Name": "eyeBlinkLeft", "Value": 0.008587414},
                                      {"Name": "eyeSquintLeft", "Value": 0.08684245},
                                      {"Name": "eyeWideLeft", "Value": 0.019322554},
                                      {"Name": "eyeLookUpLeft", "Value": 0.14725171},
                                      {"Name": "eyeLookOutLeft", "Value": 0.041758154},
                                      {"Name": "eyeLookInLeft", "Value": 0.029516565},
                                      {"Name": "eyeLookDownLeft", "Value": 0.038173012},
                                      {"Name": "noseSneerLeft", "Value": 0.0023600564},
                                      {"Name": "mouthUpperUpLeft", "Value": 1.091706E-5},
                                      {"Name": "mouthSmileLeft", "Value": 0.14898233},
                                      {"Name": "mouthLeft", "Value": 8.8955215E-7},
                                      {"Name": "mouthFrownLeft", "Value": 2.4013032E-6},
                                      {"Name": "mouthLowerDownLeft", "Value": 0.029986627},
                                      {"Name": "jawLeft", "Value": 0.005504965},
                                      {"Name": "cheekPuff", "Value": 0.007256892},
                                      {"Name": "mouthShrugUpper", "Value": 0.004847104},
                                      {"Name": "mouthFunnel", "Value": 0.011520468},
                                      {"Name": "mouthRollLower", "Value": 0.011173302},
                                      {"Name": "jawOpen", "Value": -2.6444745E-6},
                                      {"Name": "tongueOut", "Value": 0.0076810257},
                                      {"Name": "mouthPucker", "Value": 0.01952764},
                                      {"Name": "mouthRollUpper", "Value": 0.011341397},
                                      {"Name": "jawRight", "Value": 0.22556275},
                                      {"Name": "mouthLowerDownRight", "Value": 0.030444907},
                                      {"Name": "mouthFrownRight", "Value": 3.6600832E-6},
                                      {"Name": "mouthRight","Value": 5.046384E-7},
                                      {"Name": "mouthSmileRight","Value": 0.064317495},
                                      {"Name": "mouthUpperUpRight","Value": 2.6314472E-5},
                                      {"Name": "noseSneerRight","Value": 0.0023587374},
                                      {"Name": "eyeLookDownRight","Value": 0.03809583},
                                      {"Name": "eyeLookInRight","Value": 0.04240543},
                                      {"Name": "eyeLookOutRight","Value": 0.022643492},
                                      {"Name": "eyeLookUpRight","Value": 0.14720361},
                                      {"Name":"eyeWideRight","Value":0.018056832},
                                      {"Name":"eyeSquintRight","Value":0.08685683},
                                      {"Name":"eyeBlinkRight","Value":0.008586093},
                                      {"Name":"browDownRight","Value":0.03145967},
                                      {"Name":"browInnerUpRight","Value":0.022048565},
                                      {"Name":"browOuterUpRight","Value":0.015740598}]}}

for i in range(10000):
    # cli.send((bytes(repr(json.dumps(jsonFinal)).encode('utf-8'))))
    cli.sendto((bytes(json.dumps(testjson).encode('utf-8'))), ipaddress)
    time.sleep(0.05)
    print(i)

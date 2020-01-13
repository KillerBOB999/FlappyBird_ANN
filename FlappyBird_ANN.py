import NeuralNetwork
from NeuralNetwork import NeuralNetwork

import Edge
from Edge import Edge

def main(playerX: int, playerY: int, pipeInfo: list, stillAlive: bool): 
    test1 = Edge(0, 3, 100, 100)
    test2 = Edge(1, 3, 100, 100)
    test3 = Edge(2, 3, 100, 100)

    supertest = (test1, test2, test3)
    NNTest = NeuralNetwork(supertest, 4, (3))


    if pipeInfo[0]['x'] >= 0:
        print("Pipe Info = ", pipeInfo[0]['x'])
    else:
        print("Pipe Info = ", pipeInfo[1]['x'])
    return
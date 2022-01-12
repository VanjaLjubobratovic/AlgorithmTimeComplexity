import numpy as np
from dijkstra import Graph
from searchAlgo import *
from fibonacci import *
import time
import matplotlib.pyplot as plt

def main ():

    plt.figure()
    xpoints = np.array([0, 6])
    ypoints = np.array([0, 250])
    plt.plot(xpoints, ypoints)
    plt.show()

if __name__ == "__main__":
    main()
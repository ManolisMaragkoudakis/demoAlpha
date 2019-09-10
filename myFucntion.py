import numpy as np
import matplotlib.pyplot as plt

def plotXY(X = np.array([]), Y = np.array([])):
    plt.figure(1)
    plt.plot(X,Y,'o')
    plt.show()
    return
       

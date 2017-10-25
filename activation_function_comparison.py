import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
sigmoid = lambda x: 1/(1+np.exp(-x))

#activation function
af_sigmoid = sigmoid(x)
af_ReLu = np.maximum(x,0)
af_Swiss = x*sigmoid(x)

#derivative
de_sig = sigmoid(x)*(1-sigmoid(x))
de_swi = sigmoid(x)+x*sigmoid(x)*(1-sigmoid(x))

#plot
plt.plot(x,af_sigmoid,'g',label='sigmoid')
plt.plot(x,af_ReLu,'ro',label='ReLu')
plt.plot(x,af_Swiss,'bs',label='Swiss')
plt.plot(x,de_sig,'y+',label='Derivative of sigmoid')
plt.plot(x,de_swi,'k-.',label='Derivative of Swiss')

plt.legend(bbox_to_anchor=(0,1),loc=2,borderaxespad=0.)
plt.grid(True)
plt.show()

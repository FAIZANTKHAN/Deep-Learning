# This contains the basic understandings how the different activation function works
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# This activation function use to change the value into from 0 to 1
print(sigmoid(100))
print(sigmoid(1))


def tank(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

#Change the value into from 1 to -1

print(tank(-56))
print(tank(50))
print(tank(1))

def relu(x):
    return max(0,x)

#max of  the 0 or that value

print(relu(-7))
print(relu(1))

def leaky_relu(x):
    return max(0.1*x,x)

print(leaky_relu(-100))
print(leaky_relu(8))

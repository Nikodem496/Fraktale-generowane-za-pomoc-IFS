import pylab
import random as r
x = [0]
y = [0]

for _ in range(2000000):
    random_num = r.random()

    if random_num < 0.142:
        x.append(0.05*x[-1] + 0.0*y[-1] - 0.06)
        y.append(0.0*x[-1] + 0.4*y[-1] - 0.47)
    elif random_num < 0.142*2:
        x.append(-0.05*x[-1] + 0.0*y[-1] - 0.06)
        y.append(0.0*x[-1] - 0.4*y[-1] - 0.47)
    elif random_num < 0.142*3:
        x.append(0.03*x[-1] - 0.14*y[-1] - 0.16)
        y.append(0.0*x[-1] + 0.26*y[-1] -0.01)
    elif random_num < 0.142*4:
        x.append(-0.03*x[-1] + 0.14*y[-1] - 0.16)
        y.append(0.0*x[-1] - 0.26*y[-1] -0.01)
    elif random_num < 0.142*5:
        x.append(0.56*x[-1] + 0.44*y[-1] + 0.3)
        y.append(-0.37*x[-1] + 0.51*y[-1] + 0.15)
    elif random_num < 0.142*6:
        x.append(0.19*x[-1] + 0.07*y[-1] - 0.2)
        y.append(-0.1*x[-1] + 0.15*y[-1] + 0.28)
    elif random_num < 0.142*7:
        x.append(-0.33*x[-1] - 0.34*y[-1] - 0.54)
        y.append(-0.33*x[-1] + 0.34*y[-1] + 0.39)

pylab.figure()
pylab.scatter(x,y,s = 5)
pylab.show()

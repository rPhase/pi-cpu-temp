from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore",".*GUI is implemented.*")

plt.ion()
x = []
y = []

cpu = CPUTemperature()

def write_temp(temp):
    with open("cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def redraw():
    plt.draw()
    plt.pause(0.00001)

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.title("CPU Temp")
    plt.ylabel("Temperature")
    plt.xlabel("Time")
    plt.scatter(x,y)
    plt.plot(x,y)
    redraw()

while True:
    temp = cpu.temperature
    write_temp(temp)
    graph(temp)
    sleep(1)

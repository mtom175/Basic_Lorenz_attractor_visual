#imports
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#parameters
b = 8/3 #fuild layer
o = 10 #Prandtl number
p = 28 #Rayleigh number

xs = [0]
ys = [1]
zs = [1.05]

#time
dt = 0.01


#steps
steps = 10000


#Lorenz PDEs
def lorenz(x, y, z):
    dx = o*(y - x)
    dy = x*(p -z)-y
    dz = x*y - b*z
    return (x + dx*dt), (y + dy*dt), (z + dz*dt)

#intergartion of the pdes over time
for i in range(steps):
    x, y , z = lorenz(xs[-1], ys[-1], zs[-1])
    xs.append(x)
    ys.append(y)
    zs.append(z)



#Plot
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111, projection='3d')

ax.plot(xs, ys, zs, color = 'white', lw=0.1)
ax.set_facecolor("black")
line, = ax.plot([], [], [], lw=2, color='orange')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
#animation

frames = 10000
def update(frame):
    line.set_data(xs[:frame], ys[:frame])
    line.set_3d_properties(zs[:frame])
    return line,


ani = FuncAnimation(fig,
                    update,
                    frames = frames,
                    interval = 5,
                    blit = True)

#ani.save('Lorenz_attractor.mp4', writer = 'ffmpeg', fps = 30)

plt.show()

import rebound
import matplotlib; matplotlib.use("pdf")
import matplotlib.pyplot as plt
import numpy as np

# create simulation object
sim = rebound.Simulation()

sim.add(m=1., x=-9, vy=-0.15) # Star 1
sim.add(m=1., x=9, vy=0.15) # Star 2

objects = ["Star_1", "Star_2"]

# moves center of mass to origin
sim.move_to_com()
sim.integrator = "whfast"
sim.set_dt=0.01

Nout = 1000
times = np.linspace(0, 100.*np.pi, Nout) # 50 orbits
x = np.zeros((sim.N,Nout))
y = np.zeros((sim.N,Nout))

ps = sim.particles
for ti,t in enumerate(times):
    sim.integrate(t)
    for i, p in enumerate(ps):
        x[i][ti] = p.x
        y[i][ti] = p.y


fig = plt.figure(figsize=(11,5))

def plot(zoom):
    ax.set_xlim([-zoom,zoom])
    ax.set_ylim([-zoom,zoom])
    ax.set_xlabel("x [AU]")
    ax.set_ylabel("y [AU]")
    for i in xrange(0,sim.N):
        plt.plot(x[i],y[i])
        if x[i][-1]*x[i][-1]+y[i][-1]*y[i][-1]>0.01*zoom*zoom or i==0:
            ax.annotate(objects[i], xy=(x[i][-1], y[i][-1]),horizontalalignment="center")

ax = plt.subplot(121)
plot(zoom=24.)

plt.savefig("orbits.pdf")

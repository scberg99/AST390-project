import rebound
import matplotlib; matplotlib.use("pdf")
import matplotlib.pyplot as plt
import numpy as np

# create simulation object
sim = rebound.Simulation()
sim.add(m=1) # Sun
sim.add(m=1.66e-30, a=0.387, e=0.205) # Mercury
sim.add(m=2.447e-6, a=0.723336, e=0.00678) # Venus
sim.add(m=3e-6, a=1.0, e=0.017) #Earth
sim.add(m=3.212e-7, a=1.52371, e=0.09339) # Mars
sim.add(m=9.543e-4,a=5.2029,e=0.0484) # Jupiter
sim.add(m=2.856e-4,a=9.583,e=0.0565) #Saturn
sim.add(m=4.372e-5,a=19.189,e=0.04726) # Uranus
sim.add(m=5.178e-5,a=30.0699,e=0.00859) # Neptune

sim.move_to_com()
sim.status()

eccen_merc = []
eccen_venus = []
eccen_earth = []
eccen_mars = []
eccen_jup = []
eccen_sat = []
eccen_ur = []
eccen_nep = []
times = []


for i in range(101):
    tmax=1.0e2*i
    sim.integrate(tmax)
    times.append(sim.t)
    eccen_merc.append(sim.particles[1].e)
    eccen_venus.append(sim.particles[2].e)
    eccen_earth.append(sim.particles[3].e)
    eccen_mars.append(sim.particles[4].e)
    eccen_jup.append(sim.particles[5].e)
    eccen_sat.append(sim.particles[6].e)
    eccen_ur.append(sim.particles[7].e)
    eccen_nep.append(sim.particles[8].e)

plt.plot(times, eccen_merc)
plt.plot(times, eccen_venus)
plt.plot(times, eccen_earth)
plt.plot(times, eccen_mars)
plt.plot(times, eccen_jup)
plt.plot(times, eccen_sat)
plt.plot(times, eccen_ur)
plt.plot(times, eccen_nep)

plt.xlabel('Time (unit)')
plt.ylabel('Eccentricity')
plt.savefig("orbits.pdf")

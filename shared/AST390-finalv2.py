import rebound
import matplotlib; matplotlib.use("pdf")
import matplotlib.pyplot as plt
import numpy as np

def get_e_vals():
    eccen_merc.append(sim.particles[1].e)
    eccen_venus.append(sim.particles[2].e)
    eccen_earth.append(sim.particles[3].e)
    eccen_mars.append(sim.particles[4].e)
    eccen_jup.append(sim.particles[5].e)
    eccen_sat.append(sim.particles[6].e)
    eccen_ur.append(sim.particles[7].e)
    eccen_nep.append(sim.particles[8].e)

def plot_e_vals():
    merc = plt.plot(times, eccen_merc, label='mercury')
    venus = plt.plot(times, eccen_venus, label='venus')
    earth = plt.plot(times, eccen_earth, label='earth')
    mars = plt.plot(times, eccen_mars, label='mars')
    jupiter = plt.plot(times, eccen_jup, label='jupiter')
    saturn = plt.plot(times, eccen_sat, label='saturn')
    uranus = plt.plot(times, eccen_ur, label='uranus')
    neptune = plt.plot(times, eccen_nep, label='neptune')
    plt.legend()
    plt.title('Orbital Eccentricities')
    plt.xlabel('Time (years)')
    plt.ylabel('Eccentricity')
    plt.savefig("eccentricity.pdf")

a_vals = {'Mercury':0.387,'Venus':0.723336,'Earth':1,'Mars':1.52371,
          'Jupiter':5.2029,'Saturn':9.583,'Uranus':19.189,'Neptune':30.0699}

# create simulation object
sim = rebound.Simulation()
sim.add(m=1) # Sun
sim.add(m=1.66e-30, a=a_vals["Mercury"], e=0.205) # Mercury
sim.add(m=2.447e-6, a=a_vals["Venus"], e=0.00678) # Venus
sim.add(m=3e-6, a=a_vals["Earth"], e=0.017) # Earth
sim.add(m=3.212e-7, a=a_vals["Mars"], e=0.09339) # Mars
sim.add(m=9.543e-4,a=a_vals["Jupiter"], e=0.0484) # Jupiter
sim.add(m=2.856e-4,a=a_vals["Saturn"],e=0.0565) # Saturn
sim.add(m=4.372e-5,a=a_vals["Uranus"],e=0.04726) # Uranus
sim.add(m=5.178e-5,a=a_vals["Neptune"],e=0.00859) # Neptune

sim.move_to_com()
sim.integrator = 'whfast'

eccen_merc = [] # Eccentricity of mercury orbit
eccen_venus = []
eccen_earth = []
eccen_mars = []
eccen_jup = []
eccen_sat = []
eccen_ur = []
eccen_nep = []

times = []

for step in np.linspace(0,100000,100): # 20000 orbits
    sim.integrate(step)
    times.append(sim.t)
    get_e_vals()

plot_e_vals()

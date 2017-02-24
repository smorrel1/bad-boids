#!/usr/bin/env python
"""
This plots a flock of [50] birds flocking. Flying rules are each bird flys towards the middle of the flock, doesn't
crash into its neighbours and matches the speed of more distant neighbours.
Args:
  a config.yml containing 9 space and speed parammeters:
  x_min x_max y_min y_max n_boids x_vel_min x_vel_max y_vel_min y_vel_max
  """
# TODO:  Change of variable/function/class name
# TODO:  Replace global variables with function arguments, Break a large function into smaller units
# TODO: Replace loop with iterator
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import yaml
from boid_utilities import *

flark = yaml.load(open("/Users/stephenmorrell/git/bad-boids/config.yml"))
flark_params = {'radius_bump': 100, 'radius_attraction': 10000, 'affinity': 0.125}
boids = instantiate_boids(**flark)
figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])

def animate(frame):
  update_boids(boids, flark_params=flark_params)
  scatter.set_offsets(zip(boids[0], boids[1]))

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
  plt.show()

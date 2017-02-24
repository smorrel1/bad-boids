"""
Args:
  a config.yml containing 9 parammeters
  x_min x_max y_min y_max n_boids x_vel_min x_vel_max y_vel_min y_vel_max
  """
# TODO:  Replace magic numbers with constants, Replace repeated code with a function
# TODO:  Change of variable/function/class name, Replace loop with iterator
# TODO:  Replace global variables with function arguments, Break a large function into smaller units
# TODO:  Separate code concepts into files or modules
# TODO: use assert statements
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import yaml
from boid_utilities import *

flark_params = {'radius_bump': 100, 'radius_attraction': 10000, 'affinity': 0.125}

def update_boids(boids, flark_params):
  positions_x, positions_y, velocities_x, velocities_y = boids
  velocities_x, velocities_y = fly_to_middle(velocities_x, positions_x, velocities_y, positions_y)
  velocities_x, velocities_y = dont_crash(velocities_x, positions_x, velocities_y, positions_y, flark_params)
  velocities_x, velocities_y = match_speed(velocities_x, positions_x, velocities_y, positions_y, flark_params)
  positions_x, positions_y = fly_a_bit(velocities_x, positions_x, velocities_y, positions_y)

flark = yaml.load(open("/Users/stephenmorrell/git/bad-boids/config.yml"))
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

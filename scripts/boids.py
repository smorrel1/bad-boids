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
import yaml
from boid_utilities import *
import argparse

def boids():

  def animate(frame):
    update_boids(boids, flark_params=flark_params)
    scatter.set_offsets(zip(boids[0], boids[1]))

  flark = yaml.load(open("/Users/stephenmorrell/git/bad-boids/config.yml"))
  flark_params = {'radius_bump': 100, 'radius_attraction': 10000, 'affinity': 0.125}
  parser = argparse.ArgumentParser(description='parameters to fly the boids')
  parser.add_argument('--radius_bump', dest='radius_bump', type=int, default=100,
                      help='how far each bird is from another before it must fly away')
  parser.add_argument('--radius_attraction', dest='radius_attraction', type=int, default=10000,
                      help='The radius within which the bird is attracted to others in the flock')
  parser.add_argument('--affinity', dest='affinity', type=float, default=0.125,
                      help='The strength of attraction to other birds within the radius_attraction')
  args = parser.parse_args()  # produces Namespace()
  flark_params['radius_bump'] = args.radius_bump
  flark_params['radius_attraction'] = args.radius_attraction
  flark_params['affinity'] = args.affinity
  boids = instantiate_boids(**flark)
  figure = plt.figure()
  axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
  scatter = axes.scatter(boids[0], boids[1])
  anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)
  plt.show()

if __name__ == "__main__":
  boids()

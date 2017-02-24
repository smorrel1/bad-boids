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

radius_bump = 100
radius_attraction = 10000
affinity = 0.125

def instantiate_boids(x_min=-450.0, x_max=50.0, y_min=300.0, y_max=600.0, n_boids=50, x_vel_min=0.0, x_vel_max=10.0,
                      y_vel_min=-20.0, y_vel_max=20.0):
  boids_x = np.random.rand(n_boids)*(x_max-x_min)+x_min
  boids_y = np.random.rand(n_boids)*(y_max-y_min)+y_min
  boid_x_velocities = np.random.rand(n_boids)*(x_vel_max-x_vel_min) + x_vel_min
  boid_y_velocities = np.random.rand(n_boids)*(y_vel_max-y_vel_min) + y_vel_min
  boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)
  return boids

# change each bird's velocity towards the centre of the flock
def fly_to_middle(velocities_x, positions_x,velocities_y, positions_y):
  for i in range(len(positions_x)):
    for j in range(len(positions_x)):
      velocities_x[i] = velocities_x[i] + (positions_x[j] - positions_x[i]) * 0.01 / len(positions_x)
      velocities_y[i] = velocities_y[i] + (positions_y[j] - positions_y[i]) * 0.01 / len(positions_y)
  return velocities_x, velocities_y

# Fly away from nearby boids
def dont_crash(xvs, xs, yvs, ys):
  def flee(speed, me, they):
    return speed + (me - they)
  flock_size = len(xs)
  for i in range(flock_size):
    for j in range(flock_size):
      distance = (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2
      if distance < radius_bump:
        xvs[i] = flee(xvs[i], xs[i], xs[j])
        yvs[i] = flee(yvs[i], ys[i], ys[j])
  return xvs, yvs

def match_speed(xvs, xs, yvs, ys):
  # Try to match speed with nearby boids
  flock_size = len(xs)
  for i in range(flock_size):
    for j in range(flock_size):
      distance = (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2
      def move_towards(me, they):
        return me + (they - me) * affinity / flock_size
      if distance < radius_attraction:
        xvs[i] = move_towards(xvs[i], xvs[j])
        yvs[i] = move_towards(yvs[i], yvs[j])
  return xvs, yvs

  # Move according to velocities
def fly_a_bit(velocities_x, positions_x, velocities_y, positions_y):
  for i in range(len(positions_x)):
    positions_x[i] = positions_x[i] + velocities_x[i]
    positions_y[i] = positions_y[i] + velocities_y[i]
  return positions_x, positions_y

def update_boids(boids):
  positions_x, positions_y, velocities_x, velocities_y = boids
  velocities_x, velocities_y = fly_to_middle(velocities_x, positions_x, velocities_y, positions_y)
  velocities_x, velocities_y = dont_crash(velocities_x, positions_x, velocities_y, positions_y)
  velocities_x, velocities_y = match_speed(velocities_x, positions_x, velocities_y, positions_y)
  positions_x, positions_y = fly_a_bit(velocities_x, positions_x, velocities_y, positions_y)

flark = yaml.load(open("/Users/stephenmorrell/git/bad-boids/config.yml"))
boids = instantiate_boids(**flark)
figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])

def animate(frame):
  update_boids(boids)
  scatter.set_offsets(zip(boids[0], boids[1]))

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
  plt.show()

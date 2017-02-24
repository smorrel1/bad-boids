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
  for i in range(len(xs)):
    for j in range(len(xs)):
      distance = (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2
      if distance < radius_bump:
        xvs[i] = flee(xvs[i], xs[i], xs[j])
        yvs[i] = flee(yvs[i], ys[i], ys[j])
  return xvs, yvs

def match_speed(xvs, xs, yvs, ys):
  # Try to match speed with nearby boids
  for i in range(len(xs)):
    for j in range(len(xs)):
      if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < radius_attraction:
        xvs[i] = xvs[i] + (xvs[j] - xvs[i]) * 0.125 / len(xs)
        yvs[i] = yvs[i] + (yvs[j] - yvs[i]) * 0.125 / len(xs)
  return xvs, yvs

def update_boids(boids):
  xs, ys, xvs, yvs = boids
  xvs, yvs = fly_to_middle(xvs, xs, yvs, ys)
  xvs, yvs = dont_crash(xvs, xs, yvs, ys)
  xvs, yvs = match_speed(xvs, xs, yvs, ys)

    # Move according to velocities
  for i in range(len(xs)):
    xs[i] = xs[i] + xvs[i]
    ys[i] = ys[i] + yvs[i]

flark = yaml.load(open("/Users/stephenmorrell/git/bad-boids/config.yml"))
boids = instantiate_boids(**flark)
# boids = instantiate_boids(x_min=-450.0, x_max=50.0, y_min=300.0, y_max=600.0, n_boids=50, x_vel_min=0.0, x_vel_max=10.0,
#                       y_vel_min=-20.0, y_vel_max=20.0)
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

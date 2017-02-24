"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""
# TODO:  Replace magic numbers with constants, Replace repeated code with a function
# TODO:  Change of variable/function/class name, Replace loop with iterator
# TODO:  Replace hand-written code with library code
# TODO:  Replace set of arrays with array of structures
# TODO:  Replace constants with a configuration file
# TODO:  Replace global variables with function arguments, Break a large function into smaller units
# TODO:  Separate code concepts into files or modules
# TODO: use assert statements
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# Deliberately terrible code for teaching purposes
def instantiate_boids(x_min=-450.0, x_max=50.0, y_min=300.0, y_max=600.0, n_boids=50, x_vel_min=0.0, x_vel_max=10.0,
                      y_vel_min=-20.0, y_vel_max=20.0):
  # boids_x = [random.uniform(-450, 50.0) for x in range(n_boids)]
  boids_x = np.random.rand(n_boids)*(x_max-x_min)+x_min
  boids_y = [random.uniform(300.0, 600.0) for x in range(n_boids)]
  boids_y = np.random.rand(n_boids)*(y_max-y_min)+y_min
  # boid_x_velocities = [random.uniform(0, 10.0) for x in range(n_boids)]
  boid_x_velocities = np.random.rand(n_boids)*(x_vel_max-x_vel_min) + x_vel_min
  # boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(n_boids)]
  boid_y_velocities = np.random.rand(n_boids)*(y_vel_max-y_vel_min) + y_vel_min
  boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)
  return boids

def update_boids(boids):
  xs, ys, xvs, yvs = boids
  # Fly towards the middle
  for i in range(len(xs)):
    for j in range(len(xs)):
      xvs[i] = xvs[i] + (xs[j] - xs[i]) * 0.01 / len(xs)
  for i in range(len(xs)):
    for j in range(len(xs)):
      yvs[i] = yvs[i] + (ys[j] - ys[i]) * 0.01 / len(xs)
  # Fly away from nearby boids
  for i in range(len(xs)):
    for j in range(len(xs)):
      if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 100:
        xvs[i] = xvs[i] + (xs[i] - xs[j])
        yvs[i] = yvs[i] + (ys[i] - ys[j])
  # Try to match speed with nearby boids
  for i in range(len(xs)):
    for j in range(len(xs)):
      if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < 10000:
        xvs[i] = xvs[i] + (xvs[j] - xvs[i]) * 0.125 / len(xs)
        yvs[i] = yvs[i] + (yvs[j] - yvs[i]) * 0.125 / len(xs)
  # Move according to velocities
  for i in range(len(xs)):
    xs[i] = xs[i] + xvs[i]
    ys[i] = ys[i] + yvs[i]

boids = instantiate_boids(n_boids=50)
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

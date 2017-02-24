import os

import yaml
from nose.tools import assert_almost_equal
from nose.tools import assert_greater_equal
from nose.tools import assert_less_equal

from scripts import boids


def test_instantiate_boids():
  my_boids= boids.instantiate_boids()
  boids_x, boids_y, boid_x_velocities, boid_y_velocities = my_boids
  assert_greater_equal(min(boids_x), -450.0, 'x_min failed')
  assert_less_equal(max(boids_x), 50, 'x_max failed')
  assert_greater_equal(min(boids_y), 300.0, 'y_min failed')
  assert_less_equal(max(boids_y), 600, 'y_max failed')

def test_instantiate_boids_speeds():
  my_boids= boids.instantiate_boids()
  boids_x, boids_y, boid_x_velocities, boid_y_velocities = my_boids
  assert_greater_equal(min(boid_x_velocities), 0.0, 'x_min_velocities failed')
  assert_less_equal(max(boid_x_velocities), 10., 'x_max_velocities failed')
  assert_greater_equal(min(boid_y_velocities), -20.0, 'y_min_velocities failed')
  assert_less_equal(max(boid_y_velocities), 20., 'y_max_velocities failed')

# test non-standard values from config file
def test_instantiate_boids_nonstandard():
  flark = yaml.load(open(os.path.join(os.path.dirname(__file__), '..',"config.yml")))
  boids_x, boids_y, boid_x_velocities, boid_y_velocities = boids.instantiate_boids(**flark)
  assert_greater_equal(min(boids_x), flark['x_min'], 'x_min failed')
  assert_less_equal(max(boids_x), flark['x_max'], 'x_max failed')
  assert_greater_equal(min(boids_y), flark['y_min'], 'y_min failed')
  assert_less_equal(max(boids_y), flark['y_max'], 'y_max failed')
  assert_greater_equal(min(boid_x_velocities), flark['x_vel_min'], 'x_min_velocities failed')
  assert_less_equal(max(boid_x_velocities), flark['x_vel_max'], 'x_max_velocities failed')
  assert_greater_equal(min(boid_y_velocities), flark['y_vel_min'], 'y_min_velocities failed')
  assert_less_equal(max(boid_y_velocities), flark['y_vel_max'], 'y_max_velocities failed')


# test boids move by <= 0.01
def test_bad_boids_regression():
  regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), '..', 'fixture.yml')))
  boid_data = regression_data["before"]
  flark_params = {'radius_bump': 100, 'radius_attraction': 10000, 'affinity': 0.125}
  boids.update_boids(boid_data, flark_params=flark_params)
  for after, before in zip(regression_data["after"], boid_data):
    for after_value, before_value in zip(after, before):
      assert_almost_equal(after_value, before_value, delta=0.01)

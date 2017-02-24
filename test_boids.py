import boids
from nose.tools import assert_almost_equal
from nose.tools import assert_greater_equal
from nose.tools import assert_less_equal
import os
import yaml

def test_instantiate_boids():
  my_boids=boids.instantiate_boids()
  boids_x, boids_y, boid_x_velocities, boid_y_velocities = my_boids
  assert_greater_equal(min(boids_x), -450.0, 'x_min failed')
  assert_less_equal(max(boids_x), 50, 'x_max failed')


# test boids move by <= 0.01
def test_bad_boids_regression():
  regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
  boid_data = regression_data["before"]
  boids.update_boids(boid_data)
  for after, before in zip(regression_data["after"], boid_data):
    for after_value, before_value in zip(after, before):
      assert_almost_equal(after_value, before_value, delta=0.01)

**Introduction**
This plots a flock of [50] birds flocking. Flying rules are each bird flys towards the middle of the flock, doesn't
crash into its neighbours and matches the speed of more distant neighbours.

*** Usage: ***

callable from the command line with ./boids.py

Args:

  a config.yml containing 9 space and speed parammeters:
  
  x_min x_max y_min y_max n_boids x_vel_min x_vel_max y_vel_min y_vel_max

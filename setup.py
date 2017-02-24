from setuptools import setup, find_packages

setup(
  name="Boids",
  version="0.1",
  packages=find_packages(exclude=['*test']),
  scripts=['scripts/boids'],
  install_requires=['argparse']
)
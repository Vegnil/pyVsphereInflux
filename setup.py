from setuptools import setup, find_packages
from glob import glob

setup(name='pyVsphereInflux',
      version='0.4',
      description='A library and supporting script for pulling data from vSphere and inserting it into InfluxDB',
      scripts=glob('bin/*'),
      package_dir={'': 'lib'},
      packages=find_packages('lib'),
      install_requires=[
        'pyvmomi',
        'influxdb',
        'pexpect',
      ])
      
# vim: et:ai:sw=4:ts=4

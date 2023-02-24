'''
use `pip install -e .` to enable packages to be imported into tests and other modules
'''

from setuptools import setup, find_packages

setup(name='ORBIT', version='0.2.0', description='Open Source Algorithmic Trading.',
      author='OpenLiquid', packages=find_packages())

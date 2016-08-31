import os
import distutils
from distutils.core import setup, Extension, Command
import numpy

scripts=['wombat-make-scripts']

scripts=[os.path.join('bin',s) for s in scripts]

setup(
    name="wombat", 
    packages=['wombat'],
    scripts=scripts,
    version="0.1",
)





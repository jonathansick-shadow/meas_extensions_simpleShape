from .simpleShapeLib import *
from .version import *   # generated by sconsUtils
from lsst.meas.algorithms.algorithmRegistry import AlgorithmRegistry

AlgorithmRegistry.register("shape.simple", SimpleShapeControl)

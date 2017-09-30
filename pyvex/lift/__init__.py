from ..block import IRSB
from .lifter import Lifter, Postprocessor

lifters = []
postprocessors = []

def register(lifter):
    if issubclass(lifter, Lifter):
        lifters.append(lifter)
    if issubclass(lifter, Postprocessor):
        postprocessors.append(lifter)

from ..errors import PyVEXError

from .libvex import LibVEXLifter
from .fixes import FixesPostProcessor
from .spotter import LifterSpotter

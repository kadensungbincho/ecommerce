from .base import *
# overwritten by
from .production import *

try:
    from .local import *
except:
    pass
    
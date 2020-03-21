from dataclasses import dataclass
from typing import *

@dataclass
class Tree(object):
    rep: object
    children: List[object]
#!/usr/bin/env python3
"""func that call other func"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function returns float of the func inside"""
    def multiplier_function(x: float) -> float:
        """returns x * mul.... in float"""
        return x * multiplier
    return multiplier_function

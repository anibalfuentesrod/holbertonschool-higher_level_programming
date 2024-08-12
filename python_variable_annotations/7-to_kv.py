#!/usr/bin/env python3
"""...smae thing bruh"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """reutrn the a tuple  that takes str and floats"""
    return (k, float(v ** 2))

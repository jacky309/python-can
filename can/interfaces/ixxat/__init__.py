"""
Ctypes wrapper module for IXXAT Virtual CAN Interface V4 on win32 systems

Copyright (C) 2016-2021 Giuseppe Corbelli <giuseppe.corbelli@weightpack.com>
"""

__all__ = [
    "get_ixxat_hwids",
    "IXXATBus",
]

from can.interfaces.ixxat.canlib import IXXATBus

# import this and not the one from vcinpl2 for backward compatibility
from can.interfaces.ixxat.canlib_vcinpl import get_ixxat_hwids

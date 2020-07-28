#
# Copyright (C) 2017-2018 Pico Technology Ltd.
#
from __future__ import print_function
from distutils.core import setup

import ctypes
from ctypes import *
from ctypes.util import find_library
import sys
import os.path


from ctypes import cdll
lib = cdll.LoadLibrary("/Applications/PicoScope 6.app/Contents/Resources/lib/libps5000a.dylib")

signalfile = ".sdkwarning"
if not os.path.exists(signalfile):
    name = 'ps5000'
    try:
        if sys.platform == 'win32':
            result = ctypes.WinDLL(find_library(name))
        else:
            result = cdll.LoadLibrary(find_library(name))
    except OSError:
        print("Please install the PicoSDK in order to use this wrapper."
              "Visit https://www.picotech.com/downloads")
        exit(1)
    open(signalfile, 'a').close()


setup(name='PicoSDK',
      version='1.0',
      description='PicoSDK Python wrapper',
      author='Pico Technology Ltd',
      author_email='support@picotech.com',
      url='https://www.picotech.com',
      packages=['picosdk'])
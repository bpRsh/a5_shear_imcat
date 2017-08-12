#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 27, 2016
# Last update : 
#

# Imports
# Imports
import subprocess
import time

# start time
start_time = time.time()

# current dir
pwd = "./galshear"



commands = " " +\
"cd " + pwd + " ; " +\
"lc -C -n r -n rkappa -n ngals -n gm -n gmerr -n gc -n gcerr < color_mono_galshear_shear.dat > color_mono_galshear_shear.cat ; " +\
"lc -C -n r -n rkappa -n ngals -n em -n emerr -n ec -n ecerr < color_mono_galshear_ellip.dat > color_mono_galshear_ellip.cat " 



print(commands)
print("\nCreating galshear/color_mono_galshear_shear.cat ")
print("Creating galshear/color_mono_galshear_ellip.cat ")
subprocess.call(commands,shell=True)


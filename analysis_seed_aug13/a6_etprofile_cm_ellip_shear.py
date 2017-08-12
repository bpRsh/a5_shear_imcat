#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 27, 2016
# Last update : Oct 03, 2016
#
# Depends     : galshear/galshear_shear.cat
#
# Outputs     : galshear/color_galshear_shear.dat
#             : galshear/monochromatic_galshear_shear.dat
#             : galshear/color_galshear_ellip.dat
#             : galshear/monochromatic_galshear_ellip.dat
#
# Info: This program finds ellipticity profile from galshear/galshear_shear.cat
#       This does not change input file, only creates 4 output files.
#
#
# Imports
import subprocess
import time

# start time
start_time = time.time()

# current dir
pwd = "./galshear"


commands = " " +\
    "cd " + pwd + " ; " +\
    "etprofile -o 849 849 -d 0.1 -r 100 1200 -e cg_avg < galshear_shear.cat | lc -O > color_galshear_shear.dat ; " +\
    "etprofile -o 849 849 -d 0.1 -r 100 1200 -e mg_avg < galshear_shear.cat | lc -O > monochromatic_galshear_shear.dat ;  " +\
    "lc -b +all 'ce_avg = %ce %c9e vadd 0.5 vscale' < galshear_shear.cat | etprofile -o 849 849 -d 0.1 -r 100 1200 -e ce_avg | lc -O > color_galshear_ellip.dat   ; " +\
    "lc -b +all 'me_avg = %me %m9e vadd 0.5 vscale' < galshear_shear.cat | etprofile -o 849 849 -d 0.1 -r 100 1200 -e me_avg | lc -O > monochromatic_galshear_ellip.dat "


print(commands)
print("\nCreating galshear/color_galshear_shear.dat ")
print("Creating galshear/monochromatic_galshear_shear.dat ")
print("Creating galshear/color_galshear_ellip.dat ")
print("Creating galshear/monochromatic_galshear_ellip.dat ")
subprocess.call(commands, shell=True)

# NAME
# etprofile --- calculates tangential alignment profile

# SYNOPSIS
#   etprofile [option...] < catfile > asciifile
#       -o io jo	# origin about which we do profile (2048, 2048)
#       -d dlnr		# log bin size 0.25
#       -r rmin rmax	# min and max radii (200, 2000)
#       -l lossfactor	# multiply e by 1/ lossfactor
#       -e ename	# name for 2-vector ellipticity (e)
#       -x xname	# name for 2-vector spatial coordinate (x)

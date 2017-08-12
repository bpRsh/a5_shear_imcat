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
"etprofile -o 849 849 -d 0.1 -r 100 1200 -e cg_avg < galshear_shear.cat | lc -o > color_galshear_shear.dat ; " +\
"etprofile -o 849 849 -d 0.1 -r 100 1200 -e mg_avg < galshear_shear.cat | lc -o > monochromatic_galshear_shear.dat ;  " +\
"lc -b +all 'me_avg = %me %m9e vadd 0.5 vscale' < galshear_shear.cat | etprofile -o 849 849 -d 0.1 -r 100 1200 -e me_avg | lc -o > monochromatic_galshear_ellip.dat ;  " +\
"lc -b +all 'ce_avg = %ce %c9e vadd 0.5 vscale' < galshear_shear.cat | etprofile -o 849 849 -d 0.1 -r 100 1200 -e ce_avg | lc -o > color_galshear_ellip.dat ; " +\
"lc -b +all 'ce_avg = %ce %c9e vadd 0.5 vscale' < galshear_shear.cat | etprofile -o 849 849 -d 0.1 -r 100 1200 -e ce_avg | lc -O > color_galshear_ellip.dat   ; " +\
"lc -b +all 'me_avg = %me %m9e vadd 0.5 vscale' < galshear_shear.cat | etprofile -o 849 849 -d 0.1 -r 100 1200 -e me_avg | lc -O > monochromatic_galshear_ellip.dat   ; " +\
"etprofile -o 849 849 -d 0.1 -r 100 1200 -e mg_avg < galshear_shear.cat | lc -O > monochromatic_galshear_shear.dat   ; " +\
"etprofile -o 849 849 -d 0.1 -r 100 1200 -e cg_avg < galshear_shear.cat | lc -O > color_galshear_shear.dat " 



print(commands)
print("\nCreating galshear/color_galshear_shear.dat ")
print("Creating galshear/monochromatic_galshear_shear.dat ")
print("Creating galshear/color_galshear_ellip.dat ")
print("Creating galshear/monochromatic_galshear_ellip.dat ")
subprocess.call(commands,shell=True)


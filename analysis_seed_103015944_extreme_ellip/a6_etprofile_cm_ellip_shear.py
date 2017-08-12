#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 27, 2016
# Last update : 
#
# Estimated time: 13 seconds

# Imports
import subprocess
import time

# beginning time
program_begin_time = time.time()
begin_ctime        = time.ctime()


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



# print the time taken
program_end_time = time.time()
end_ctime        = time.ctime()
seconds          = program_end_time - program_begin_time
m, s             = divmod(seconds, 60)
h, m             = divmod(m, 60)
d, h             = divmod(h, 24)
print('\nBegin time: ', begin_ctime)
print('End   time: ', end_ctime,'\n')
print("Time taken: {0:.0f} days, {1:.0f} hours, \
      {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 24, 2016
# Last update : Sep 27, 2016
#
# Depends     : galshear/galshear_cut.cat
#               galshear/galshear_*.par  # 8 par files for monochromatic and colored
#
#              i.e.
#              galshear_c9pg0.par  galshear_cpg0.par   galshear_m9pg0.par  galshear_mpg0.par
#              galshear_c9pg1.par  galshear_cpg1.par   galshear_m9pg1.par  galshear_mpg1.par
#
#              Also, galshear_big_cat and galshear_cut.cat
#
# Outputs    : galshear/galshear_fpg.cat
#              galshear/galshear_shear.cat
#
# Info:
# 1. This program creates fitted P gamma values (i.e. galshear_fpg.cat)
#    from galshear_cut.cat and 8 other par files.
#
# 2. It will also create shear catalog file.
#  
# Estimated time: 9 seconds
#
# Imports
import subprocess
import time

# start time
start_time = time.time()

# current dir
pwd = "./galshear"



##==============================================================================
# create galshear/galshear_fpg.cat
##==============================================================================
commands = "cd " + pwd + " ; " +\
"lc -b +all 'ox = %x' 'x = %rg %e[0] 2 vector' < galshear_cut.cat | gen2Dpolymodel galshear_mpg0.par | gen2Dpolymodel galshear_m9pg0.par | gen2Dpolymodel galshear_cpg0.par | gen2Dpolymodel galshear_c9pg0.par | lc -b +all 'x = %rg %e[1] 2 vector' | gen2Dpolymodel galshear_mpg1.par | gen2Dpolymodel galshear_m9pg1.par | gen2Dpolymodel galshear_cpg1.par | gen2Dpolymodel galshear_c9pg1.par | lc -b +all 'x = %ox' > galshear_fpg.cat "
print("\nCreating galshear/galshear_fpg.cat :\n")
print(commands)
subprocess.call(commands,shell=True)






##==============================================================================
# create galshear/galshear_shear.cat
##==============================================================================
commands = "cd " + pwd + " ; " +\
"lc -b +all 'mg = %me[0] %mPg0mod / %me[1] %mPg1mod / 2 vector' 'm9g = %m9e[0] %m9Pg0mod / %m9e[1] %m9Pg1mod / 2 vector' 'cg = %ce[0] %cPg0mod / %ce[1] %cPg1mod / 2 vector' 'c9g = %c9e[0] %c9Pg0mod / %c9e[1] %c9Pg1mod / 2 vector' < galshear_fpg.cat | lc -b +all 'mg_avg = %mg %m9g vadd 0.5 vscale' 'cg_avg = %cg %c9g vadd 0.5 vscale' > galshear_shear.cat "
print("\nCreating galshear/galshear_shear.cat :\n")
print(commands)
subprocess.call(commands,shell=True)







# print the time taken
end_time = time.time()
seconds  = end_time - start_time
m, s     = divmod(seconds, 60)
h, m     = divmod(m, 60)
d, h     = divmod(h, 24)
print("\nTime taken ==> {:2.0f} days, {:2.0f} hours,\
{:2.0f} minutes, {:f} seconds.".format( d, h, m, s))

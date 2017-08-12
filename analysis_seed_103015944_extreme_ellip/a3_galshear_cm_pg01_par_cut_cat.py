#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 24, 2016
# Last update : Sep 27, 2016
#
# Depends     : galshear/galshear_*.cat 
#
# Outputs     : inside galshear 8 par files:
#              galshear_c9pg0.par  galshear_cpg0.par   galshear_m9pg0.par  galshear_mpg0.par
#              galshear_c9pg1.par  galshear_cpg1.par   galshear_m9pg1.par  galshear_mpg1.par
#
#              Also, galshear_big_cat and galshear_cut.cat
#
# Info:
# 1. This program creates P_gamma values (Pg0 and Pg1)
#    for chromatic and monochromatic fitsfiles. (c,c9,m,m9)
# 
#    The suffix 9 is for 90 degree rotated case.
#
#    In total it creates 2*4 = 8 par files inside galshear,
#    one galshear/galshear_big.cat, and, 
#    one galshear/galshear_cut.cat.
#
#    This means it will create 8 par files and 2 cat files inside galshear.
#  
# Estimated time: 1 min 20 seconds for 130 catalogs.

# Imports
import subprocess
import time

# start time
start_time = time.time()

# current dir
pwd = "./galshear"


# First create galshear/galshear_big.cat
commands= " " +\
"cd " + pwd + " ; " +\
"catcats galshear_[0123456789].cat galshear_[123456789][123456789].cat galshear_1[0123456789][0123456789].cat > galshear_big.cat"

print("\nRunning catcats to get big cat file :\n")
print(commands)
subprocess.call(commands,shell=True)


##==============================================================================
# create galshear_cpg0.par and galshear_cpg1.par  # note: ls*cpg*   rm*cpg* 
##==============================================================================

commands = " " +\
"cd " + pwd + " ; " +\
"lc -c < galshear_big.cat ; " +\
"lc -i '%rg 1.5 > %ce %ce dot 1 < and %me %me dot 1 < and %c9e %c9e dot 1 < and %m9e %m9e dot 1 < and' < galshear_big.cat > galshear_cut.cat ;  " +\
"lc -b +all 'x = %rg %ce[0] 2 vector' 'cPg0 = %cPg[0][0]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 cPg0 > galshear_cpg0.par ;  " +\
"lc -b +all 'x = %rg %ce[1] 2 vector' 'cPg1 = %cPg[1][1]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 cPg1 > galshear_cpg1.par "


print("\nCreating par files for cpg0 and cpg1 :\n")
print(commands)
subprocess.call(commands,shell=True)






##==============================================================================
# create galshear_c9pg0.par and galshear_c9pg1.par  # note: ls*c9pg*   rm*c9pg* 
##==============================================================================

commands = " " +\
"cd " + pwd + " ; " +\
"lc -b +all 'x = %rg %c9e[0] 2 vector' 'c9Pg0 = %c9Pg[0][0]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 c9Pg0 > galshear_c9pg0.par ;  " +\
"lc -b +all 'x = %rg %c9e[1] 2 vector' 'c9Pg1 = %c9Pg[1][1]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 c9Pg1 > galshear_c9pg1.par "


print("\nCreating par files for c9pg0 and c9pg1 :\n")
print(commands)
subprocess.call(commands,shell=True)





##==============================================================================
# create galshear_mpg0.par and galshear_mpg1.par  # note: ls*mpg*   rm*mpg* 
##==============================================================================

commands = " " +\
"cd " + pwd + " ; " +\
"lc -b +all 'x = %rg %me[0] 2 vector' 'mPg0 = %mPg[0][0]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 mPg0 > galshear_mpg0.par ;  " +\
"lc -b +all 'x = %rg %me[1] 2 vector' 'mPg1 = %mPg[1][1]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 mPg1 > galshear_mpg1.par "


print("\nCreating par files for mpg0 and mpg1 :\n")
print(commands)
subprocess.call(commands,shell=True)







##==============================================================================
# create galshear_m9pg0.par and galshear_m9pg1.par  # note: ls*m9pg*   rm*m9pg* 
##==============================================================================

commands = " " +\
"cd " + pwd + " ; " +\
"lc -b +all 'x = %rg %m9e[0] 2 vector' 'm9Pg0 = %m9Pg[0][0]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 m9Pg0 > galshear_m9pg0.par ;  " +\
"lc -b +all 'x = %rg %ce[1] 2 vector' 'm9Pg1 = %m9Pg[1][1]' < galshear_cut.cat | " +\
                 "fit2Dpolymodel2 x 4 1 m9Pg1 > galshear_m9pg1.par "


print("\nCreating par files for m9pg0 and m9pg1 :\n")
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

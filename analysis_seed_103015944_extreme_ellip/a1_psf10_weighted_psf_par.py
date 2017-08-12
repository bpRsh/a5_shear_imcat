#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Douglas Clowe; Associate Professor, Ohio University
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Aug 22, 2016
# Last update : Sep 27, 2016
#
# Inputs      : psf10.fits, weighted_psf.fits
#
# Outputs     : psf10.par, weighted_psf.par
#
#
# Info:
# 1. This program takes in an input fitsfile and creates a parameter file
#    for that file.
#  
# 2. weighted_psf.fits is created from weighted average of 21 normalized psfs
#    in between wavelength weight 1 and 1.2
#    (flux ratio obtained from jedisim/simdatabase)
#    ( ref: ~/jedisim/simdatabase/average_flux_ratio.py) 
#    ( ref: ~/jedisim/weighted_psf.py)
#
# 3. psf10.fits is the unnormalized psf created by phosim. We use this psf
#    to normalize all the 21 unnormalized psfs created by phosim.
#
# 4. psrat is the pixscale ratio
#    from jesisim_config_file:
#    pix_scale=0.03  		# pixel scale used in jedisim
#    final_pix_scale=0.2    # LSST pixscale (arcsecords per pixel)
#
#    psrat = 0.03 / 0.2 = 1.15
#
# Estimated time : 23 seconds

# Imports
from __future__ import print_function
import os
import sys
import subprocess
import time

# start time
start_time = time.time()


##==============================================================================
## for psf10
##==============================================================================
sfile = ' psf10'
psrat = ' ' +  str(0.15)   # ratio of pixscales 0.03/0.2 = 0.15
ffile = ' psf10.fits'
ofile = ' psf10.par'


## do imcat analysis
commands = " " +\
"ic -s 100 '%1 grand .001 * +'" + ffile + " > temp.fits"  + " ;" +\
"hfindpeaks temp.fits -r 0.5 20 | "                    + \
"getsky -Z rg 3 | "                                    + \
"apphot -z 30 | "                                      + \
"lc -b -i '%flux 0 >' | "                              + \
"cleancat 100000 | "                                   + \
"getshapes -s" + psrat + ' ' + "| "                    + \
"lc -b +all 'x = %x %d vadd' | "                       + \
"apphot -z 30 | "                                      + \
"getshapes -s " + ' ' + psrat + "| "                   + \
"lc -b +all 'x = %x %d vadd' | "                       + \
"apphot -z 30 | "                                      + \
"getshapes -s " + psrat + "| "                         + \
"lc -b +all 'x = %x %d vadd' | "                       + \
"apphot -z 30 | "                                      + \
"getshapes -s" + psrat + "| "                          + \
"lc -b +all 'st = %psh[0][0] %psh[0][1] %psh[1][0] "   + \
                  "%psh[1][1] %psm[0][0] %psm[0][1] "  + \
                  "%psm[1][0] %psm[1][1] %e[0] %e[1] " + \
                  "%rg 11 vector' | "                  + \
"fit2Dpolymodel x 0 0 st > " + ofile  + " ;" +\
"rm temp.fits"


# call the commands
print("\nRunning commands :\n")
print('Commands : \n', commands)
print("\n\n")
subprocess.call(commands,shell=True)






##==============================================================================
## for weighted_psf
##==============================================================================

sfile = ' weighted_psf'
psrat = ' ' +  str(0.15)
ffile = ' weighted_psf.fits'
ofile = ' weighted_psf.par'


## do imcat analysis
commands = " " +\
"ic -s 100 '%1 grand .001 * +'" + ffile + " > temp.fits"  + " ;" +\
"hfindpeaks temp.fits -r 0.5 20 | "                    + \
"getsky -Z rg 3 | "                                    + \
"apphot -z 30 | "                                      + \
"lc -b -i '%flux 0 >' | "                              + \
"cleancat 100000 | "                                   + \
"getshapes -s" + psrat + ' ' + "| "                    + \
"lc -b +all 'x = %x %d vadd' | "                       + \
"apphot -z 30 | "                                      + \
"getshapes -s " + ' ' + psrat + "| "                   + \
"lc -b +all 'x = %x %d vadd' | "                       + \
"apphot -z 30 | "                                      + \
"getshapes -s " + psrat + "| "                         + \
"lc -b +all 'x = %x %d vadd' | "                       + \
"apphot -z 30 | "                                      + \
"getshapes -s" + psrat + "| "                          + \
"lc -b +all 'st = %psh[0][0] %psh[0][1] %psh[1][0] "   + \
                  "%psh[1][1] %psm[0][0] %psm[0][1] "  + \
                  "%psm[1][0] %psm[1][1] %e[0] %e[1] " + \
                  "%rg 11 vector' | "                  + \
"fit2Dpolymodel x 0 0 st > " + ofile  + " ;" +\
"rm temp.fits"


# call the commands
print("\nRunning commands :\n")
print('Commands : \n', commands)
print("\n\n")
subprocess.call(commands,shell=True)

# print the time taken
end_time = time.time()
seconds  = end_time - start_time
m, s     = divmod(seconds, 60)
h, m     = divmod(m, 60)
d, h     = divmod(h, 24)
print("\nTime taken ==> {:2.0f} days, {:2.0f} hours,\
{:2.0f} minutes, {:f} seconds.".format( d, h, m, s))

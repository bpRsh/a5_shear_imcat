#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 15, 2016
# Last update : Oct 03, 2016
#
# Depends     : galshear/color_galshear_shear.dat
#               galshear/monochromatic_galshear_shear.dat
#               galshear/color_galshear_ellip.dat
#               galshear/monochromatic_galshear_ellip.dat
#
# Outputs     : galshear/color_mono_galshear_shear.dat
#               galshear/color_mono_galshear_ellip.dat
#
# Info: This program creates a new dat file with only some columns from
#       two input files for color and monochromatic cases. 
#       It does this for shear and ellipticity files.
#
# Imports
import numpy as np
import subprocess,os,sys,shutil




##=======================================================================
## For shear
##=======================================================================

# bin   r   ngals   et  eterror   rkappa   kappa  kappaerror  nu
# 0     1   2       3   4         5        6      7           8      
infile1 = 'galshear/color_galshear_shear.dat'
infile2 = 'galshear/monochromatic_galshear_shear.dat'
r,rkappa,ngals,etmono ,eterrormono  = np.genfromtxt(infile1,delimiter=None,usecols=(1,5,2,3,4),dtype=float,unpack=True)
r,rkappa,ngals,etcolor,eterrorcolor = np.genfromtxt(infile2,delimiter=None,usecols=(1,5,2,3,4),dtype=float,unpack=True)





# write to a file
outfile = 'galshear/color_mono_galshear_shear.dat'
print('Creating : ', outfile)
with open(outfile,'w') as f:

    # write header
    header = '# r       rkappa     ngals   etmono eterrormono etcolor  eterrorcolor '
    print(header,file=f)

    # write data
    for i in range(len(r)):
        print(r[i],rkappa[i],ngals[i],etmono[i],eterrormono[i],etcolor[i],eterrorcolor[i],sep='   ', file=f)
    

# convert dat to cat
outfile = 'galshear/color_mono_galshear_shear.cat'
print('Creating : ', outfile)
cmd = 'lc -C -n r -n rkappa -n ngals -n etmono -n eterrormono -n etcolor -n eterrorcolor < galshear/color_mono_galshear_shear.dat > galshear/color_mono_galshear_shear.cat'
subprocess.call(cmd, shell=True)


##=======================================================================
## For ellipticity
##=======================================================================
infile1 = 'galshear/color_galshear_ellip.dat'
infile2 = 'galshear/monochromatic_galshear_ellip.dat'
r,rkappa,ngals,etmono,eterrormono = np.genfromtxt(infile1,delimiter=None,usecols=(1,5,2,3,4),dtype=float,unpack=True)
r,rkappa,ngals,etcolor,eterrorcolor = np.genfromtxt(infile2,delimiter=None,usecols=(1,5,2,3,4),dtype=float,unpack=True)





# write to a file
outfile = 'galshear/color_mono_galshear_ellip.dat'
print('\nCreating : ', outfile)
with open(outfile,'w') as f:

    # write header
    header = '# r       rkappa     ngals   etmono eterrormono etcolor  eterrorcolor '
    print(header,file=f)

    # write data
    for i in range(len(r)):
        print(r[i],rkappa[i],ngals[i],etmono[i],eterrormono[i],etcolor[i],eterrorcolor[i],sep='   ', file=f)


# convert dat to cat
outfile = 'galshear/color_mono_galshear_ellip.cat'
print('Creating : ', outfile)
cmd = 'lc -C -n r -n rkappa -n ngals -n etmono -n eterrormono -n etcolor -n eterrorcolor < galshear/color_mono_galshear_ellip.dat > galshear/color_mono_galshear_ellip.cat'
subprocess.call(cmd, shell=True)

# checking
#commands = '''
#geany galshear/color_galshear_shear.dat
#geany galshear/color_mono_galshear_shear.dat
#galshear/color_mono_galshear_ellip.cat
#'''

#subprocess.call(commands,shell=True)

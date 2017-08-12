#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 27, 2016
# Last update : Oct 17, 2016
#

# Imports
import subprocess


# input catalogs
incat1 = 'galshear/color_mono_galshear_shear.cat'
incat2 = 'galshear/color_mono_galshear_ellip.cat'


## plots for shear analysis
command1 = "plotcat r gm -w 3                       -T 'shear analysis for default' "       + " -d 'images/r_gm_shear1.ps/ps' "    + " <  " + incat1
command2 = "plotcat r gc -w 3                       -T 'shear analysis for default' "       + " -d 'images/r_gc_shear1.ps/ps' "    + " <  " + incat1
command3 = "plotcat r 'erat = %gc %gm - %gm /' -w 3 -T 'shear analysis for default' "       + " -d 'images/r_erat_shear1.ps/ps' "  + " <  " + incat1

# plots for ellipticity analysis
command4 = "plotcat r em -w 3                       -T 'ellipticity analysis for default' " + " -d 'images/r_em_ellip1.ps/ps' "    + " <  " + incat2
command5 = "plotcat r 'erat = %ec %em /' -w 3       -T 'ellipticity analysis for default' " + " -d 'images/r_erat_ellip1.ps/ps' "  + " <  " + incat2
command6 = "plotcat r 'erat = %ec %em - %em /' -w 3 -T 'ellipticity analysis for default' " + " -d 'images/r_erat_ellipp1.ps/ps' " + " <  " + incat2


# commands to plot
commands = [command1, command2, command3, command4, command5, command6]
for cmd in commands:
    subprocess.call(cmd,shell=True)

print('ps files created inside the directory: images')

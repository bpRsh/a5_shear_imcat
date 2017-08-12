#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Sep 27, 2016
# Last update : 
#

# Imports
import subprocess
import time


# current dir
pwd = "/Users/poudel/Research/outlier_rh_analysis/galshear"


# plot
commands = "cd " + pwd + " ; " + "plotcat r em < color_mono_galshear_ellip.cat "
subprocess.call(commands,shell=True)



# plot
commands = "cd " + pwd + " ; " + "plotcat r gm < color_mono_galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)



# plot
commands = "cd " + pwd + " ; " + "plotcat r gc < color_mono_galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)



# plot
commands = "cd " + pwd + " ; " + "plotcat r 'erat = %ec %em /' < color_mono_galshear_ellip.cat   "
subprocess.call(commands,shell=True)
time.sleep(1.0)


# plot
commands = "cd " + pwd + " ; " + "plotcat r 'erat = %ec %em - %em /' < color_mono_galshear_ellip.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)


# plot
commands = "cd " + pwd + " ; " + "plotcat r 'erat = %gc %gm - %gm /' < color_mono_galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)


# plot
commands = "cd " + pwd + " ; " + "plotcat r gc < color_mono_galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)

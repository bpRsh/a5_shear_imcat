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
pwd = "./galshear"


# plot
commands = "cd " + pwd + " ; " + "plotcat rg mPg0mod < galshear_shear.cat "
subprocess.call(commands,shell=True)



# plot
commands = "cd " + pwd + " ; " + "plotcat rg mPg1mod < galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)



# plot
commands = "cd " + pwd + " ; " + "plotcat rg m9Pg0mod < galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)



# plot
commands = "cd " + pwd + " ; " + "plotcat rg m9Pg1mod < galshear_shear.cat  "
subprocess.call(commands,shell=True)
time.sleep(1.0)


# plot
commands = "cd " + pwd + " ; " + "plotcat rg c9Pg1mod < galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)


# plot
commands = "cd " + pwd + " ; " + "plotcat rg c9Pg0mod < galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)


# plot
commands = "cd " + pwd + " ; " + "plotcat rg cPg0mod < galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)


# plot
commands = "cd " + pwd + " ; " + "plotcat rg cPg1mod < galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)

# plot
commands = "cd " + pwd + " ; " + "plotcat rg m9Pg1mod < galshear_shear.cat "
subprocess.call(commands,shell=True)
time.sleep(1.0)

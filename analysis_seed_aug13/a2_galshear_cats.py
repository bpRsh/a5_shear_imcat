#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author      : Douglas Clowe; Associate Professor, Ohio University
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 22, 2016
# Last update : Oct 17, 2016
#
# Inputs      : All jedisim_output fitsfiles
#               psf10.par
#               weighted_psf.par
#                                 
# Outputs     : galshear/galshear_*.cat
#
# Info:
# 1. This runs imcat command on all the jedisim output files.
#    It reads a. lsst_*.fits
#             b. 90_lsst_*.fits
#             c. monochromatic_*.fits
#             d. 90_monochromatic_*.fits
#
#    from the input directory,
#
#    And, also reads two paramters files: a. psf10.par
#                                         b. weighted_psf.par
#    from the current directory.
#    Then it create catalogs inside galshear e.g. galshear_100.cat.
#
#
# 2. The parameter files are created using a1_psf10_weighted_psf_par.py.
#
# 3. The weights are obtained by the average flux ratio of one hundred 
#    f606 and f814 galaxies. ( refer: ~/jedisim/simdatabase/average_flux_ratio.py)
#    We got weight range 1.0 to 1.2.
#    Then, ~/jedisim/weighted_psf.py gives the weighted_psf.fits.
#    Then, a1_psf10_weighted_psf_par.py gives weighted_psf.par and psf10.par.
#    To run weighted psf we need 21 normalized psf (phosim gives unnormalized
#    psf and we normalize them after using a6_normalize_phosim_psf.py)
#    
#
# 4. The psf 10 is chosen as the middle of 21 normalized psf, created by 
#    Phosim software for narrowband_10.icat and narrowband_10.sed for given seed.
#    The Phosim gives unnormalized psf and we normalize all the psf using
#    ~/Research/psf_creation/a6_normalize_phosim_psf.py so that sum of all
#    the pixels in these psf are equal to that of psf10.fits.
#    Note that, psf10.fits is same for normalized and unnormalized cases.
#
# Estimated time: 8 min 9 seconds for 109 loops.

# Imports
import subprocess
import os          
import time
import shutil
import re

# beginning time
program_begin_time = time.time()
begin_ctime        = time.ctime()
print('Begin time: ', begin_ctime)


# input/output folder
indir  = '~/jedisim_all_outputs/jedisim_output_seed_aug13'
outdir = 'galshear/'  # do not overwrite this folder!



##=============================================================
## 0 to last file + 1
for i in range(0,101):

    out_cat_file = outdir + 'galshear_{:d}'.format(i)
    print('{} {} {}'.format('\nCreating the cat file :',out_cat_file, '.cat'))


    # commands to run
    # chromatic files
    cfile    = indir + "/" + "lsst_{:d}.fits".format(i)               
    c9file   = indir + "/" + "90_lsst_{:d}.fits".format(i)               
    cparfile = 'weighted_psf.par'

    # monochromatic files    
    mfile    = indir + "/" + "monochromatic_{:d}.fits".format(i)               
    m9file   = indir + "/" + "90_monochromatic_{:d}.fits".format(i)    
    mparfile = 'psf10.par'

    # output files
    ofile    = outdir + 'galshear_{:d}.cat'.format(i)

    # command to run
    commands = "hfindpeaks " + cfile + " -r 0.5 20 | "                                  + \
    "getsky -Z rg 3 | "                                                                 + \
    "apphot -z 30 -M 30 | "                                                             + \
    "getshapes | "                                                                      + \
    "lc -b +all 'ox = %x' | "                                                           + \
    "cleancat 5 |  "                                                                    + \
    "apphot -z 30 -M 30 | "                                                             + \
    "getshapes | "                                                                      + \
    "lc -b +all 'x = %x %d vadd' |  "                                                   + \
    "apphot -z 30 -M 30 | "                                                             + \
    "getshapes | "                                                                      + \
    "lc -b +all 'x = %x %d vadd' |  "                                                   + \
    "apphot -z 30 -M 30 | "                                                             + \
    "getshapes | "                                                                      + \
    "lc +all 'dx = %x %ox vsub' | "                                                     + \
    "gen2Dpolymodel " + cparfile + " | "                                                + \
    "lc -b +all 'Pg = %psh %psm %stmod[0] %stmod[1] 2 vector "                          + \
                      "%stmod[2] %stmod[3] 2 vector 2 vector "                          + \
                      "%stmod[4] %stmod[5] 2 vector %stmod[6] "                         + \
                      "%stmod[7] 2 vector 2 vector inverse dot "                        + \
                      "dot msub' 'e = %e %psm %stmod[4] "                               + \
    "%stmod[5] 2 vector %stmod[6] "                                                     + \
    "%stmod[7] 2 vector 2 vector inverse dot "                                          + \
    "%stmod[8] %stmod[9] 2 vector dot vsub' | "                                         + \
    "lc -b +all 'ce = %e' 'cPg = %Pg' 'cmag = %mag' | "                                 + \
    "apphot -z 30 -M 30 -f " + c9file + " | "                                           + \
    "getshapes -f  "+ c9file + " | "                                                    + \
    "lc -b +all 'Pg = %psh %psm %stmod[0] %stmod[1] 2 vector %stmod[2] "                + \
                      "%stmod[3] 2 vector 2 vector %stmod[4] "                          + \
                      "%stmod[5] 2 vector %stmod[6] "                                   + \
                      "%stmod[7] 2 vector 2 vector inverse dot dot "                    + \
                      "msub' 'e = %e %psm %stmod[4] %stmod[5] 2 vector "                + \
                      "%stmod[6] %stmod[7] 2 vector 2 vector inverse dot "              + \
                      "%stmod[8] %stmod[9] 2 vector dot vsub' | "                       + \
    "lc -b +all 'c9e = %e' 'c9Pg = %Pg' 'c9mag = %mag' | "                              + \
    "apphot -z 30 -M 30 -f " + mfile + " | "                                            + \
    "getshapes -f "+ mfile + " | "                                                      + \
    "gen2Dpolymodel " + mparfile + " | "                                                + \
    "lc -b +all 'Pg = %psh %psm %stmod[0] %stmod[1] 2 vector %stmod[2] "                + \
                      "%stmod[3] 2 vector 2 vector %stmod[4] "                          + \
                      "%stmod[5] 2 vector %stmod[6] "                                   + \
                      "%stmod[7] 2 vector 2 vector inverse dot dot msub' 'e = %e %psm " + \
                      "%stmod[4] %stmod[5] 2 vector %stmod[6] "                         + \
                      "%stmod[7] 2 vector 2 vector inverse dot %stmod[8] "              + \
                      "%stmod[9] 2 vector dot vsub' | "                                 + \
    "lc -b +all 'me = %e' 'mPg = %Pg' 'mmag = %mag' | "                                 + \
    "apphot -z 30 -M 30 -f " + m9file + "| "                                            + \
    "getshapes -f " + m9file + " | "                                                    + \
    "lc -b +all 'Pg = %psh %psm %stmod[0] %stmod[1] 2 vector %stmod[2] "                + \
                      "%stmod[3] 2 vector 2 vector %stmod[4] "                          + \
                      "%stmod[5] 2 vector %stmod[6] "                                   + \
                      "%stmod[7] 2 vector 2 vector inverse dot dot msub' 'e = %e %psm " + \
                      "%stmod[4] %stmod[5] 2 vector %stmod[6] "                         + \
                      "%stmod[7] 2 vector 2 vector inverse dot %stmod[8] "              + \
                      "%stmod[9] 2 vector dot vsub' | "                                 + \
    "lc -b +all 'm9e = %e' 'm9Pg = %Pg' 'm9mag = %mag' > "                              + \
    ofile


    # run the program
    subprocess.call(commands,shell=True)
##=============================================================================



    

# print the time taken
program_end_time = time.time()
end_ctime        = time.ctime()
seconds          = program_end_time - program_begin_time
m, s             = divmod(seconds, 60)
h, m             = divmod(m, 60)
d, h             = divmod(h, 24)
print('Begin time: ', begin_ctime)
print('End   time: ', end_ctime,'\n')
print("Time taken: {0:.0f} days, {1:.0f} hours, \
      {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

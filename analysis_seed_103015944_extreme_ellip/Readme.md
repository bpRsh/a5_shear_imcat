#### Topic     : Shear Analysis of Galaxies


#### Author    : Bhishan Poudel
#### Date      : Oct 12, 2016
### Last update: 

## 1. Create par files for psf10.fits and weighted_psf.fits

Program : a1_par_psf10_weighted.py  

Inputs  : psf10.fits, weighted_psf.fits  

Outputs : psf10.par, weighted_psf.par  

This program creates the parameter file for given input fisfiles, viz., 
psf10.fits and weighted_psf.fits.

The par files have THREE vectors: l,m, and st  , st has 11 components
The input psf files psf10.fits and weighted_psf.fits are obtained from
jedisim directory. The later is obtained using weighed_psf.py in that
folder.



## 2. Use par files to obtain cat files for all JEDISIM output fitsfiles

Program : a2_galshear_cats.py

Inputs  : ~/jedisim/jedisim_output/jedisim_output_all_normalized_psf/*.fits
          e.g. lsst_0.fits, 90_lsst_0.fits,   
          e.g. monochromatic_0.fits, 90_monochromataic_0.fits
           
Outputs : galshear/*.cat  
          e.g. galshear_0.cat  (upto maybe galshear_105.cat)  
          
This program uses the parameters files psf10.par and weighted_psf.par 
to obtain the catalogs files for all the fitsfiles created by JEDISIM.

Variables in galshear/galshear_0.cat are following:   
x,lg,rg,eg,fs,nu,fb0,dfb,flux,mag,rh,rp,rql,  
rqu,nbad,fmax,e,psm,psh,d,ox,stmod,Pg,ce,cPg,  
cmag,c9e,c9Pg,c9mag,me,mPg,mmag,m9e,m9Pg,m9mag  
 


## 3. Combine separate cat files and create par files for Pg0 and Pg1 for c,c9,m,m9  

Program : a3_galshear_cm_pg01_par_cut_cat.py

Depends : galshear/galshear_*.cat    
            e.g. galshear_0.cat, galshear_49.cat    
          
Outputs : galshear/galshear_c9pg0.par, etc  (2*4 = 8 parameter files)
          galshear/galshear_big.cat
          galshear/galshear_cut.cat
          
This program combines all the cat files for jedisim_fitsfiles.    
Then, combines them to create galshear_big.cat .    
Then, it creates par files for Pg values (Pg0, and Pg1) for variables 
c,c9, m, m9 . It also create galshear_cut.cat. 

Here, suffix 9 is for 90 degree rotated case.  
cfile is lsst.fits file       (i.e. chromatic files).      
mfile is monochormatic.fits   (i.e. monochromatic files).      


## 4. Create par files for fitted P-gamma vand galaxy shear value

Program : a4_galshear_fpg_shear_cat.py 

Depends : galshear/galshear_cut.cat   
	  galshear/galshear_*.par  # 8 par files for c,c9,m,m9 monochromatic and colored
          
Info:
1. This program creates fitted P gamma values (i.e. galshear_fpg.cat)
    from galshear_cut.cat and 8 other par files.

2. It will also create shear catalog file. 

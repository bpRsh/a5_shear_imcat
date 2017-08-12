#!/usr/bin/perl
$doproc = 1;
$sfile = shift @ARGV;
$psrat = shift @ARGV;
$ffile = $sfile.".fits";
$ofile = $sfile.".par";
    
&esystem("ic -s 100 '%1 grand .001 * +' $ffile > temp.fits");
&esystem("hfindpeaks temp.fits -r 0.5 20 | getsky -Z rg 3 | apphot -z 30 | lc -b -i '%flux 0 >' | cleancat 100000 | getshapes -s $psrat | lc -b +all 'x = %x %d vadd' | apphot -z 30 | getshapes -s $psrat | lc -b +all 'x = %x %d vadd' | apphot -z 30 | getshapes -s $psrat | lc -b +all 'x = %x %d vadd' | apphot -z 30 | getshapes -s $psrat | lc -b +all 'st = %psh[0][0] %psh[0][1] %psh[1][0] %psh[1][1] %psm[0][0] %psm[0][1] %psm[1][0] %psm[1][1] %e[0] %e[1] %rg 11 vector' | fit2Dpolymodel x 0 0 st > $ofile");
&esystem("rm temp.fits");

sub esystem{
    print "$_[0]\n";
    if ($doproc) {
        system($_[0]);
    }
}

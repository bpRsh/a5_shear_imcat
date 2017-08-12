#!/usr/bin/perl
$doproc = 1;
$dir = shift @ARGV;
$mnum = shift @ARGV;
$max = shift @ARGV;
for($i = $mnum; $i <= $max; $i = $i + 1) {
    $cfile = $dir."/lsst/lsst_".$i.".fits";
    $c90file = $dir."/90_lsst/90_lsst_".$i.".fits";
    $mfile = $dir."/monochromatic/monochromatic_".$i.".fits";
    $m90file = $dir."/90_monochromatic/90_monochromatic_".$i.".fits";
    $cpsf = "weighted_psf.par";
    $mpsf = "psf10.par";
    $ofile = $dir."/galshear_".$i.".cat";
    &esystem("perl galshear.pl $cfile $c90file $cpsf $mfile $m90file $mpsf $ofile");
}

sub esystem{
    print "$_[0]\n";
    if ($doproc) {
        system($_[0]);
    }
}

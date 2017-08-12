#!/usr/bin/perl
$doproc = 1;
$cfile = shift @ARGV;
$c9file = shift @ARGV;
$cparfile = shift @ARGV;
$mfile = shift @ARGV;
$m9file = shift @ARGV;
$mparfile = shift @ARGV;
$ofile = shift @ARGV;

&esystem("hfindpeaks $cfile -r 0.5 20 | getsky -Z rg 3 | apphot -z 30 -M 30 | getshapes | lc -b +all 'ox = %x' | cleancat 5 |  apphot -z 30 -M 30 | getshapes | lc -b +all 'x = %x %d vadd' |  apphot -z 30 -M 30 | getshapes | lc -b +all 'x = %x %d vadd' |  apphot -z 30 -M 30 | getshapes | lc +all 'dx = %x %ox vsub' | gen2Dpolymodel $cparfile | lc -b +all 'Pg = %psh %psm %stmod[0] %stmod[1] 2 vector %stmod[2] %stmod[3] 2 vector 2 vector %stmod[4] %stmod[5] 2 vector %stmod[6] %stmod[7] 2 vector 2 vector inverse dot dot msub' 'e = %e %psm %stmod[4] %stmod[5] 2 vector %stmod[6] %stmod[7] 2 vector 2 vector inverse dot %stmod[8] %stmod[9] 2 vector dot vsub' | lc -b +all 'ce = %e' 'cPg = %Pg' 'cmag = %mag' | apphot -z 30 -M 30 -f $c9file | getshapes -f $c9file | lc -b +all 'Pg = %psh %psm %stmod[0] %stmod[1] 2 vector %stmod[2] %stmod[3] 2 vector 2 vector %stmod[4] %stmod[5] 2 vector %stmod[6] %stmod[7] 2 vector 2 vector inverse dot dot msub' 'e = %e %psm %stmod[4] %stmod[5] 2 vector %stmod[6] %stmod[7] 2 vector 2 vector inverse dot %stmod[8] %stmod[9] 2 vector dot vsub' | apphot -z 30 -M 30 -f $mfile | getshapes -f $mfile | gen2Dpolymodel $mparfile | lc -b +all 'Pg = %psh %psm %stmod[0] %stmod[1] 2 vector %stmod[2] %stmod[3] 2 vector 2 vector %stmod[4] %stmod[5] 2 vector %stmod[6] %stmod[7] 2 vector 2 vector inverse dot dot msub' 'e = %e %psm %stmod[4] %stmod[5] 2 vector %stmod[6] %stmod[7] 2 vector 2 vector inverse dot %stmod[8] %stmod[9] 2 vector dot vsub' | lc -b +all 'me = %e' 'mPg = %Pg' 'mmag = %mag' | apphot -z 30 -M 30 -f $m9file | getshapes -f $m9file | lc -b +all 'Pg = %psh %psm %stmod[0] %stmod[1] 2 vector %stmod[2] %stmod[3] 2 vector 2 vector %stmod[4] %stmod[5] 2 vector %stmod[6] %stmod[7] 2 vector 2 vector inverse dot dot msub' 'e = %e %psm %stmod[4] %stmod[5] 2 vector %stmod[6] %stmod[7] 2 vector 2 vector inverse dot %stmod[8] %stmod[9] 2 vector dot vsub' | lc -b +all 'm9e = %e' 'm9Pg = %Pg' 'm9mag = %mag' > $ofile");

sub esystem{
    print "$_[0]\n";
    if ($doproc) {
        system($_[0]);
    }
}

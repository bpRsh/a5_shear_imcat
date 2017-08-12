CC=gcc
CFLAGS=-O3 -Wall
LIBS=-I/usr/local/include -I/usr/include -I /Users/poudel/Applications/cfitsio/include  -L /Users/poudel/Applications/cfitsio/lib -lm -lcfitsio


# execute program and clean it
default: im
	echo " compilation finished ... "




im :  imcopy imarith imstat

imcopy :
	gcc -Wall -O3 cexamples/imcopy.c -o cexamples/imcopy $(LIBS)

imarith :
	gcc -Wall -O3 cexamples/imarith.c -o cexamples/imarith $(LIBS)

imstat :
	gcc -Wall -O3 cexamples/imstat.c -o cexamples/imstat $(LIBS) 


# Utility targets
.PHONY: clean

clean:
	rm -rf cexamples/imcopy
	rm -rf cexamples/imarith
	rm -rf cexamples/imstat

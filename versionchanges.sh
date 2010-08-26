#!/bin/bash
PREV_VERSION_DIR=/usr/share/fonts/truetype/ttf-sil-padauk
for font in Padauk.ttf Padauk-Bold.ttf;
do
	LOG_FILE=versionchanges`basename $font .ttf`.txt
	CHECK_FILE=versionchangetext`basename $font .ttf`.txt
	rm -rf $LOG_FILE
	echo $font
	for test in test-suite/*.txt;
	do
		echo $test
		echo $test >> $LOG_FILE
		comparerenderer -f $font -a $PREV_VERSION_DIR/$font -s 12 -t $test -n -c --ignore-gid --tolerance 3.0>> $LOG_FILE
		comparerenderer -f $font -a $PREV_VERSION_DIR/$font -s 12 -t $test -h -c --ignore-gid --tolerance 3.0 >> $LOG_FILE
	done
	perl -CIO -e 'while ($l=<STDIN>) { if ($l=~/[\x{1000}-\x{109F}\x{aa60}-\x{aa7f}]/) {print $l;} }' < $LOG_FILE > $CHECK_FILE
done


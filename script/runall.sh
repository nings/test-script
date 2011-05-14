#!/bin/sh
#echo "Nightly Run Successful: $(date)" >> /media/bak/testbed/script/tmp/mybackup.log
#scerun.jar /media/temp/work1/9/scenario.xml

for((i = 1 ; $i <= 3 ; i++)); do
#  time startsce.sh /media/temp/work1/$i/scenario.xml
	time scerun.jar /media/file/work514/$i/scenario.xml
done

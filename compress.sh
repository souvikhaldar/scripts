#!/bin/sh
pigz --help &>/dev/null
if [ $? -eq 0 ]
then 
	echo "pigz present"
else
	echo "pigz not present"
	exit
fi


tar --help &>/dev/null
if [ $? -eq 0 ]
then 
	echo "tar present"
else
	echo "tar not present"
	exit
fi

if [ -z "$1" ]
then 
	echo "No directory provided, please provide directory to compress by compress.sh <dir-name>"
else
	echo "Compressing directory: " $1
fi

echo "Compressed file: $1_compressed.tar.gz"

tar -cf - $1 | pigz --best >  $1_compressed.tar.gz

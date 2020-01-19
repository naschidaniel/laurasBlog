#!/bin/bash
#$ -cwd
#$ -M daniel@naschi.at

d=`date +%Y-%m-%d`

# - Starting the job here
cd ~/dev/laurasBlog/

conda env list 

echo "conda env export"

conda env export > ~/dev/laurasBlog/docker/web/laurasBlog.yml --name laurasBlog

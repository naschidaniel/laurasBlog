#!/bin/bash
#$ -cwd
#$ -M daniel@naschi.at

d=`date +%Y-%m-%d`

# - Starting the job here
cd ~/dev/djangoVue/

conda env list 

echo "conda env export"

conda env export > ~/dev/djangoVue/docker/web/djangoVue.yml --name djangoVue

#!/bin/bash

source set_env.sh

echo "${COLOR_START}- Lunching ------------------------------------------------------------${COLOR_END}"
echo ""

python Failed_jobs_finder.py

echo ""
echo "- Operation finished --------------------------------------------------"

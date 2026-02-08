#!/bin/bash

# Remote top directory containing list.txt
JOBS_TOPDIR="/pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/GEM21_11a_00_000/2070MeV_Q2_0_02"
export JOBS_TOPDIR

TXT_FILE="${JOBS_TOPDIR}/list.txt"
XML_FILE="${JOBS_TOPDIR}/grid_submission.xml"

#if [[ ! -d "$DEST_DIR" ]]; then
#  echo "Error: destination directory does not exist: $DEST_DIR" >&2
#  exit 2
#fi

# NOTE: Generate the list file on the remote side inside "$JOBS_TOPDIR" first, e.g.:
#           rm list.txt ; ls master-routine_validation_01-eScattering > list.txt
#       In JOBS_TOPDIR
sscpg1 "$TXT_FILE"
sscpg1 "$XML_FILE"

#!/bin/bash

#source local_download.sh

source ./scripts/update_script.sh

# Remote top directory containing list.txt
export PyDir="/pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/GEM21_11a_00_000/2070MeV_Q2_0_02"
Check_if_dir_exist "${PyDir}"

ls ${PyDir}/master-routine_validation_01-eScattering > ${PyDir}/list.txt
export TXT_FILE="${PyDir}/list.txt"
Check_if_dir_exist "${TXT_FILE}"

export XML_FILE="${PyDir}/grid_submission.xml"
Check_if_dir_exist "${TXT_FILE}"

source ./scripts/execute_python_script.sh

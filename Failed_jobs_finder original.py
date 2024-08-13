import os


def find_unmatched_scripts(prefix, input_txt, output_txt, false=None):
    PrinOut = false

    # Initialize the lists
    gst_root_files = []
    sh_files = []

    # Read the input .txt file
    with open(input_txt, 'r') as file:
        for line in file:
            line = line.strip()
            if line.endswith('.gst.root'):
                gst_root_files.append(line)
            elif line.endswith('.sh'):
                sh_files.append(line)

    print("Number of '.gst.root' files: " + str(len(gst_root_files)))
    print("Number of '.sh' files: " + str(len(sh_files)))

    print("\n")

    # List to store unmatched .sh files
    unmatched_sh_files = []

    # Check for unmatched .sh files
    for sh_file in sh_files:
        matched = False
        sh_file_base_name = os.path.splitext(sh_file)[0]

        if PrinOut:
            print(sh_file_base_name)

        for gst_file in gst_root_files:
            gst_file_base_name0 = os.path.splitext(gst_file)[0]
            gst_file_base_name = os.path.splitext(gst_file_base_name0)[0]

            if PrinOut:
                print(gst_file_base_name)

            if sh_file_base_name == gst_file_base_name:
                matched = True
                break
        if not matched:
            unmatched_sh_files.append(sh_file)

    # Write unmatched .sh files to the output .txt file
    with open(output_txt, 'w') as file:
        file.write('<parallel>\n')
        for sh_file in unmatched_sh_files:
            file.write(prefix + sh_file + '\n')
        file.write('</parallel>\n')

    print("Expected Number of '.gst.root' and '.sh' files: " + str(len(sh_files) * 2))
    print("Number of unmatched '.sh' files: " + str(len(unmatched_sh_files)))


if __name__ == "__main__":
    ## 2 GeV prefix
    prefix = "jobsub_submit  -n --memory=2GB --disk=2GB --expected-lifetime=4h  --lines '+FERMIHTC_AutoRelease=True' -f /pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/207052MeV//setup_FNAL.sh -f /pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/207052MeV//setup_GENIE.sh --lines '+FERMIHTC_GraceMemory=4096' --lines '+FERMIHTC_GraceLifetime=6000' --mail_on_error --singularity-image /cvmfs/singularity.opensciencegrid.org/fermilab/fnal-wn-sl7:latest  file:///pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/207052MeV//master-routine_validation_01-eScattering/"
    ## 4 GeV prefix
    # prefix = "jobsub_submit  -n --memory=2GB --disk=2GB --expected-lifetime=4h  --lines '+FERMIHTC_AutoRelease=True' -f /pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/402962MeV//setup_FNAL.sh -f /pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/402962MeV//setup_GENIE.sh --lines '+FERMIHTC_GraceMemory=4096' --lines '+FERMIHTC_GraceLifetime=6000' --mail_on_error --singularity-image /cvmfs/singularity.opensciencegrid.org/fermilab/fnal-wn-sl7:latest  file:///pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/402962MeV//master-routine_validation_01-eScattering/"
    ## 6 GeV prefix
    # prefix = "jobsub_submit  -n --memory=2GB --disk=2GB --expected-lifetime=4h  --lines '+FERMIHTC_AutoRelease=True' -f /pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/598636MeV//setup_FNAL.sh -f /pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/598636MeV//setup_GENIE.sh --lines '+FERMIHTC_GraceMemory=4096' --lines '+FERMIHTC_GraceLifetime=6000' --mail_on_error --singularity-image /cvmfs/singularity.opensciencegrid.org/fermilab/fnal-wn-sl7:latest  file:///pnfs/genie/scratch/users/asportes/2N_Analysis_Samples/Ar40/G18_10a_00_000/598636MeV//master-routine_validation_01-eScattering/"

    input_txt = "input.txt"  # List of files in master-routine_validation_01-eScattering
    output_txt = "grid_submission.xml"  # output .xml file
    find_unmatched_scripts(prefix, input_txt, output_txt)
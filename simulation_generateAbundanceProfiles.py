
#python3 ./simulation_generateAbundanceProfiles.py  ~/workspace/data/simulation/close/simulation_input.txt ~/workspace/data/simulation/close/ab.csv 1 2 100
#python3 ./simulation_generateAbundanceProfiles.py  ~/workspace/data/overlap_test/genome_562_50x/simulation_input.txt ~/workspace/data/overlap_test/genome_562_50x/low_cov/ab.csv 1 1 20

import os, glob, random, sys, argparse


import numpy as np
from numpy.random import RandomState


def main(argv):
    
    parser = argparse.ArgumentParser()

    parser.add_argument("inputStrains", help="File with one genome filename per line")
    parser.add_argument("outputFilename", help="Filename of output abundance table")
    parser.add_argument("nbDatasets", help="")
    parser.add_argument("nbStrains", help="")
    parser.add_argument("maxCoverage", help="")
    
    
    args = parser.parse_args()

    inputStrainsFilename = args.inputStrains
    outputFilename = os.path.abspath(args.outputFilename)
    nbDatasets = int(args.nbDatasets)
    nbStrains = int(args.nbStrains)
    maxCoverage = int(args.maxCoverage)

    strain_filenames = []
    for line in open(inputStrainsFilename):
        line = line.rstrip()
        if not os.path.exists(line):
            print("File not found: ", line)
            exit(1)

        strain_filenames.append(line)

    outputDir = os.path.dirname(outputFilename)
    if not os.path.exists(outputDir): os.makedirs(outputDir)

    create_abundance_profiles(strain_filenames, nbDatasets, nbStrains, maxCoverage, outputFilename)

    print("\nOutput filename: ", outputFilename)



def create_abundance_profiles(strain_filenames, nbDatasets, nb_strains, maxCoverage, outputFilename):

    np.set_printoptions(suppress=True)
    vals = []
    #for i in range(0, nb_strains):
    #    vals.append(0.2+random.random()-0.2)
    #print(vals)
    s = np.random.dirichlet([1]*nb_strains, nbDatasets)#.transpose()
    print(s*maxCoverage)

    file_abundanceProfile = open(outputFilename, "w")
    file_abundanceProfile.write("Dataset;Strain;Abundance\n")

    #strain_filenames = glob.glob(os.path.join(strainsDir, "*.fna"))
    #print(strain_filenames)
    #strain_filenames.sort()
    #print(strain_filenames)

    for dataset_ID in range(0, nbDatasets):

        i = 0
        for strain_filename in strain_filenames:
            if i >= nb_strains: break

            #strain_abundance = random.random() * max_strain_abundance
            #strain_abundance =  1 + dataset_ID * 5 #to remove
            #strain_abundance = 30*(i+1) #random.random()*10 #(1-np.random.power(5))*20
            #strain_abundance = round(strain_abundance, 1)
            #strain_abundance = s[dataset_ID][i] * maxCoverage #100*(i+1) #s[dataset_ID][i] * 100
            strain_abundance = s[dataset_ID][i] * maxCoverage #100*(i+1) #s[dataset_ID][i] * 100

            file_abundanceProfile.write(str(dataset_ID) + ";" + strain_filename + ";" + str(strain_abundance) + "\n")

            i += 1

    file_abundanceProfile.close()



if __name__ == "__main__":
    main(sys.argv[1:])  

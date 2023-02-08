Long-read simulator for HiFi metagenomics.


Create a root directory for the simulated data.

```
mkdir /path/to/rootDir
```

Inside this folder, create a file listing the genome filenames used in the simulation (one genome per line).

```
input_simulation.txt:

/path/to/genomes/GCF_004792595.1_ASM479259v1_genomic.fna
/path/to/genomes/GCF_004792635.1_ASM479263v1_genomic.fna
/path/to/genomes/GCF_900478175.1_33787_E01_genomic.fna
```

Generate a coverage profile across multiple samples.

```
python3 ./simulation_generateAbundanceProfiles.py rootDir/input_simulation.txt rootDir/coverageProfiles.csv nbDatasets nbGenomes maxCoverage
```

This will generate a coverage file with the following format.

```
Dataset;Strain;Abundance
0;/path/to/genomes/GCF_004792595.1_ASM479259v1_genomic.fna;49.08896171517891
0;/path/to/genomes/GCF_004792635.1_ASM479263v1_genomic.fna;24.227616649590498
0;/path/to/genomes/GCF_900478175.1_33787_E01_genomic.fna;26.68342163523058
1;//path/to/genomes/GCF_004792595.1_ASM479259v1_genomic.fna;68.62897751203839
1;/path/to/genomes/GCF_004792635.1_ASM479263v1_genomic.fna;29.843335974802045
1;/path/to/genomes/GCF_900478175.1_33787_E01_genomic.fna;1.5276865131595745
2;/path/to/genomes/GCF_004792595.1_ASM479259v1_genomic.fna;25.46861676806681
2;/path/to/genomes/GCF_004792635.1_ASM479263v1_genomic.fna;73.73717122422924
2;/path/to/genomes/GCF_900478175.1_33787_E01_genomic.fna;0.7942120077039481
3;/path/to/genomes/GCF_004792595.1_ASM479259v1_genomic.fna;65.67273602655372
3;/path/to/genomes/GCF_004792635.1_ASM479263v1_genomic.fna;0.2682704016216626
3;/path/to/genomes/GCF_900478175.1_33787_E01_genomic.fna;34.0589935718246
4;/path/to/genomes/GCF_004792595.1_ASM479259v1_genomic.fna;20.186503363681208
4;/path/to/genomes/GCF_004792635.1_ASM479263v1_genomic.fna;4.381463860002489
4;/path/to/genomes/GCF_900478175.1_33787_E01_genomic.fna;75.4320327763163
```

Generate the fastq files from the coverage profile

```
python3 ./simulation_generateReads.py coverageProfiles.csv outputDir /path/to/pbsim-master/ [short|long] errorRate

Example:
python3 ./simulation_generateReads.py rootDir/coverageProfiles.csv rootDir/reads/ ./pbsim-master/ long 0.999
```

This will create the readsets in rootDir/reads/ folder ("rootDir/reads/simulatedReads_*.fastq.gz") and the file "rootDir/reads/abundance_profile.csv" containing all information on the simulation.

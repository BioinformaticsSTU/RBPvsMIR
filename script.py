
from shutil import copyfile
import os
import random
import sys



#################
# pita
def pita(rna, distance, species, p_value, ddG, FDR):
	num=random.randint(0, 999);
	print("num is "+str(num));
	fp_log=open("log.txt", "w");
	fp_log.write("pita\n");
	title="RNA_"+str(num);
	rna_name=title+".fasta";
	fp_rna=open(rna_name, "w");
	fp_rna.write(">SEQUENCE\n");
	fp_rna.write(rna);
	fp_rna.close();
	DIR=title+"_dir";
	file_1000=DIR;
	os.system("./run_perturbate_string.sh /usr/local/matlab "+title);
	#os.system("./perturbate.R "+title+" "+rna);
	os.system("./run_padjust.py "+title+" "+distance+" "+species);
	fp_log.write("run_padjust\n");
	fp_log.write(title+":"+distance);
	os.system("./multipro.pl "+DIR+" "+title+" "+distance+" "+species);
	fp_log.write("multipro\n");
	os.system("./run_perturbate_string.sh /usr/local/matlab "+title);
	#os.system("./perturbate.R");
	os.system("./multicheck.pl "+DIR+" "+title+" "+distance+" "+species);
	fp_log.write("multicheck\n");
	DIR="result/"+title;
	os.system("./get_top_PRpair.py "+DIR+" "+p_value+" "+ddG);
	os.system("./get_PRpair.sh "+DIR);
	os.system("./multi_sum_and_total.pl "+DIR+" "+title);
	os.system("./integrate.py result/"+title);
	#os.system("rm -r result/"+title+"_*");
	os.rmdir(file_1000);
	os.remove(rna_name);
	os.remove(file);
	#copyfile("result_index.php", DIR+"/index.php");
	os.rename(DIR+"/result.txt", DIR+"/result0.txt");
	os.system("./get_FDR2.r "+DIR+" "+FDR);
	os.system("./get_pair.sh "+DIR);
	os.system("./network.r "+DIR);
	fp_log.close();

###########
# targetscan
def targetscan(rna, distance, species, p_value, FDR):
	num=random.randint(0, 999);
	fp_log=open("log.txt", "w");
	fp_log.write("targetscan");
	title="RNA_"+str(num);
	rna_name=title+".fasta";
	fp_rna=open(rna_name, "w");
	fp_rna.write(rna);
	fp_rna.close();
	DIR=title+"_dir";
	file_1000=DIR;
	os.system("./run_perturbate_string.sh /usr/local/matlab "+title);
	#os.system("./perturbate.R");
	os.system("./run_padjust_RBP_TS.py "+title+" "+distance+" "+species);
	fp_log.write("run_padjust_RBP_TS");
	os.system("./multipro_RBP_TS.pl "+DIR+" "+title+" "+distance+" "+species);
	fp_log.write("multipro_RBP_TS");
	os.system("./run_perturbate_string.sh /usr/local/matlab "+title);
	#os.system("./perturbate.R");
	DIR="result/"+title;
	os.system("./get_top_PRpair_RBP_TS.py "+DIR+" "+p_value);
	fp_log.write("get_top_PRpair_RBP_TS");
	os.system("./get_PRpair_RBP_TS.sh "+DIR);
	os.system("./multi_sum_and_total_RBP_TS.pl "+DIR+" "+title);
	os.system("./integrate_RBP_TS.py result/"+title);
	#os.system("rm -r result/"+title+"_*");
	os.rmdir(file_1000);
	os.remove(rna_name);
	os.remove(file);
	#copyfile("result_index.php", DIR+"/index.php");
	os.rename(DIR+"/result.txt", DIR+"/result0.txt");
	os.system("./get_FDR_RBP_TS.r "+DIR+" "+FDR);
	os.system("./get_pair.sh "+DIR);
	os.system("./network.r "+DIR);
	fp_log.close();


#######
# union and intersection
def UI(rna, distance, species, p_value, ddG, FDR):
	num=random.randint(0, 999);
	fp_log=open("log.txt", "w");
	fp_log.write("union and intersection\n");
	title="RNA_"+str(num);
	rna_name=title+".fasta";
	fp_rna=open(rna_name, "w");
	fp_rna.write(rna);
	fp_rna.close();
	DIR=title+"_dir";
	file_1000=DIR;
	os.system("./run_perturbate_string.sh /usr/local/matlab "+title);
	#os.system("./perturbate.R");
	os.system("./run_padjust_RBP_TS_pita.py "+title+" "+distance+" "+species);
	fp_log.write("run_padjust_RBP_TS_pita");
	fp_log.write(title+":"+distance);
	os.system("./multipro_RBP_TS_pita.pl "+DIR+" "+title+" "+distance+" "+species);
	fp_log.write("multipro");
	os.system("./run_perturbate_string.sh /usr/local/matlab "+title);
	#os.system("./perturbate.R");
	os.system("./multicheck.pl "+DIR+" "+title+" "+distance+" "+species);
	fp_log.write("multicheck");
	DIR="result/"+title;
	os.system("./get_top_PRpair_RBP_TS_pita.py "+DIR+" "+p_value+" "+ddG);
	os.system("./get_PRpair_RBP_TS_pita.sh "+DIR);
	os.system("./multi_sum_and_total_pita.pl "+DIR+" "+title);
	os.system("./multi_sum_and_total_TS.pl "+DIR+" "+title);
	os.system("./integrate_RBP_TS_pita.py result/"+title);
	#os.system("rm -r result/"+title+"_*");
	os.rmdir(file_1000);
	os.remove(rna_name);
	os.remove(file);
	os.rename(DIR+"/result_pita.txt", DIR+"/result0_pita.txt");
	os.rename(DIR+"/result_TS.txt", DIR+"/result0_TS.txt");
	os.system("./get_FDR_RBP_TS_pita.r "+DIR+" "+FDR);
	os.system("./get_pair_TS_pair.sh "+DIR);
	os.system("./network_RBP_TS_pita.r "+DIR);
	fp_log.close();

"""

##
# rna="GTAAAGGACTGGGGCCCCGCAACTGGCCTCTCCTGCCCTCTTAAGCGCAGCGCCATTTTAGCAACGCAGAAGCCCGGCGCCGGGAAGCCTCAGCTCGCCTGAAGGCAGGTCCCCTCTGACGCCTCCGGGAGCCCAGGTTTCCCAGAGTCCTTGGGACGCAGCGACGAGTTGTGCTGCTATCTTAGCTGTCCTTATAGGCT";
# distance=str(0);
# species="human";
# p_value=str(0.05);
# ddG=str(-6);
# FDR=str(0.05);
# pita(rna, distance, species, p_value, ddG, FDR);



# rna=sys.argv[1];
# distance=sys.argv[2];
# species=sys.argv[3];
# p_value=int(sys.argv[4])/2;
# ddG=sys.argv[5];
# FDR=sys.argv[5];
# pita(rna, distance, species, p_value, ddG, FDR);

def pita(rna, distance, species, p_value, ddG, FDR):
	print("pita");
	print(rna+"	"+distance+"	"+species+"	"+p_value+"	"+ddG+"	"+FDR);


def targetscan(rna, distance, species, p_value, FDR):
	print("targetscan");
	print(rna+"	"+distance+"	"+species+"	"+p_value+"	"+FDR);


def UI(rna, distance, species, p_value, ddG, FDR):
	print("UI");
	print(rna+"	"+distance+"	"+species+"	"+p_value+"	"+ddG+"	"+FDR);

"""





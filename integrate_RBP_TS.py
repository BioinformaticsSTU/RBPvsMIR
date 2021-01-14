#!/usr/bin/python

import sys
import commands

path=sys.argv[1];

file_PRresult=path+"/PRresult_top.txt";
file_prpair=path+"/prpair_sta.txt";
file_output=path+"/result.txt";

fp_w=open(file_output, "w");
fp_PR=open(file_PRresult, "r");
fp_w.write("RBP\tmiRNAs\tposition_of_RBP\tposition_of_miRNAs\tp_value_from_RBPmap\tnumber_of_overlapping_sites_in_real_sequence\tobserved_number_of_sequence_having_binding_sites_equal_to_or_large_than_the_real_one_in_simulated_data\n");
#fp_w.write("RBP\tmiRNAs\tpRBP\tpRNAs\tRBPpvalue\tddG\tnumber\tobserved\n");

line=fp_PR.readline();
while(line!=""):
    words=line.split("\t");
    protein=words[0];
    rna=words[1];
    result=commands.getoutput("cat "+file_prpair+" | grep "+protein+"$'\t'"+rna+"$'\t'");
    words_result=result.strip().split("\t");
    rest=words_result[2]+"\t"+words_result[5]+"\n";
    fp_w.write(line.strip()+"\t"+rest);
    line=fp_PR.readline();

fp_PR.close();
fp_w.close();



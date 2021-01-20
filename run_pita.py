#!/usr/bin/python

import commands
import time
import os
import sys

file_input=sys.argv[1];
num=sys.argv[2];
title=sys.argv[3];


#########rm
commands.getoutput("rm result/"+title+"_"+num+"/*pita*");

###########pita

input_pita_utr=file_input; #input_utr.fa
input_pita_mirna="known_mirs/human_mirs.fasta"; #known_mirs/human_mirs.fasta,input_microRNAs.fa
output_name="test";

commands.getoutput("./pita/pita_prediction.pl -utr "+input_pita_utr+" -mir "+input_pita_mirna+" -prefix result/"+title+"_"+num+"/"+output_name+" -gxp -l 8 -gu 8;0 -m 8;0");

###########integrate

file_pita="result/"+title+"_"+num+"/test_pita_results.tab";
file_rbpmap="result/"+title+"_"+num+"/file_"+num;

#fp_fimo=open("fimo.txt", "r");
fp_pita=open(file_pita, "r");
fp_rbpmap=open(file_rbpmap, "r");

line_pita=fp_pita.readline();
words_pita=line_pita.split();

#####################
arrR=[];
line_rbpmap=fp_rbpmap.readline();
i=0;
while(line_rbpmap!=""):
    words_rbpmap=line_rbpmap.split("\t");
    motif_rbpmap=words_rbpmap[0].strip();
    start_rbpmap=words_rbpmap[1].strip();
    end_rbpmap=str(int(start_rbpmap)+8);
    z_rbpmap=words_rbpmap[4].strip();
    p_rbpmap=words_rbpmap[5].strip();
    arrR.append([]);
    arrR[i]=[motif_rbpmap, start_rbpmap, end_rbpmap, z_rbpmap, p_rbpmap];
    i=i+1;
    line_rbpmap=fp_rbpmap.readline();


###########
arrP=[];
line_pita=fp_pita.readline();
i=0;
while(line_pita!=""):
    words_pita=line_pita.strip().split("\t");
    utr=words_pita[0].strip();
    mirna=words_pita[1].strip();
    start=words_pita[3].strip();
    end=words_pita[2].strip();
    dGduplex=words_pita[7].strip();
    arrP.append([]);
    arrP[i]=[utr, mirna, start, end, dGduplex];
    line_pita=fp_pita.readline();
    i=i+1;

############

###############
#num_F=len(arrF);
num_P=len(arrP);
num_R=len(arrR);

file_result="result/"+title+"_"+num+"/PRresult.txt";
fp_w=open(file_result, "w");
for i in range(0,num_R):
    for j in range(0,num_P):
        if( ( int(arrR[i][1])<=int(arrP[j][2]) and int(arrP[j][2])<=int(arrR[i][2]) ) or ( int(arrR[i][1])<=int(arrP[j][3]) and int(arrP[j][3])<=int(arrR[i][2]) ) ):
            fp_w.write(arrR[i][0]+"\t"+str(arrR[i][1])+"-"+str(arrR[i][2])+"\t"+str(arrR[i][3])+"\t"+str(arrR[i][4])+"\t"+arrP[j][1]+"\t"+str(arrP[j][2])+"-"+str(arrP[j][3])+"\t"+str(arrP[j][4])+"\n");
            #fp_w.write(arrR[i][0]+"\t"+arrM[j][1]+"\t"+str(arrR[i][1])+"-"+str(arrR[i][2])+"\t"+str(arrM[j][2])+"-"+str(arrM[j][3])+"\n");

fp_pita.close();
#fp_fimo.close();
fp_rbpmap.close();
fp_w.close();

#commands.getoutput("cp result/"+num+"/PRresult.txt RESULT/output"+num);



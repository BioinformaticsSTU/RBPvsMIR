#!/usr/bin/python

import commands
import time
import os
import sys

file_input=sys.argv[1];
num=sys.argv[2];
title=sys.argv[3];
extent=int(sys.argv[4])/2;
species=sys.argv[5];


#dir="/home/dzchen/data_and_code/RBPmap/";
dir="RBPmap/";

##########RBPmap
timestamp=commands.getoutput("perl "+dir+"RBPmap.pl -input "+file_input+"| grep 'Job name' | awk -F ':' '{print $2}'");
timestamp=timestamp.strip();

###########pita

input_pita_utr=file_input; #input_utr.fa

if(species=="human"):
  input_pita_mirna="known_mirs/human_mirs.fasta"; #known_mirs/human_mirs.fasta,input_microRNAs.fa
else:
  input_pita_mirna="known_mirs/mouse_mirs.fasta";

output_name="test";

commands.getoutput("/opt/pita/pita -utr "+input_pita_utr+" -mir "+input_pita_mirna+" -prefix result/"+timestamp+"/"+output_name+" -gxp -l 8 -gu 8;0 -m 8;0");

############

dir_rbpmap="result/"+timestamp+"/";
commands.getoutput("cat "+dir_rbpmap+"All_Predictions.txt | grep -n  Protein > "+dir_rbpmap+"protein_and_site.txt");
commands.getoutput('cat '+dir_rbpmap+'All_Predictions.txt | grep -n  Protein | awk -F ":" \'BEGIN{ ORS=","; } {print $1}\' > '+dir_rbpmap+'protein_site.txt');
commands.getoutput('wc -l '+dir_rbpmap+'All_Predictions.txt  | awk -F " " \'{print $1}\' >>'+dir_rbpmap+'protein_site.txt ');
commands.getoutput('cat '+dir_rbpmap+'All_Predictions.txt | grep -n  Protein | awk -F ":" \'BEGIN{ ORS=","; } {print $3}\' > '+dir_rbpmap+'protein_name.txt');

###########

fp=open(dir_rbpmap+"All_Predictions.txt","r");
fp_site=open(dir_rbpmap+"protein_site.txt", "r");
line_site=fp_site.readline().strip();
words_site=line_site.split(",");
words_site=words_site[0:len(words_site)];
num_site=len(words_site);

fp_name=open(dir_rbpmap+"protein_name.txt", "r");
line_name=fp_name.readline().strip();
words_name=line_name.split(",");
words_name=words_name[0:len(words_name)-1];

i=0;
for i in range(0, len(words_name) ):
    words_name[i]=words_name[i].strip().split("(")[0];

num_name=len(words_name);

array=[];
i=0;
for i in range(0, len(words_name)-1 ):
    protein_name=words_name[i];
    start=str(int(words_site[i])+2);
    end=str(int(words_site[i+1])-2);
    array.append([]);
    array[i]=[protein_name, start, end];

array.append([]);
arr_len=len(array)-1;
array[arr_len]=[words_name[arr_len], str(int(words_site[arr_len])+2), str(int(words_site[arr_len+1])-2)];

############
len_array=len(array);
filein_rbpmap=dir_rbpmap+"All_Predictions.txt";
fileout_rbpmap=dir_rbpmap+"file_"+num;
commands.getoutput("rm "+fileout_rbpmap);
commands.getoutput("touch "+fileout_rbpmap);

for i in range(0, len_array):
    protein= array[i][0];
    start= array[i][1];
    end= array[i][2];
    commands.getoutput("sed -n -e "+start+"','"+end+"'p' "+filein_rbpmap+" | sed 's/^/'"+protein+"'\t&/g' >>"+fileout_rbpmap);

commands.getoutput("rm result/"+title+"_"+num);
commands.getoutput("mv result/"+timestamp+" result/"+title+"_"+num);

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
    start_rbpmap=str(int(words_rbpmap[1].strip())-extent);
    end_rbpmap=str(int(words_rbpmap[1].strip())+8+extent);
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
    start=str(int(words_pita[3].strip())-extent);
    end=str(int(words_pita[2].strip())-extent);
    dGduplex=words_pita[7].strip();
    arrP.append([]);
    arrP[i]=[utr, mirna, start, end, dGduplex];
    line_pita=fp_pita.readline();
    i=i+1;

############

###############
num_P=len(arrP);
num_R=len(arrR);

file_result="result/"+title+"_"+num+"/PRresult.txt";
fp_w=open(file_result, "w");
for i in range(0,num_R):
    for j in range(0,num_P):
        if( ( int(arrR[i][1])<=int(arrP[j][2]) and int(arrP[j][2])<=int(arrR[i][2]) ) or ( int(arrR[i][1])<=int(arrP[j][3]) and int(arrP[j][3])<=int(arrR[i][2]) ) ):
            fp_w.write(arrR[i][0]+"\t"+str(arrR[i][1])+"-"+str(arrR[i][2])+"\t"+str(arrR[i][3])+"\t"+str(arrR[i][4])+"\t"+arrP[j][1]+"\t"+str(arrP[j][2])+"-"+str(arrP[j][3])+"\t"+str(arrP[j][4])+"\n");

fp_pita.close();
fp_rbpmap.close();
fp_w.close();




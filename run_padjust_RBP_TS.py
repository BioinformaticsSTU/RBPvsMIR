#!/usr/bin/python

import commands
import time
import os
import sys

num=sys.argv[1];
file_input=num+".fasta";
extent=int(sys.argv[2])/2;
species=sys.argv[3];

dir="./RBPmap/";

##########RBPmap
timestamp=commands.getoutput("perl "+dir+"RBPmap.pl -input "+file_input+"| grep 'Job name' | awk -F ':' '{print $2}'");
timestamp=timestamp.strip();

########### TS

input_TS_utr=num+".txt"; #
if(species=="human"):
  input_TS_mirna="./targetscan_70/miR_Family_human_fix.txt"; #
else:
  input_TS_mirna="./targetscan_70/miR_Family_mouse_fix.txt";

output_name="result/"+timestamp+"/TS_output.txt";

fp_TS=open(file_input, "r");
head=fp_TS.readline().strip().strip(">");
content=fp_TS.readline();
fp_TS.close();
fp_w=open(input_TS_utr, "w");
if(species=="human"):
  fp_w.write(head+"\t9606\t"+content);
else:
  fp_w.write(head+"\t10090\t"+content);

fp_w.close();

commands.getoutput("./targetscan_70/targetscan_70.pl "+input_TS_mirna+" "+input_TS_utr+" "+output_name);

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

commands.getoutput("rm -r result/"+num);
commands.getoutput("mv result/"+timestamp+" result/"+num);


##########padjust.py


file_TS="result/"+num+"/TS_output.txt";
file_rbpmap="result/"+num+"/file_"+num;

fp_rbpmap=open(file_rbpmap, "r");
#####################
arrR=[];
line_rbpmap=fp_rbpmap.readline();
i=0;
while(line_rbpmap!=""):
    words_rbpmap=line_rbpmap.split("\t");
    motif_rbpmap=words_rbpmap[0].strip();
    start_rbpmap=int(words_rbpmap[1].strip())-extent;
    if(start_rbpmap<1):
      start_rbpmap=1;
    end_rbpmap=int(words_rbpmap[1].strip())+8+extent;
    p_rbpmap=words_rbpmap[5].strip();
    arrR.append([]);
    arrR[i]=[motif_rbpmap, start_rbpmap, end_rbpmap, p_rbpmap];
    i=i+1;
    line_rbpmap=fp_rbpmap.readline();


###########
fp_TS=open(file_TS, "r");
line_TS=fp_TS.readline();

arrTS=[];
line_TS=fp_TS.readline();
i=0;
while(line_TS!=""):
    words_TS=line_TS.strip().split("\t");
    mirna=words_TS[1].strip();
    start_TS=int(words_TS[3].strip())-extent;
    if(start_TS<1):
      start_TS=1
    end_TS=int(words_TS[4].strip())+extent;
    arrTS.append([]);
    arrTS[i]=[mirna, start_TS, end_TS];
    line_TS=fp_TS.readline();
    i=i+1;
############
num_TS=len(arrTS);
num_R=len(arrR);

file_result="result/"+num+"/PRresult.txt";
fp_w=open(file_result, "w");
for i in range(0,num_R):
    for j in range(0,num_TS):
        if( ( int(arrR[i][1])<=int(arrTS[j][1]) and int(arrTS[j][1])<=int(arrR[i][2]) ) or ( int(arrR[i][1])<=int(arrTS[j][2]) and int(arrTS[j][2])<=int(arrR[i][2]) ) ):
            fp_w.write(arrR[i][0]+"\t"+arrTS[j][0]+"\t"+str(arrR[i][1])+"-"+str(arrR[i][2])+"\t"+ str(arrTS[j][1])+"-"+str(arrTS[j][2])+"\t"+arrR[i][3]+"\n" );


fp_TS.close();
fp_rbpmap.close();
fp_w.close();




#!/usr/bin/python

import sys

num=sys.argv[1];

p_value=float(sys.argv[2]);
ddG=float(sys.argv[3]);

path=num;
file_input=path+"/PRresult.txt";
file_output=path+"/PRresult_top.txt";

fp=open(file_input, "r");
fp_w=open(file_output, "w");
line=fp.readline();
while(line!=""):
    words=line.strip().split("\t");
    if(float(words[4])<= p_value and float(words[5])<= ddG):
        fp_w.write(line);
    line=fp.readline();

fp.close();
fp_w.close();




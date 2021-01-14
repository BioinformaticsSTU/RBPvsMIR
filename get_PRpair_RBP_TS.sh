#!/bin/bash

#input=$1;
#output=$2;
path=$1;

input=$path"/PRresult_top.txt";
output=$path"/protein_and_rna_top.txt";

awk '{print $1"\t"$2}' $input | sort -u > $output;
#awk '{print $1"\t"$5}' $input | sort -u > $output;




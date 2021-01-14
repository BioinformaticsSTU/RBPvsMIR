#!/bin/bash

#input=$1;
#output=$2;
path=$1;

input=$path"/PRresult_top_TS.txt";
output=$path"/protein_and_rna_top_TS.txt";

awk '{print $1"\t"$2}' $input | sort -u > $output;
#awk '{print $1"\t"$5}' $input | sort -u > $output;

#############
input=$path"/PRresult_top_pita.txt";
output=$path"/protein_and_rna_top_pita.txt";

awk '{print $1"\t"$2}' $input | sort -u > $output;



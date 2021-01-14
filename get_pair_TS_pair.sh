#!/bin/bash

path=$1;
`cat ${path}/result_TS.txt |tail -n +2 | awk '{print $1"\t"$2}' | sort -u > ${path}/PRpair_TS.txt `;

`cat ${path}/result_pita.txt |tail -n +2 | awk '{print $1"\t"$2}' | sort -u > ${path}/PRpair_pita.txt `;

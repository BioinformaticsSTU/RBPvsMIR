#!/bin/bash

path=$1;
`cat ${path}/result.txt |tail -n +2 | awk '{print $1"\t"$2}' | sort -u > ${path}/PRpair.txt `;

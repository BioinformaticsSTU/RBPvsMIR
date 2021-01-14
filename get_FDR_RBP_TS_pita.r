#!/usr/bin/Rscript

#.libPaths("/var/www/html/OmicsARules/R-3.2.3/library");

args<-commandArgs(T);
path=args[1];
FDR_value=as.numeric(args[2]);

result=read.table(paste(path,"result0_pita.txt", sep="/"), header=TRUE);
occurence=result[7];
greater=result[8];
pvalue=greater/1000;

n=nrow(pvalue);
FDR=p.adjust(as.numeric(pvalue[[1]]),"fdr", n);

result_m=as.matrix(result);
pvalue_m=as.matrix(pvalue);
colnames(pvalue_m)=c("pvalue");

FDR_m=as.matrix(FDR);
colnames(FDR_m)="FDR";

result_all=cbind(result_m, pvalue_m, FDR_m);

data=result_all[result_all[,10] <= FDR_value,];

write.table(data, paste(path, "result_pita.txt", sep="/"), sep="\t", quote=FALSE, row.names = FALSE);

################

result=read.table(paste(path,"result0_TS.txt", sep="/"), header=TRUE);
occurence=result[5];
greater=result[6];
pvalue=greater/1000;

n=nrow(pvalue);
FDR=p.adjust(as.numeric(pvalue[[1]]),"fdr", n);

result_m=as.matrix(result);
pvalue_m=as.matrix(pvalue);
colnames(pvalue_m)=c("pvalue");

FDR_m=as.matrix(FDR);
colnames(FDR_m)="FDR";

result_all=cbind(result_m, pvalue_m, FDR_m);

data=result_all[result_all[,9] <= FDR_value,];

write.table(data, paste(path, "result_TS.txt", sep="/"), sep="\t", quote=FALSE, row.names = FALSE);



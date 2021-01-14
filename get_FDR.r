#!/var/www/html/OmicsARules/R-3.2.3/bin/Rscript

.libPaths("/var/www/html/OmicsARules/R-3.2.3/library");
library(dplyr)

args<-commandArgs(T);
path=args[1];
FDR_value=as.numeric(args[2]);

result=read.table(paste(path,"result.txt", sep="/"), header=TRUE);
#occurence=result[7];
#greater=result[10];

occurence=result[7];
greater=result[8];

pvalue=greater/1000;

colnames(pvalue)=c("pvalue");
n=nrow(pvalue);
result2=cbind(result, pvalue);

FDR=p.adjust(as.numeric(result2[[9]]),"fdr", n);

result3=cbind(result2, FDR);

data=filter(result3, FDR<= FDR_value);
write.table(data, paste(path, "result.txt", sep="/"), sep="\t", quote=FALSE, row.names = FALSE);


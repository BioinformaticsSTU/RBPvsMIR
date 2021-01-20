args<-commandArgs(T);
TITLE=args[1];
STRING=args[2];

STRING=toupper(STRING);
dir_name=TITLE+"_dir";
dir.create(dir_name);

for(i in 1:999){
	Sequence=strsplit(STRING, split="")[[1]];
	Sequence_p=sample(Sequence, length(Sequence));
	STRING_p=paste(Sequence_p, collapse="");
	file_name=paste(c(dir_name, '/string', i, '.txt'), collapse="");
	#print(file_name);
	cat(">SEQUENCE\n", file=file_name);
	cat(STRING_p, file=file_name, append=TRUE);
}


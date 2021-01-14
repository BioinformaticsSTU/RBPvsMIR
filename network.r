#!/usr/bin/Rscript

library(igraph)

args<-commandArgs(T);
path=args[1];

network=read.delim(paste(path, "PRpair.txt", sep="/"), header=F);
Network=as.data.frame(network);
g=graph_from_data_frame(Network);

pdf(paste(path, "network.pdf", sep="/"));
plot(g, vertex.size=3, vertex.color="red", edge.arrow.size=0.5, vertex.label.font=0.3);
#plot.igraph(g, layout=layout.fruchterman.reingold/layout_with_fr, size='10');
dev.off();

png(paste(path, "network.png", sep="/"), width=1080, height=720);
plot(g, vertex.size=3, vertex.color="red", edge.arrow.size=0.5, vertex.label.font=0.3);
dev.off();



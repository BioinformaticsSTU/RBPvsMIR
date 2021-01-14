

from argparse import ArgumentParser, RawTextHelpFormatter
from script import pita
from script import targetscan
from script import UI
##
def create_parser(subparsers, fun):
	if(fun=="pita"):
		parser_pita = subparsers.add_parser('pita', help='create a macroscopic image showing transcripts of queried gene');
		group_input = parser_pita.add_argument_group("Input files arguments");
		group_input.add_argument('-r','--rna', required=True, help="RNA sequence");
		group_input.add_argument('-s','--species', required=True, help="species");
		group_input.add_argument('-d','--distance', required=True, help="distance between RNA and RBP");
		group_input.add_argument('-p','--p_value', required=True, help="p value");
		group_input.add_argument('-g','--ddG', required=True, help="gene id that you want to query");
		group_input.add_argument('-f','--fdr', required=True, help="FDR");
		return(parser_pita);
	if(fun=="targetscan"):
		parser_targetscan = subparsers.add_parser('targetscan', help='create a macroscopic image showing transcripts of queried gene');
		group_input = parser_targetscan.add_argument_group("Input files arguments");
		group_input.add_argument('-r','--rna', required=True, help="RNA sequence");
		group_input.add_argument('-s','--species', required=True, help="species");
		group_input.add_argument('-d','--distance', required=True, help="distance between RNA and RBP");
		group_input.add_argument('-p','--p_value', required=True, help="p value");
		#group_input.add_argument('-g','--ddG', required=True, help="gene id that you want to query");
		group_input.add_argument('-f','--fdr', required=True, help="FDR");
		return(parser_targetscan);
	if(fun=="union"):
		parser_union = subparsers.add_parser('union', help='create a macroscopic image showing transcripts of queried gene');
		group_input = parser_union.add_argument_group("Input files arguments");
		group_input.add_argument('-r','--rna', required=True, help="RNA sequence");
		group_input.add_argument('-s','--species', required=True, help="species");
		group_input.add_argument('-d','--distance', required=True, help="distance between RNA and RBP");
		group_input.add_argument('-p','--p_value', required=True, help="p value");
		group_input.add_argument('-g','--ddG', required=True, help="gene id that you want to query");
		group_input.add_argument('-f','--fdr', required=True, help="FDR");
		return(parser_union);
	if(fun=="intersection"):
		parser_intersection = subparsers.add_parser('intersection', help='create a macroscopic image showing transcripts of queried gene');
		group_input = parser_intersection.add_argument_group("Input files arguments");
		group_input.add_argument('-r','--rna', required=True, help="RNA sequence");
		group_input.add_argument('-s','--species', required=True, help="species");
		group_input.add_argument('-d','--distance', required=True, help="distance between RNA and RBP");
		group_input.add_argument('-p','--p_value', required=True, help="p value");
		group_input.add_argument('-g','--ddG', required=True, help="gene id that you want to query");
		group_input.add_argument('-f','--fdr', required=True, help="FDR");
		return(parser_intersection);

#######
def main():
	description = "";
	parser = ArgumentParser(description=description, formatter_class=RawTextHelpFormatter, add_help=True);
	#subparsers = parser.add_subparsers(help='sub-command help');
	subparsers = parser.add_subparsers(dest='subcommand_name', help='sub-command help');
	# create the parser for the "pita" command
	parser_parser_pita=create_parser(subparsers, "pita");
	# create the parser for the "targetscan" command
	parser_parser_pita=create_parser(subparsers, "targetscan");
	# create the parser for the "union" command
	parser_parser_pita=create_parser(subparsers, "union");
	# create the parser for the "intersection" command
	parser_parser_pita=create_parser(subparsers, "intersection");
	###
	args = parser.parse_args();
	subcommand = args.subcommand_name;
	############
	if subcommand == "pita":
		pita(args.rna, args.distance, args.species, args.p_value, args.ddG, args.fdr);
		#print(args.rna+"	"+args.distance+"	"+args.species+"	"+args.p_value+"	"+args.ddG+"	"+args.fdr);
	if subcommand == "targetscan":
		targetscan(args.rna, args.distance, args.species, args.p_value, args.fdr);
		#print(args.rna+"	"+args.distance+"	"+args.species+"	"+args.p_value+"	"+args.fdr);
	if subcommand == "union" or subcommand == "intersection":
		UI(args.rna, args.distance, args.species, args.p_value, args.ddG, args.fdr);
		#print(args.rna+"	"+args.distance+"	"+args.species+"	"+args.p_value+"	"+args.ddG+"	"+args.fdr);


######
if __name__ == '__main__':
    main();







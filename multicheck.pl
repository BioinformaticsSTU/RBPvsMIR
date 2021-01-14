#!/usr/bin/perl

use threads;
use warnings;
use strict;

my $j=-1;
my $thread;

my $dir=$ARGV[0];
my $title=$ARGV[1];
my $extent=$ARGV[2]/2;
my $species=$ARGV[3];

while()
{
     #last if($j>=999);
     last if($j>=99);

     $j++;
     my $num=$j;
     my $cmd="cat result/".$title."_".$num."/test_pita_results.tab | wc -l";
     my $res_num=`$cmd`;
     if($res_num<15)
     {
       my $file_input=$dir."/string".$num.".txt";
       threads->new(\&ss, $file_input, $num, $title, $extent, $species);
       sleep(20);
     }

}

foreach $thread(threads->list(threads::all))
{
    $thread->join();
}

sub ss()  
{
    my ($file_input, $num, $title, $extent, $species)=@_;
    #system("./run_pita.py ".$file_input." ".$num." ".$title);
    system("./run_integration.py ".$file_input." ".$num." ".$title." ".$extent." ".$species);
}


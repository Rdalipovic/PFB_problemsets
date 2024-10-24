#!/usr/bin/env python

import os, sys, math

from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *


## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }


def count_kmers(kmer_list):

    kmer_count_dict = dict()

    ##################
    ## Step 2:
    ## begin your code
    for seq_kmers in kmer_list:
        for kmer in seq_kmers:
            if kmer not in kmer_count_dict:
                kmer_count_dict[kmer] = 0
            if kmer in kmer_count_dict:
                kmer_count_dict[kmer] += 1
        







    ## end your code
    ################

    return kmer_count_dict


def main():

    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(
        progname
    )

    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    kmer_length = int(sys.argv[2])
    num_top_kmers_show = int(sys.argv[3])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    all_kmers = list()

    #######################
    ## Step 1:
    ## begin your code, populate 'all_kmers' list with the
    ## collection of kmers from all sequences
    
    for seq in seq_list:
        all_kmers.append(sequence_to_kmer_list(seq,kmer_length))



    ## end your code
    #######################

    kmer_count_dict = count_kmers(
        all_kmers
    )  # see step 2 above. You implement this. :-)

    unique_kmers = list(kmer_count_dict.keys())

    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation

    unique_kmers = sorted(unique_kmers, key = lambda x: kmer_count_dict[x], reverse = True)    


    ##Logo creation
 
    entropy = {}
    count = 0
    for kmer in unique_kmers: #get each kmer in unique kmers
        freq = {}
        entropy[kmer] = 0
        for base in kmer: #get the count of each base in the kmer
            if base in freq:
                freq[base] += 1
            else:
                freq[base] = 1
        
        entropy_list = [] #list that will hold lists of elements that will be summed together
        for b in freq:
            
            hellow = abs( (freq[b]/len(kmer) ) * math.log2( freq[b]/len(kmer) )) #Shannon Entropy formula
            entropy_list.append(hellow)
       
        entropy[kmer] = sum(entropy_list) #sum to get entropy value and store in in a dict with the kmer as the key

        



    ## end your code

    ## printing the num top kmers to show
    top_kmers_show = unique_kmers[0:num_top_kmers_show]

    for kmer in top_kmers_show:
        print("{}: {} {}".format(kmer, kmer_count_dict[kmer], entropy[kmer]))

    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()

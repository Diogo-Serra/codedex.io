#!/usr/bin/env python3

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG',
                'GAA', 'ACC', 'GGA']
item_to_find = 'TGA'
item_found = False
for dna in dna_sequence:
    if dna == item_to_find:
        item_found = True
    if item_found:
        print("Item Found!")
    else:
        print("Item not found")

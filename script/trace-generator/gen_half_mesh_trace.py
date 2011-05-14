#!/usr/bin/env python
# usage: python gen_star_trace.py <number-of-nodes> <run-time [s]> <output-file>

import sys
import datetime
import os
import operator
import random

if len(sys.argv) != 4:
	print "usage: python " + sys.argv[0] + " <number-of-nodes> <run-time [s]> <output-file>"
	sys.exit(1)

number_of_nodes = int(sys.argv[1])
run_time = int(sys.argv[2])
out = file(sys.argv[3], "w")

q_c=0.8
first_node_index = 1
last_node_index = first_node_index + number_of_nodes - 1

for i in range(first_node_index, last_node_index + 1):
	for j in range(first_node_index, last_node_index + 1):
		if (i != j and random.random() > q_c):
			out.write(str(i) + "\t" + str(j) + "\t" + str(0) + "\t" + str(run_time) + "\n")

out.close()

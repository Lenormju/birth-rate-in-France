#!/usr/bin/python
# -*- coding: latin-1 -*-
OUT_FILE_NAME = "naissances.plot"
IN_FILE_NAME = "data_naissances.txt"
with open(IN_FILE_NAME) as in_file, \
		open(OUT_FILE_NAME, 'w') as out_file:
	i = 0
	for line in reversed(in_file.readlines()): # get chronologic order
		parts = line.strip('\n').split(" 	")
		year = int(parts[0])
		month = parts[1]
		amount = int(parts[2].replace(' ', '').split('(p)')[-1])
		out_file.write("{year}\t{month}\t{amount}\n".format(**locals()))
		i += 1
	print("Processed {} entries into {}".format(i, OUT_FILE_NAME))

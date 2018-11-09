# Understand behaviour of SeqIO with empty files of different formats

import os
from Bio import SeqIO

# path to folder containing empty files
dir_ = 'empty'

# list files in directory of interest
for filename in os.listdir(dir_):
	print('\nFile type: '+filename.split('.')[-1])
	try:
		for record in SeqIO.parse(dir_+'/'+filename, filename.split('.')[-1]):
			print(record.id)
	except Exception as e:
		print(filename.split('.')[-1] + ' gives an error')
		print(e)
	else:
		print('No error')
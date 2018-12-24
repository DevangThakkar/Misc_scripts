import os
import sys
import Bio
from timeit import timeit

SEQ_LINE = '@dummy\n' + 'ATCGN'*10 + '\n' + '+dummy\n' + 'IFG?W'*10 + '\n'

# Make test file
if not os.path.isfile('file.fastq'):
    with open('file.fastq', 'w') as out_f:
        for _ in range(50000000):
            out_f.write(SEQ_LINE)

def use_parser(parser, filename):
    with open(filename) as handle:
        return list(parser(handle))

print('Python version: {}\n'
      'Biopython version: {}'.
       format(sys.version_info, Bio.__version__))
# print('New version: Run 23-12-18_21:15')
# print('can not remove all rstrip() keeping it for line 2/4, 10x20, py3')
sum_ = 0.0
for _ in range(10):
    print('Iteration '+str(_))
    b = timeit(
            'use_parser(FastqStrictIterator, "file.fastq")',
            setup='from Bio.SeqIO.QualityIO import FastqStrictIterator; from __main__ import use_parser',
            number = 20)

    sum_ += b

    print('New: %.2f' % b)

print(sum_/10)

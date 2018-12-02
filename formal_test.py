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

sum_ = 0

for _ in range(10):
    print('Iteration '+str(_))
    a = timeit(
            'use_parser(FastqGeneralIterator, "file.fastq")',
            setup='from Bio.SeqIO.QualityIO import FastqGeneralIterator; from __main__ import use_parser',
            number = 20)
    b = timeit(
            'use_parser(FastqStrictIterator, "file.fastq")',
            setup='from Bio.SeqIO.QualityIO import FastqStrictIterator; from __main__ import use_parser',
            number = 20)

    sum_ += a

    print('Old: %.2f' % a)
    print('New: %.2f' % b)
    print('Change: %.2f' % (a-b))

print(sum_)
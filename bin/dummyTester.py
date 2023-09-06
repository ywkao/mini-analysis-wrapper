#!/usr/bin/env python2
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input filename of parameters', default='', type=str)
parser.add_argument('-o', '--output', help='output filename of result', default='', type=str)
args = parser.parse_args()

# load parameters
filename = args.input
with open(filename, 'r') as fin:
    contents = fin.readlines()
    for line in contents:
        if not 'paramB' in line:
            continue
        paramB = tuple([float(ele) for ele in line.strip().split(' = ')[1].split(', ')])

# perform some calculation
def dummy_algorithm(parameters):
    '''dummy data processing'''
    result = tuple([ele*10. for ele in list(paramB)])
    return result

result = dummy_algorithm(paramB)

# determine output file name & export result
outputName = args.output
with open(outputName, 'w') as fout:
    fout.write("# result with {0}\n".format(paramB))
    fout.write("dummy result = {0}\n".format(result))

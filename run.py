#!/usr/bin/env python2
import subprocess
import argparse
import interface.config as cfg
import interface.parallel_utils as pu

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dryRun', help='do not submit jobs', action='store_true')
args = parser.parse_args()

# manual containers
myRanges = (range(1,6), range(1,6), range(1,6)) # tuple of three lists
parameter_file_list = []
command_list = []

def exe(command):
    subprocess.call(command, shell=True)

def mkdir():
    command = 'mkdir -p output/config output/result'
    exe(command)

def generate_parameters():
    '''
    1. Generate a set of parameters values through a grid scan of given ranges.
    2. Export a set of values to a text file.
    '''
    rA, rB, rC = myRanges # pass elements through tuple
    for i in rA:
        for j in rC:
            for k in rB:
                str_values = "%.1f, %.1f, %.1f" % (i, j, k)
                filename = "./output/config/input_namelist_%d_%d_%d.txt" % (i, j, k)
                parameters = cfg.template.format(VALUES=str_values) # string format method

                #print(filename+'\n')
                #print(parameters)

                with open(filename, 'w') as fout:
                    fout.write(parameters+'\n')

                parameter_file_list.append(filename)

        break

def create_commands():
    ''' Create commands from a list of text files with generated parameters '''
    for f in parameter_file_list:
        command = "./bin/dummyTester.py --input %s" % f
        command_list.append(command)

def submit_jobs():
    ''' Submit jobs through python multiprocessing module if not in dryRun; otherwise simply pring commands '''
    if args.dryRun:
        for command in command_list: print(command)
    else:
        pu.submit_jobs(command_list, 10)


if __name__ == "__main__":
    mkdir()
    generate_parameters()
    create_commands()
    submit_jobs()

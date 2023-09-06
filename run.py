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
    if args.dryRun:
        print(command)
    else:
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
        for j in rB:
            for k in rC:
                str_values = "%.1f, %.1f, %.1f" % (i, j, k)
                filename = "./output/config/input_namelist_%d_%d_%d.txt" % (i, j, k)
                parameters = cfg.template.format(VALUES=str_values) # string format method

                #print(filename+'\n')
                #print(parameters)

                if args.dryRun:
                    print(filename + " will be created")
                else:
                    with open(filename, 'w') as fout:
                        fout.write(parameters+'\n')

                parameter_file_list.append(filename)

        break # only len(rB)xlen(rC) of parameter files will be created

    ''' Caveat: one needs to avoid more than 1,000 files in a directory '''

def create_commands():
    ''' Create commands from a list of text files with generated parameters '''
    for f in parameter_file_list:
        output_file_name = f.replace('config', 'result').replace('input_namelist', 'output')
        command = "./bin/dummyTester.py --input %s --output %s" % (f, output_file_name)
        command_list.append(command)

def submit_jobs():
    ''' Submit jobs through python multiprocessing module if not in dryRun mode; otherwise, simply printing commands '''
    if args.dryRun:
        for command in command_list: print(command)
    else:
        pu.submit_jobs(command_list, 10) # processing 10 jobs in the same time

        '''Remark: it will be even better to use bsub or condor jobs for multi-processing'''

def print_final_message():
    if args.dryRun:
        print("[INFO] this is the end of dryRun mode (print commands only)")
    else:
        print("[INFO] all jobs completed!")

if __name__ == "__main__":
    mkdir()
    generate_parameters()
    create_commands()
    submit_jobs()
    print_final_message()

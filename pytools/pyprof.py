#!/usr/bin/env python
import os, sys, glob

if not len(sys.argv) > 1:
    raise ValueError('need a python script to run')

python_script = " ".join(sys.argv[1:])
profiling_file = python_script.split('pyprof')[-1].split()[0].split('/')[-1]
assert profiling_file.endswith('.py')
profiling_file = profiling_file.replace('.py', '.prof')
#if os.path.exists(profiling_file):
    #raise Exception('{} exists already'.format(profiling_file))

cmd = "/usr/bin/env python -B -m cProfile -o {profiling_file} {python_script} " \
    .format(python_script = python_script, profiling_file=profiling_file)
print(cmd)
os.system(cmd)

cmd = "pyprof2calltree -i {profiling_file} -k ".format(profiling_file=profiling_file)
print(cmd)
os.system(cmd)


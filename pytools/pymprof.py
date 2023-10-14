#!/usr/bin/env python
import os, sys, glob


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        raise ValueError('need a python script to run')

    # this_file = os.path.basename(__file__)

    python_script = " ".join(sys.argv[1:])
    profiling_file = os.path.basename(python_script.split()[0])
    assert profiling_file.endswith('.py')
    profiling_file = profiling_file.replace('.py', '.py.lprof')

    cmd = f"/usr/bin/env python -m memory_profiler {python_script}"
    print(cmd)
    os.system(cmd)

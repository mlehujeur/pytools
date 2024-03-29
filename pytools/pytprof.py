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

    # cmd = f"/usr/bin/env kernprof -l {python_script} && /usr/bin/env python -m line_profiler {profiling_file}"
    cmd = f"/usr/bin/env kernprof -l -v -u 1e-3 {python_script}"  
    print(cmd)
    os.system(cmd)

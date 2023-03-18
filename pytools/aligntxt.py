import sys

filename = sys.argv[1]
sep = sys.argv[2]
assert sep in ',;\t '

with open(filename, 'r') as fid:
    for l in fid:
        columns = l.rstrip('\n').split(sep)
        

import os
import re

def count_sloc(path):
    # takes in a Jupyter Notebook filepath
    # returns its true source-lines-of-code count
    assert path[-6:] == ".ipynb", "must provide a Jupyter Notebook file"
    file = open(path)
    contents = file.read().split('\n')
    reading = False
    flag = False
    count = 0
    for s in contents:
        s = s.rstrip()
        if reading and re.search("\s+\]", s):
            flag = True
        if flag and re.search("\s+\}", s):
            flag = False
            reading = False
            count -=1
        if reading:
            print(repr(s))
            count += 1
        if '"source": [' in s:
            reading = True
    return count


def test_count_sloc():
    print(count_sloc('/Users/adityasengupta/projects/adaptive-optics/control/dev/AR2.ipynb'))


if __name__ == "__main__":
    test_count_sloc()

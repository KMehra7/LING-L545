import sys

line = sys.stdin.readline()

c = '. '

while line != '':
    if c in line :
        line = line.replace(c, '.\n')
    sys.stdout.write(line)
    line = sys.stdin.readline()
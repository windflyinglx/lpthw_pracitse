from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying file from %s to %s" % (from_file,to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %s" % exists(to_file)



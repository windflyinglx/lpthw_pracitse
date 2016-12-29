from sys import argv

script , file_name = argv

print 'We are going to earse %s' %file_name
print 'If you don\'t want that, hit CTRL-C (^C).'
print 'If you do want that, hit RETURN.'
raw_input('?')
print 'Opening file ...'
text = open(file_name,'w')
print 'Truncate... Goodbye!'
#text.truncate()

print 'Now I\'m going to ask you add 3 lines'
line1 = raw_input('line1:')
line2 = raw_input('line2:')
line3 = raw_input('line3:')
print 'Now I\'m going to add these lines to the file'
text.write(line1)
text.write('\n')
text.write(line2)
text.write('\n')
text.write(line3)
text.close()
print "And finally it is closed"

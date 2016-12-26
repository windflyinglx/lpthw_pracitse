from sys import argv

script,arg1,arg2 = argv
prompt = '>'

print '''Hi %s This is CNN News, 
and we want to know more about your life,
please answer the following questions.''' %arg1

print 'What will you do after graduation?',
job = raw_input(prompt)

print """Today we interviewed %s ,who is %s year old.
He is going to %s""" %(arg1,arg2,job)
 

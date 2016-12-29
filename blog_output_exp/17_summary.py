def greeting():
	print "Hello,my name is Robot, what's your name,plz write it down below:"
	name = raw_input('>')
	if name != 'Leon':
		print 'I see,so your name is %s' % name
	elif name == 'Leon':
		print 'Wow, your name is the same with my creater, %s' % name
	print """
Since you bought me online, it is my honor to be your personal secret.
I will try my best to serve you well. 
	"""
	return name

name = greeting()

# print name

def personal_information(name):
	print "now let me know more about you, %s" %name
	print "Which year were you born?",
	birth_year = int(raw_input('>'))
	print "what is your gender,male or female?",
	gender = raw_input("M means male,F means female >")
	age = 2016 - birth_year
#	print """
#In general,you are %d year old (that is pretty young).
#And you are %s
#""" % (age,gender)

#personal_information(name)

def function_chose():
	cal = "1. Caculation"
	rdf = "2. Read files"
	wtf = "3. Write files"
	ors = "4. Others"
	t = {1:cal,2:rdf,3:wtf,4:ors}

	print """ As a robot,I can do a lot for you, here is the list
%s
%s
%s
%s

please give me the number you want.
""" %(t[1],rdf,wtf,ors)
	function_chose = raw_input(">")
	if int(function_chose) in range(1,5):
		print t[int(function_chose)]
	else:
		print "Ops,I don't understand what you mean."
	return function_chose

function_chose()
# print function_chose()



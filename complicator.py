#from sys import argv


def st_tockovanje(starost):
    if starost < 20:
      return 1
    elif starost < 30:
      return 2
    else:
      return 3
    
def fb_tockovanje(prijatelji):
    if prijatelji < 20:
      return 5
    elif prijatelji < 50:
      return 20
    else:
      return 60   
    
def calculate():
  return fb_tockovanje(FB)+st_tockovanje(age)
  


prompt = '>>'

print "Do you have any deadlines (true/false)?" 
deadlines = raw_input(prompt)

print "Number of FB friends?" 
FB = int(raw_input(prompt))

print "How much money do you currently have?" 
money = raw_input(prompt)

print "What's the outside temperature?" 
temperature = raw_input(prompt)


print "What's your age?" 
age = int(raw_input(prompt))


print "Tvoj koncni rezultat = %r" % ((st_tockovanje(age) + fb_tockovanje(FB)))

print "se en print %r" % calculate()





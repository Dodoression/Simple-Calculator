#   PART 1
import math

s = input("Please enter 2 numbers and an operation:\n+, -, *, /\n")
s = ''.join(s.split())

def sqrt(float):
    if ('sqrt' in s_spt[0]):
        s_sfunc = s_spt[0].split('sqrt')
        print(s_sfunc)
        b = int[s_sfunc[0]]
        a = math.sqrt(s_sfunc[0])
        return a
    if ('sqrt' in s_spt[1]):
        s_sfunc = s_spt[1].split('sqrt')
        print(s_sfunc)
        print(math.sqrt(float(s_sfunc[1]))) 
        
        

if ('+' in s) :
    s_spt = (s.split('+'))
    sqrt(s_spt)
    #print("s1 i s2" + s_spt[0] + s_spt[1])
    new = float(s_spt[0]) + float(s_spt[1])
    print(new)

if ('-' in s) :
    s_spt = (s.split('-'))
    new = float(s_spt[0]) - float(s_spt[1])
    print(new)

if ('*' in s) :
    s_spt = (s.split('*'))
    new = float(s_spt[0]) * float(s_spt[1])
    print(new)

if ('/' in s) :
    s_spt = (s.split('/'))
    new = float(s_spt[0]) / float(s_spt[1])
    print(new)

# PART 2

while True :
    vuvedi = input("Using " + str(new) + " please enter an operation and another number:\n+, -, *, /\nor press = to get the end result.\n")
    s = ''.join(s.split())
    if ('=' in vuvedi):
        print(new)
        break;

    if ('+' in vuvedi) :
        vuvedi_spt = (vuvedi.split('+'))
        new = float(new) + float(vuvedi_spt[1])
        print(new)

    if ('-' in vuvedi) :
        vuvedi_spt = (vuvedi.split('-'))
        new = float(new) - float(vuvedi_spt[1])
        print(new)

    if ('*' in vuvedi) :
        vuvedi_spt = (vuvedi.split('*'))
        new = float(new) * float(vuvedi_spt[1])
        print(new)

    if ('/' in vuvedi) :
        vuvedi_spt = (vuvedi.split('/'))
        new = float(new) / float(vuvedi_spt[1])
        print(new)
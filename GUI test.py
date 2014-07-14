
#This is what we should run:



#Syntax to pass to the mid2cnc script: params = '-outfile ./mytest.gcode'
# os.system ('python -i mid2cnc.py ' + params)

import os
import easygui as eg
params = '' #initializing variable

machinelist = ('ultimaker', 'cupcake', 'thingomatic', 'shapercube', 'custom')
machine = eg.choicebox(msg='Machine type', title='Pick machine', choices=machinelist)
print machine

params = params + '-machine ' + machine

infile = eg.fileopenbox(msg='Choose the midi file ', title=' Grab the file you want to convert', default=os.path.expanduser("~")+"//My Documents/", filetypes = "*.mid") # the "default=os.path.expanduser("~")" gets your home forlder so you don't have top start browsing from some obscure python install folder
print infile
params = params + ' -infile ' + infile

outfile = eg.filesavebox(msg='Choose the output file ', title=' Pick where you want the gcode to arrive', default=os.path.expanduser("~")+"//My Documents//Output.gcode", filetypes = "*.gcode")
print outfile
params = params + " -outfile " + outfile

verbose = eg.boolbox(msg='Do you want the verbose to be activated (for debug)', title=' Verbose Y/N ', choices=('No', 'Yes'), image=None) # returns true if the first is chosen
if verbose == 0:
	 params = params + " -verbose"
print params


#TODO:
# Enforce .gcode at the end of outfile
# handle cases where nothing is entered
# Also why is filesavebox appearing in the background ?

#This is what we should run:



# params = '-outfile ./mytest.gcode'
# os.system ('python -i mid2cnc.py ' + params)

import os
import easygui as eg
params = '' #initializing variable


machine = eg.choicebox(msg='Machine type', title='Pick machine', choices=("Ultimaker","Cupcake"))
print machine

params = params + '-machine ' + machine

infile = eg.fileopenbox(msg='Choose the midi file ', title=' Grab the file you want to convert', default=os.path.expanduser("~")+"//My Documents/", filetypes = "*.mid") # the "default=os.path.expanduser("~")" gets your home forlder so you don't have top start browsing from some obscure python install folder
print infile
params = params + ' -infile ' + infile

outfile = eg.filesavebox(msg='Choose the output file ', title=' Pick where you want the gcode to arrive', default=os.path.expanduser("~")+"//My Documents//Output.gcode", filetypes = "*.gcode")
print outfile
params = params + " -outfile " + outfile

print params


#TODO:
# Enforce .gcode at the end of outfile
# Read repositories of survey metadata and convert to JSON

import numpy as np
from astropy import table
import json

# Option 1: Following info are needed to open the right ASCII table
field_name = 'COSMOS' # string -- please use conventional spelling (see list of fields at http://)
telescope = 'Subaru' # string
instr = 'SuprimeCam' # string 
data_type = 'imaging'  # string -- choose from: 'imaging','spectroscopy','ifu','grism','prism'
bands = ['Bj band','Vj band']  # list of string -- list of filters or configurations 
nbands = len(bands)
# Option 2: otherwise you can directly edit
uniq_id = ['{}_{}_{}_{}_{}'.format(field_name,telescope,instr,data_type,i[:i.find(' ')]) for i in bands]

# to distinguish string vs float keys
# same order as in Metadata_make_table.py
types  = ['S','S','S','S','S', 
          'S','S','S','f',
          'f','f','f',
          'f','f',
          'f','f','f',
          'f','f',
          'S','i','S','f',
          'f','f',
          'S','S','S','S','S']


for i in uniq_id:
    data = {}
    #infl = open(i+'.txt','r')
    outfl = open(i+'.json','w')
    with open('COSMOS_Subaru_SuprimeCam_imaging_Bj.txt','r') as infl:
        c = 0
        for l in infl:
            l = l.split()
            key = l[0][:l[0].find(':')] #remove : from string
            if types[c] == 'S': value = l[1]
            if  types[c] == 'i': value = int(l[1])
            if  types[c] == 'f': value = float(l[1])
            data[key] = value
            c += 1
    json.dump(data,outfl)
    outfl.close()
    infl.close()

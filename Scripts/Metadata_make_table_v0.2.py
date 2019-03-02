# Write repositories of survey metadata
# "Overview" Table  (see example at https://github.com/pcapak/Astronomy-Deep-Feild-Information/blob/master/Survey_Descriptions/COSMOS/overview/COSMOS_SuprimeCam_V.txt) 

import numpy as np
from astropy import table

#############################################
#####  SECTION TO BE FILLED BY THE USER #####
#############################################
# For strings, please avoid blank spaces, special chracters (!@?*/), 
# or the underscore (_). Use 'N/A' in fields that does not apply to your survey.
# For numeric inputs, please use -99 in fields that does not apply to your survey.

# Level-1 info
# This meta-data is the same for all the filters
survey_name = 'COSMOS' # string -- must be univocal
field_name = 'COSMOS' # string -- please use conventional spelling (see list of fields at http://)
telescope = 'Subaru' # string
instr = 'SuprimeCam' # string 
data_type = 'imaging'  # string -- choose from: 'imaging','spectroscopy','ifu','grism','prism'
data_status = 'acquired'  # string -- choose from: 'acquired','ongoing','planned','planning'
bands = ['Bj band','Vj band']  # list of string -- list of filters or configurations 
nbands = len(bands)

# Level-2 info
# Meta-data that depends on filter (as defined above in the `bands` list). 
# If the value is the same for all bands, just insert one entry. Otherwise a list of values
# with the same size of `bands`.
### General:
area_dataset = 2. # in deg^2, float or list of floats
pixel_size = 0.15 # in arcsec/pixel, float or list of floats
total_int_time = [1.2,0.9] # in hours,  float or list of floats
avg_psf_fwhm = [0.95,1.33] #over all exposures in arcsec, float or list of floats
tot_pt_sensitivity = -99. # 5sigma in AB mag, float or list of floats 
eff_wl = [4460.,5484.] # in AA, float or list of floats
spec_resol = [5.,6.] #in $\lambda/\Delta\lambda$, float or list of floats
min_wl = [4020.,4990.] #in AA, float or list of floats
max_wl = [4907.,5926.] #in AA, float or list of floats
mjd0 = [53024.19,53053.184] #Modified Julian Date, float or list of floats
mjd1 = [53054.663,53053.695] #Modified Julian Date, float or list of floats
### For cadence purposes:
visit_unit = 'single' # set to 'single' if no cadence
n_visit = 1 #set to 1 if single visit
cadence_type = 'N/A' #text description of general cadence routine in units of visits, set to 'N/A' if single visit
avg_cadence = -99.  # visit intervals in days (could be list if repeated cadence), set -99. if single visit
depth_visit = -99. #5sigma AB mag, set -99. if single visit
exptime_visit = -99. #in seconds, set -99. if single visit
### URLs:
url_data = 'https://irsa.ipac.caltech.edu/data/COSMOS/images/subaru/'  
url_cit = 'https://doi.org/10.1088/0004-637X/730/2/68' 
url_sky = ['https://github.com/pcapak/Astronomy-Deep-Feild-Information/blob/master/Survey_Descriptions/COSMOS/reg/COSMOS_SuprimeCam_B.reg','https://github.com/pcapak/Astronomy-Deep-Feild-Information/blob/master/Survey_Descriptions/COSMOS/reg/COSMOS_SuprimeCam_V.reg']
url_depth = 'N/A'
url_filt = ['https://github.com/pcapak/Astronomy-Deep-Feild-Information/blob/master/Survey_Descriptions/COSMOS/filters/COSMOS_SuprimeCam_B.res','https://github.com/pcapak/Astronomy-Deep-Feild-Information/blob/master/Survey_Descriptions/COSMOS/filters/COSMOS_SuprimeCam_V.res']

#############################################
##### END OF SECTION TO BE FILLED    ########
#####      THANK YOU FOR YOUR HELP!  ########
#############################################


# Build one table per filter, column names
# Users do not need to edit the following.

values = ['uniq_id',survey_name,field_name,telescope,instr,
         data_type,bands,data_status,area_dataset,
         pixel_size,total_int_time,avg_psf_fwhm,
         tot_pt_sensitivity,eff_wl,
         spec_resol,min_wl,max_wl,
         mjd0,mjd1,
         visit_unit,n_visit,cadence_type,avg_cadence,
         depth_visit,exptime_visit,
         url_data,url_cit,url_sky,url_depth,url_filt]     

colnames = ['UNIQUE_ID','SURVEY_NAME','FIELD_NAME','TELESCOPE','INSTRUMENT',
          'DATA_TYPE','DATA_NAME','DATA_STATUS','AREA_DATASET',
          'PIXEL_SIZE','TOTAL_INTEGRATION_TIME','AVERAGE_PSF_FWHM',
          'TOTAL_POINTSOURCE_SENSITIVITY','EFFECTIVE_WAVELENGTH',
          'SPECTRAL_RESOLUTION','MIN_WAVELENGTH','MAX_WAVELENGTH',
          'MJD_START','MJD_END',
          'VISIT_UNIT','NUMBER_OF_VISITS','CADENCE_TYPE','AVERAGE_CADENCE',
          'DEPTH_PER_VISIT','EXPTIME_PER_VISIT',
          'URL_DATA','URL_CITATION','URL_SKY_LAYOUT','URL_DEPTH_LAYOUT','URL_TRANSMISSION_FILT']
types  = ['S254','S64','S64','S64','S64', 
          'S64','S64','S64','f4',
          'f4','f4','f4',
          'f4','f4',
          'f4','f4','f4',
          'f4','f4',
          'S64','i4','S64','f4',
          'f8','f8',
          'S256','S256','S256','S256','S256']

for b,bname in enumerate(bands):
    uniq_id = '{}_{}_{}_{}_{}'.format(field_name,telescope,instr,data_type,bname[:bname.find(' ')])
    values[0] = uniq_id

    tab = table.Table(np.empty(len(colnames)),names=colnames,dtype=types)
    out = open(uniq_id+'.txt','w')

    for i,icol in enumerate(colnames):
        if isinstance(values[i],(list,tuple,np.ndarray)):       
            tab[icol] = values[i][b]
            out.write(" {}:  {}\n".format(icol,values[i][b]))
        else:
            tab[icol] = values[i] 
            out.write(" {}:  {}\n".format(icol,values[i]))
    

    tab.write(uniq_id+'_v2.txt',format='ascii.commented_header',overwrite=True)
    out.close()



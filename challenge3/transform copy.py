
import pandas as pd

import pandas as pd
import numpy
import os
import io

cwd = os.getcwd()

uni = pd.read_csv('{0}/challenge3/universities-intake-enrolment-and-graduates-by-course.csv'.format(cwd))
poly = pd.read_csv('{0}/challenge3/polytechnics-intake-enrolment-and-graduates-by-course.csv'.format(cwd))

#Filter IT only
uniIT = uni.loc[(uni.course=='Information Technology')&(uni.sex=='MF')]
polyIT = poly.loc[(poly.course=='Information Technology')&(poly.sex=='MF')]

#Set index
uniIT = uniIT.set_index(['year','sex','course'])
polyIT = polyIT.set_index(['year','sex','course'])

#transform data to int
uniIT=uniIT.astype({'intake':'str','enrolment':'str','graduates':'str'})
uniIT = uniIT.replace(r',','',regex=True)
uniIT=uniIT.astype({'intake':'int','enrolment':'int','graduates':'int'})

polyIT=polyIT.astype({'intake':'str','enrolment':'str','graduates':'str'})
polyIT = polyIT.replace(r',','',regex=True)
polyIT=polyIT.astype({'intake':'int','enrolment':'int','graduates':'int'})

#add them up
allIT = uniIT.add(polyIT)

#export to csv
allIT.to_csv('{0}/challenge3/allIT.csv'.format(cwd))

print(allIT)
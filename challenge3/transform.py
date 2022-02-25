
import pandas as pd
uni = pd.read_csv('/home/jason/Documents/GitHub/ansible-training/challenge3/universities-intake-enrolment-and-graduates-by-course.csv')
poly = pd.read_csv('/home/jason/Documents/GitHub/ansible-training/challenge3/polytechnics-intake-enrolment-and-graduates-by-course.csv')

uniIT = uni.loc[(uni.course=='Information Technology')&(uni.sex=='MF')]
polyIT = poly.loc[(poly.course=='Information Technology')&(poly.sex=='MF')]

uniIT = uniIT.set_index(['year','sex','course'])
polyIT = polyIT.set_index(['year','sex','course'])

uniIT['intake']=uniIT['intake'].astype(str)
uniIT['intake']=uniIT['intake'].str.replace(',','')

uniIT['enrolment']=uniIT['enrolment'].astype(str)
uniIT['enrolment']=uniIT['enrolment'].str.replace(',','')

uniIT['graduates']=uniIT['graduates'].astype(str)
uniIT['graduates']=uniIT['graduates'].str.replace(',','')

uniIT['intake'] = pd.to_numeric(uniIT['intake'])
uniIT['enrolment'] = pd.to_numeric(uniIT['enrolment'])
uniIT['graduates'] = pd.to_numeric(uniIT['graduates'])

polyIT['intake']=polyIT['intake'].astype(str)
polyIT['intake']=polyIT['intake'].str.replace(',','')

polyIT['enrolment']=polyIT['enrolment'].astype(str)
polyIT['enrolment']=polyIT['enrolment'].str.replace(',','')

polyIT['graduates']=polyIT['graduates'].astype(str)
polyIT['graduates']=polyIT['graduates'].str.replace(',','')

polyIT['intake'] = pd.to_numeric(polyIT['intake'])
polyIT['enrolment'] = pd.to_numeric(polyIT['enrolment'])
polyIT['graduates'] = pd.to_numeric(polyIT['graduates'])

allIT = uniIT.add(polyIT)

allIT.to_csv('/home/jason/Documents/GitHub/ansible-training/challenge3/allIT.csv')
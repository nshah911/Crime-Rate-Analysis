import pymongo
import statistics
import operator
from pprint import pprint
from pymongo import MongoClient
import re
connection = MongoClient()
db=connection.crime
collection=db.crimestats



item=collection.find()
violent=[]
prop=[]
total=[]
pop=[]
Percent={}
#print db.crimestats.find()
states=['ca','ky','ma','md','me','mi','mn','oh','or','pa','ri','sc','sd','tn','tx','ut','va','vt','dc','wa','wi','wv','wy','nv']
for s in range(len(states)):
    for doc in collection.find({"State":states[s]}):
        #print doc['Murder']
        violent1=str(doc['Violent']).strip()
        prop1=str(doc['Property']).strip()
        pop1=str(doc['Population']).strip()
        total1=str(doc['Total']).strip() 
        if(violent1!=''):
         violent2=int(violent1)    
         violent.append(violent2)
        if(prop1!=''):
         prop2=int(prop1)    
         prop.append(prop2)         
        if(pop1!=''):
         pop2=int(pop1)    
         pop.append(pop2)         
        if(total1!=''):
         total2=int(total1)    
         total.append(total2) 


    #print "RES=",statistics.mean(res)
    Percentage=(statistics.mean(total)/statistics.mean(pop))*100
    Percent[states[s]]=Percentage
    print states[s],"Population MEAN=",statistics.mean(pop)
    print states[s],"Total Crime MEAN=",statistics.mean(total)
    print states[s],"violent MEAN=",statistics.mean(violent)
    print states[s],"violent MEDIAN=",statistics.median(violent)    
    print states[s],"violent Standard Deviation=",statistics.stdev(violent)
    print states[s],"Property MEAN=",statistics.mean(prop)
    print states[s],"Property  MEDIAN=",statistics.median(prop)    
    print states[s],"Property  Standard Deviation=",statistics.stdev(prop)
    print states[s],"Population MEAN=",statistics.mean(violent)
    print "***------------------------------------***"
    print states[s],"PERCENTAGE=",Percentage
    print "***------------------------------------***"
    print "=========================="
print "state with highest crimerate(Not SAFE)==>",max(Percent.iteritems(), key=operator.itemgetter(1))[0],"=" ,max(Percent.iteritems(),key=operator.itemgetter(1))[1]
print "state with lowest crimerate(SAFE)==>",min(Percent.iteritems(), key=operator.itemgetter(1))[0],"=" ,min(Percent.iteritems(), key=operator.itemgetter(1))[1]

import matplotlib.pyplot as plt
from numpy.random import normal
import numpy as np
from pylab import *
s = Percent.keys()
n = Percent.values()
pos = arange(len(s))+.5
barh(pos, n, align='center',color='red')
yticks(pos,s)
xlabel('precentage')
ylabel('states')
title('precentage of crime flow in usa')
grid(True)
show()


plt.pie(n, labels=s)
plt.show()
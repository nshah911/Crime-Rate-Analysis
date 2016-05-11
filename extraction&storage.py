import urllib
import re
import io
import string
import json
import pymongo
from pymongo import MongoClient
from collections import Counter
from bs4 import BeautifulSoup
#('us','ca','ky','ma','md','me','mi','mn','nv','ny')
connection = MongoClient()
db=connection.crime
collection=db.crimestats
states=['us','ca','ky','ma','md','me','mi','mn','oh','or','pa','ri','sc','sd','tn','tx','ut','va','vt','dc','wa','wi','wv','wy','nv']
for s in range(len(states)):
        print states[s]
        link1="http://www.disastercenter.com/crime/"+states[s]+"crime.htm"
        print "---------------------------------------------"
        print "Scraping "+link1 + "state data"
        print "---------------------------------------------"
        f1 = urllib.urlopen(link1)

        myfile01 = f1.read()
        soup100 = BeautifulSoup(myfile01)
        #print "main2=",soup100
        soup101=soup100.find('table', width="100%")
        # print "main=",soup101
        #soup303=str(soup101)
        #print "test-",len(soup101.findChildren('tr'))
        rows = soup101.findChildren('tr')
        if rows!=None:
                rows = soup101.findChildren('tr')
                print len(rows[2])
                list =dict()
                for m in range(len(rows)):
                        data= str(rows[m].findChildren('td'))
                        striped_data=re.sub("<.*?>", "", data)
                        print len(striped_data)
                        data1=striped_data.split(' ')
                        #print "sd",data1
                        print len(data1)
                        #print "test=",data1[2]

                        index0=states[s],re.sub("[^0-9]", "", data1[0])
                        print states[s],re.sub("[^0-9]", "", data1[0])
                        index=str(index0)

                        db.crimestats.insert({'State':states[s],
                                        'Year':re.sub("[^0-9]", "", data1[0]),
                                        'Population':re.sub("[^0-9]", "", data1[1]),
                                        #'Population': data1[1].strip(),
                                        'Total':re.sub("[^0-9]", "", data1[2] ),
                                        'Violent':re.sub("[^0-9]", "", data1[3]),
                                        'Property':re.sub("[^0-9]", "", data1[4]),
                                            'Murder':re.sub("[^0-9]", "", data1[5]),
                                        'Rape':re.sub("[^0-9]", "", data1[6]),
                                        'Robbery':re.sub("[^0-9]", "", data1[7]),
                                        'assault':re.sub("[^0-9]", "", data1[8]),
                                        'Burglary':re.sub("[^0-9]", "", data1[9]),
                                        'LTheft':re.sub("[^0-9]", "", data1[10]),
                                        #'VTheft':re.sub("[^0-9a-zA-Z]", "", data1[11])
                                        #'VTheft': data1[11].strip()
                                        })
                                        #db.crimestats.insert(list)
                                        #print "==DATA DUMPED SUCCESSFULLY  TO DB=="
                                       
        else:
                print "====NO TYPE==="
        
#dblist=dict()
#dblist['us']=list
        #db.crimestats.insert(list)
        #print "==DATA DUMPED SUCCESSFULLY  TO DB=="
        #print "dict--",list
#output=open("out.json","w")
#json.dump(list,output, indent=4)
#output.close()


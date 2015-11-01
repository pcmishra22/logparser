#import libraries

from common import *

import sys
#main class start here

class Main:
     
     #global objects
     
     #object of common class
     common = Common()
     
     def __init__(self, date, filename):
          
          self.date = date
          self.filename = filename
          



     #remove records from table

     def removerecords(self):
          #delete all records from event_report table
     
          Main.common.emptyrecords()
          
          

     #this method will start application     
     
     def start(self):
          

          counter=0
          with open(self.filename) as infile:
               
               for line in infile:  
                    
                    counter=counter+1
                    print 'Line Parsed :',counter
                    #check date of the line.............	
                    dt=Main.common.checkvaliddate(line)
                    
                    if( dt == self.date):
                         
                         #checkurl where the data is posted
                         
                         urldata=Main.common.checkurl(line)
                        
                         #check where data will be posted
                         
                         Main.common.checkdetailsurl(urldata,line)

                    else:
                         continue
          
#command line argument passed here
arg=sys.argv

#main object called with date and filepath

objMain = Main(arg[1],arg[2])

#program initiate here

objMain.removerecords()

#start reading files

objMain.start()




#import libraries

from db import *
import re
import urllib 

class Common(object):
     
          #global common database object initiated
          
          db = MyDB('localhost','root','ROOT1234','event')          

          #class initialize
          
          def __init__(self):
                    pass
          
          #check line by date

          def checkvaliddate(self,ln):
                    first_two_letters = ln[:2]
                    strdata=re.split(r'[[]\s*', ln)
                    return strdata[1][:11]	          

          #check url of line

          def checkurl(self,ln):
                    
                    strdata=re.split(r'[]]\s*', ln)
                    return strdata[1][:60]	


          #checkallurl 
 
          def checkdetailsurl(self,urldata,line):

                    #all url is defined here now

                    salesforceschedule='salesforce_schedule.php'
                    salesforceschedulecsvs='salesforce_schedule_csvs.php'
                    leadpost='leadpost.php'
                    bootstrapcss='bootstrap.css'
                    bootstrapjs='bootstrap.js'
                    unabletocontact='unable_to_contact.php'
                    apptajax='apptajax.php'
                    scheduleappointmentaccept='schedule_appointment_accept.php'
                    invictusappt='/invictus/appt/'

                    #decode line variable

                    line=urllib.unquote(line).decode('utf8') 	

                    #check which url is called

                    if(urldata.find(salesforceschedule) != -1):
                              self.salesforceschedulefunction(line)
                    elif(urldata.find(salesforceschedulecsvs) != -1):
                              self.salesforceschedulecsvsfunction(line)
                    elif(urldata.find(leadpost) != -1):
                              self.leadpostfunction(line)				
                    elif(urldata.find(bootstrapcss) != -1):
                              self.bootstrapcssfunction(line)
                    elif(urldata.find(bootstrapjs) != -1):
                              self.bootstrapjsfunction(line)				
                    elif(urldata.find(unabletocontact) != -1):
                              self.unabletocontactfunction(line)				
                    elif(urldata.find(apptajax) != -1):
                              self.apptajaxfunction(line)				
                    elif(urldata.find(scheduleappointmentaccept) != -1):
                              self.scheduleappointmentacceptfunction(line)	
                    elif(urldata.find(invictusappt) != -1):
                              self.invictusapptfunction(line)					
                    else:
                              self.varioururl(line)

          
          #various url
          
          def varioururl(self,ln):
                    try:
                              
                              #split all parameter
                              
                              Common.db.query('''INSERT into event_report (url) values (%s)''', (ln,)) 
                                         
                              
                    except ValueError, Argument:
                              
                              print "Some exception generated.......check the code.........varioururl", Argument
                              
                    else:
                              pass
                              
          
          #salesforce schedule function
                    
          def salesforceschedulefunction(self,ln):
                    try:
                    
                              #split all parameter
                    
                              Common.db.query('''INSERT into event_report (url) values (%s)''', (ln,)) 
                    
                        
                    except ValueError, Argument:
                    
                              print "Some exception generated.......check the code.........salesforceschedulefunction", Argument
                    
                    else:
                              pass



          #salesforce schedule csv function
                    
          def salesforceschedulecsvsfunction(self,ln):
                    try:
                    
                              #split all parameter
                    
                              Common.db.query('''INSERT into event_report (url) values (%s)''', (ln,)) 
                                  
                    
                    except ValueError, Argument:
                    
                              print "Some exception generated.......check the code.........salesforceschedulecsvsfunction", Argument
                    
                    else:
                              pass



          #split line by value
          
          def splitby(self,ln,splitter):
                    strdata=re.split(r'['+splitter+']\s*', ln)
                    return strdata
          
          #lead post function
                    
          def leadpostfunction(self,ln):
                    
                    try:
                              leadbyquestion=self.splitby(ln,'?')
                              
                              leaddata=self.splitby(leadbyquestion[1],'&')
                    
                              #split all parameter
                    
                              f=self.splitby(leaddata[0],'=')
                              l=self.splitby(leaddata[1],'=')
                              p=self.splitby(leaddata[2],'=')
                              r=self.splitby(leaddata[3],'=')
                              t=self.splitby(leaddata[4],'=')
                              pardot=self.splitby(leaddata[5],'=')
                    
                              #SQL query to INSERT a record into the table event_report.
                    
                              Common.db.query('''INSERT into event_report (url,f,l,p,r,t,pardot) values (%s,%s,%s, %s,%s, %s,%s)''', (ln,f[1],l[1],p[1],r[1],t[1],pardot[1])) 
                    
                    
                    except ValueError, Argument:
                    
                              print "Some exception generated.......check the code.........leadpostfunction", Argument
                    
                    else:
                              pass
                    
                    
          #split line by value
          def splitbyspace(self,ln):
                    strdata=re.split(r'[ ]\s*', ln)
                    return strdata[0]



          #invictus app call
                    
          def invictusapptfunction(self,ln):
                    
                    try:
                              leadbyquestion=self.splitby(ln,'?')                                                            
                              leaddata=self.splitby(leadbyquestion[1],'&')                              
                              if(len(leaddata)>1):
                              #split all parameter
                    
                                        cf_leadid=self.splitby(leaddata[0],'=')
                                        cf_new_lead=self.splitby(leaddata[1],'=')
                                        tel=self.splitby(leaddata[2],'=')
                                        fname=self.splitby(leaddata[3],'=')
                                        lname=self.splitby(leaddata[4],'=')
                                        aID=self.splitby(leaddata[5],'=')
                                        aFN=self.splitby(leaddata[6],'=')
                                        aln=self.splitby(leaddata[7],'=')
                                        aLN=self.splitbyspace(aln[1])
                                       
                                        
                                        #SQL query to INSERT a record into the table event_report.
                    
                                        Common.db.query('''INSERT into event_report (url,cf_leadid,cf_new_lead,tel,fname,lname,aID,aFN,aLN) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (ln,cf_leadid[1],cf_new_lead[1],tel[1],fname[1],lname[1],aID[1],aFN[1],aLN)) 
                    		
                    
                              else:
                                        #split all parameter
                    
                                        Common.db.query('''INSERT into event_report (url) values (%s)''', (ln,)) 

                    
                    except ValueError, Argument:
                    
                              print "Some exception generated.......check the code.........invictusapptfunction", Argument
                    
                    
                    else:
                              pass
                    

          #bootstrap css function
                    
                    
          def bootstrapcssfunction(self,ln):
                    
                    try:
                              leadbyquestion=self.splitby(ln,'?')                                                            
                              leaddata=self.splitby(leadbyquestion[1],'&')     
                    
                              
                              if(len(leaddata)>1):
                                        
                                        #split all parameter
                    
                                        cf_leadid=self.splitby(leaddata[0],'=')
                                        cf_new_lead=self.splitby(leaddata[1],'=')
                                        tel=self.splitby(leaddata[2],'=')
                                        fname=self.splitby(leaddata[3],'=')
                                        lname=self.splitby(leaddata[4],'=')
                                        aID=self.splitby(leaddata[5],'=')
                                        aFN=self.splitby(leaddata[6],'=')
                                        aln=self.splitby(leaddata[7],'=')
                                        aLN=self.splitbyspace(aln[1])
                                        aLN=self.splitbydoublequotes(aLN)
                                        
                    
                    
                                        #SQL query to INSERT a record into the table event_report.
                    
                                        Common.db.query('''INSERT into event_report (url,cf_leadid,cf_new_lead,tel,fname,lname,aID,aFN,aLN) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (ln,cf_leadid[1],cf_new_lead[1],tel[1],fname[1],lname[1],aID[1],aFN[1],aLN)) 
                    		
                    
                              else:
                                        #split all parameter
                    
                                        Common.db.query('''INSERT into event_report (url) values (%s)''', (ln,)) 

                    
                    except ValueError, Argument:
                    
                              print "Some exception generated.......check the code.........bootstrapcssfunction", Argument
                    
                    else:
                              pass

          #bootstrap js function
                    
          def bootstrapjsfunction(self,ln):
                    
                    try:
                              leadbyquestion=self.splitby(ln,'?')                                                            
                              leaddata=self.splitby(leadbyquestion[1],'&')     
                              
                              if(len(leaddata)>1):
                                        #split all parameter
                                        cf_leadid=self.splitby(leaddata[0],'=')
                                        cf_new_lead=self.splitby(leaddata[1],'=')
                                        tel=self.splitby(leaddata[2],'=')
                                        fname=self.splitby(leaddata[3],'=')
                                        lname=self.splitby(leaddata[4],'=')
                                        aID=self.splitby(leaddata[5],'=')
                                        aFN=self.splitby(leaddata[6],'=')
                                        aln=self.splitby(leaddata[7],'=')
                                        aLN=self.splitbyspace(aln[1])
                                        aLN=self.splitbydoublequotes(aLN)
                    
                                        #SQL query to INSERT a record into the table event_report.
                    
                                        Common.db.query('''INSERT into event_report (url,cf_leadid,cf_new_lead,tel,fname,lname,aID,aFN,aLN) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (ln,cf_leadid[1],cf_new_lead[1],tel[1],fname[1],lname[1],aID[1],aFN[1],aLN)) 
                    
		
                    
                              else:
                                        #split all parameter
                    
                                        Common.db.query('''INSERT into event_report (url) values (%s)''', (ln,)) 

                    
                    except ValueError, Argument:
                    
                              print "Some exception generated.......check the code.........bootstrapjsfunction", Argument
                    
                    else:
                              pass
                    
          #unable to contact function
                    
          def unabletocontactfunction(self,ln):
                    
                    try:
                    
                              data=self.splitby(ln,'?')
                             
                              leaddata=self.splitby(data[1],'&')
                              leaddata1=self.splitby(data[2],'&')
                              
                             
                              
                              #split all parameter
                              
                              cf_leadid=self.splitby(leaddata[0],'=')
                              transfer_phone=self.splitby(leaddata[1],'=')
                              lead_rec=self.splitby(leaddata[2],'=')
                              lead_first_name=self.splitby(leaddata[4],'=')		
                              lead_last_name=self.splitby(leaddata[5],'=')
                              lead_phone_number=self.splitby(leaddata[6],'=')
                              aID=self.splitby(leaddata[7],'=')
                              aFN=self.splitby(leaddata[8],'=')
                              aLN=self.splitby(leaddata[9],'=')
                              panel=self.splitby(leaddata[10],'=')
                              cf_new_lead=self.splitby(leaddata1[1],'=')	
                              tel=self.splitby(leaddata1[2],'=')	
                              fname=self.splitby(leaddata1[3],'=')	
                              lname=self.splitby(leaddata1[4],'=')	
                              notinterest=self.splitby(leaddata[11],'=')
                              notinterested=self.splitbyspace(notinterest[1])
                              
                              #SQL query to INSERT a record into the table event_report.
                    
                              Common.db.query('''INSERT into event_report (url,cf_leadid,transfer_phone,lead_rec,lead_first_name,lead_last_name,lead_phone_number,aID,aFN,aLN,panel,notinterested,cf_new_lead,tel,fname,lname) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (ln,cf_leadid[1],transfer_phone[1],lead_rec[1],lead_first_name[1],lead_last_name[1],lead_phone_number[1],aID[1],aFN[1],aLN[1],panel[1],notinterested,cf_new_lead[1],tel[1],fname[1],lname[1])) 
                    

                    
                    except ValueError, Argument:
                    
                              print "Some exception generated.......check the code.........unabletocontactfunction", Argument
                    
                    else:
                              pass
                    
          #delete all records

          def emptyrecords(self):
                    Common.db.query('''DELETE FROM event_report''','') 
                    
          
                              
          #split line by value
          
          def splitbydoublequotes(self,ln):
                    strdata=re.split(r'["]\s*', ln)
                    return strdata[0]

                    
          #ajax call of a function
                    
          def apptajaxfunction(self,ln):
                    
                    try:
                              leadbyquestion=self.splitby(ln,'?')                                                            
                              leaddata=self.splitby(leadbyquestion[1],'&')    
                    
                              #split all parameter
                    
                              cf_leadid=self.splitby(leaddata[0],'=')
                              cf_new_lead=self.splitby(leaddata[1],'=')
                              tel=self.splitby(leaddata[2],'=')
                              fname=self.splitby(leaddata[3],'=')
                              lname=self.splitby(leaddata[4],'=')
                              aID=self.splitby(leaddata[5],'=')
                              aFN=self.splitby(leaddata[6],'=')
                              aLN=self.splitby(leaddata[7],'=')
                              transfer_phone=self.splitby(leaddata[8],'=')
                              lead_rec=self.splitby(leaddata[9],'=')
                              lead_first_name=self.splitby(leaddata[11],'=')	
                              lead_last_name=self.splitby(leaddata[12],'=')
                              lead_phone_number=self.splitby(leaddata[13],'=')
                              st=self.splitby(leaddata[17],'=')          
                              start=self.splitbydoublequotes(st[1])
                    
                              #SQL query to INSERT a record into the table event_report.
                    
                              Common.db.query('''INSERT into event_report (url,cf_leadid,cf_new_lead,tel,fname,lname,aID,aFN,aLN,transfer_phone,lead_rec,lead_first_name,lead_last_name,lead_phone_number,start) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (ln,cf_leadid[1],cf_new_lead[1],tel[1],fname[1],lname[1],aID[1],aFN[1],aLN[1],transfer_phone[1],lead_rec[1],lead_first_name[1],lead_last_name[1],lead_phone_number[1],start)) 
                    

                    
                    except ValueError, Argument:
                    
                              print "Some exception generated.......check the code.........apptajaxfunction", Argument
                    
                    else:
                              pass

                    
          # schedule appointment accept function
                    
          def scheduleappointmentacceptfunction(self,ln):
                    
                    try:
                              
                              leadbyquestion=self.splitby(ln,'?')                                                            
                              leaddata=self.splitby(leadbyquestion[1],'&')                        
                              
                              #split all parameter
                    
                              cf_leadid=self.splitby(leaddata[0],'=')
                              cf_new_lead=self.splitby(leaddata[1],'=')
                              tel=self.splitby(leaddata[2],'=')
                              fname=self.splitby(leaddata[3],'=')
                              lname=self.splitby(leaddata[4],'=')
                              aID=self.splitby(leaddata[5],'=')
                              aFN=self.splitby(leaddata[6],'=')
                              aLN=self.splitby(leaddata[7],'=')
                              transfer_phone=self.splitby(leaddata[8],'=')
                              lead_rec=self.splitby(leaddata[9],'=')
                              lead_first_name=self.splitby(leaddata[11],'=')	
                              lead_last_name=self.splitby(leaddata[12],'=')
                              lead_phone_number=self.splitby(leaddata[13],'=')
                              st=self.splitby(leaddata[17],'=')          
                              start=self.splitbydoublequotes(st[1])
                    
                              #SQL query to INSERT a record into the table event_report.
                    
                              Common.db.query('''INSERT into event_report (url,cf_leadid,cf_new_lead,tel,fname,lname,aID,aFN,aLN,transfer_phone,lead_rec,lead_first_name,lead_last_name,lead_phone_number,start) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (ln,cf_leadid[1],cf_new_lead[1],tel[1],fname[1],lname[1],aID[1],aFN[1],aLN[1],transfer_phone[1],lead_rec[1],lead_first_name[1],lead_last_name[1],lead_phone_number[1],start)) 
                    
                    
                    except ValueError, Argument:
                              
                              print "Some exception generated.......check the code.........scheduleappointmentacceptfunction"
                    
                    else:
                              pass

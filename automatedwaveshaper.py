#import wsapi python wrapper
from wsapi import *
from random import *
import random

import matplotlib.pyplot as plt
import numpy as np
import time
#logfile = 'logfileonlyfilter.txt' #textfile where logfile is written
#fl = open(logfile, 'w+')
logfile1 = 'logfile.txt' #textfile where logfile is written
fl2 = open(logfile1, 'w')
carrier=193.1
filter_gap=[0.023, 0.016, 0.013]
attenuation1=[1, 3, 6, 9, 12, 15, 18, 20]
attenuation2=[1, 3, 6, 9]

np.arange(0,1,0.1)
for i in range(0,17):
    t= time.ctime()
    ctype=randint(0,1)
    # only size of the filter
    if (ctype==1):
        #Create the WSP vector Data
        print "\n************Only filter**************\n"
       
        gap=float("{0:.3f}".format(uniform(0.013, 0.025)))
        

            
        lfreq=carrier-gap
        ufreq=carrier+gap
        wsFreq = np.arange(lfreq, ufreq, 0.001)
        wsAttn = np.sin(45*(wsFreq-lfreq)/2/np.pi)
        wsPhase = 0*np.pi*np.cos(5*(wsFreq-lfreq))
        wsPort = np.ones(np.size(wsFreq))
        
        print "Gap= "+str(gap)
        print "attenuation= "+str(wsAttn)
        #Create the WSP file
        WSPfile = open('TrigProfile.wsp', 'w+')
        for x in range(np.size(wsFreq)):
            WSPfile.write("%0.3f\t%0.3f\t%0.3f\t%0.3f\n" % (wsFreq[x], wsAttn[x],
            wsPhase[x], wsPort[x]))    
        WSPfile.close()
        #Read Profile from WSP file
        WSPfile = open('TrigProfile.wsp', 'r')
        profiletext = WSPfile.read()
        WSPfile.close()
        
        #create waveshaper instance and name it "ws1"
        rc = ws_create_waveshaper("ws054395", "SN054395.wsconfig")
        print "ws_create_waveshaper rc="+ws_get_result_description(rc)

        rc = ws_open_waveshaper('ws054395');
        print "Connection to Wsp.hardware= "+ ws_get_result_description(rc)


        #checking ht list of the wavshaper connected
        rc= ws_read_sno('ws054395')
        print "Waveshaper-list: "+ rc
        #compute filter profile from profile text, then load to Waveshaper device
        rc = ws_load_profile("ws054395", profiletext)
        print "ws_load_profile rc="+ws_get_result_description(rc)
        #delete the waveshaper instance
        rc = ws_delete_waveshaper("ws054395")
        print "ws_delete_waveshaper rc="+ws_get_result_description(rc)
        #***************************************
        
        b = "type= " + str(ctype)
        fl2.write("gap=" +" "+str(gap)+" "+str(time.ctime())+" " +str(b)+"\n\n")
    
    # attenuation
    elif(ctype==0):
        #Create the WSP vector Data
        print "\n*********with attenuation********\n"
        gap=float(choice(filter_gap))
        lfreq=carrier-gap
        ufreq=carrier+gap
        wsFreq = np.arange(lfreq, ufreq, 0.001)
        if gap==0.013:
            shuffle(attenuation2)
            att=int(choice(attenuation2))    
            
            wsPhase = 0*np.pi*np.cos(5*(wsFreq-lfreq))
            wsAttn = np.sin(45*(wsFreq-lfreq)/2/np.pi)+att
            wsPort = np.ones(np.size(wsFreq))
        else:
            att=int(choice(attenuation1))
            wsAttn = np.sin(45*(wsFreq-lfreq)/2/np.pi)+att        
            wsPhase = 0*np.pi*np.cos(5*(wsFreq-lfreq))
            wsPort = np.ones(np.size(wsFreq))
        #Create the WSP file
        print "Gap="+str(gap)
        print "selectedAttenutation= "+str(att)
        print "attenuation= "+str(wsAttn)
        
        WSPfile = open('TrigProfile.wsp', 'w+')
        for x in range(np.size(wsFreq)):
            WSPfile.write("%0.3f\t%0.3f\t%0.3f\t%0.3f\n" % (wsFreq[x], wsAttn[x],
            wsPhase[x], wsPort[x]))
        WSPfile.close()
        #Read Profile from WSP file
        WSPfile = open('TrigProfile.wsp', 'r')
        profiletext = WSPfile.read()
        WSPfile.close()
        #create waveshaper instance a
        rc = ws_create_waveshaper("ws054395", "SN054395.wsconfig")
        print "ws_create_waveshaper rc="+ws_get_result_description(rc)
        #connection the waveshaper
        rc = ws_open_waveshaper('ws054395');
        print "Connection to Wsp.Hardware= "+ ws_get_result_description(rc)

      
        #checking ht list of the wavshaper connected
        rc= ws_read_sno('ws054395')
        print "Waveshaper-list: "+ rc
        #compute filter profile from profile text, then load to Waveshaper device
        rc = ws_load_profile("ws054395", profiletext)
        print "ws_load_profile rc="+ws_get_result_description(rc)
        #delete the waveshaper instance
        rc = ws_delete_waveshaper("ws054395")
        print "ws_delete_waveshaper rc="+ws_get_result_description(rc)
        
        b = "type= " + str(ctype)
        fl2.write("gap="+ " "+str(gap)+" "+str(time.ctime())+" " +str(b)+" "+ "attenuation=" + " "+str(att)+"\n\n")
    time.sleep(3600)
        
        

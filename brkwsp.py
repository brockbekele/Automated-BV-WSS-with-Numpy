#import wsapi python wrapper
from wsapi import *
#create waveshaper instance and name it "ws1"
rc = ws_create_waveshaper("ws1", "testdata/SN007090.wsconfig")
print "ws_create_waveshaper rc="+ws_get_result_description(rc)
#read profile from WSP file
WSPfile = open('testdata/test 100GHz 4ports alternating.wsp', 'r')
profiletext = WSPfile.read()
#compute filter profile from profile text, then load to Waveshaper device
rc = ws_load_profile("ws1", profiletext)
print "ws_load_profile rc="+ws_get_result_description(rc)
#delete the waveshaper instance
rc = ws_delete_waveshaper("ws1")
print "ws_delete_waveshaper rc="+ws_get_result_description(rc)

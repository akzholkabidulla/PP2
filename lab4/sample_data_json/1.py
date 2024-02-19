import json 
 
file=open("sample_data.json") 
 
sample_data_json=file.read() 
 
sample_data=json.loads(sample_data_json) 
 
print("""Interface Status 
================================================================================ 
DN                                                 Description           Speed    MTU   
-------------------------------------------------- --------------------  ------  ------""") 
 
 
for i in sample_data["imdata"]: 
   dn_key=i["l1PhysIf"]["attributes"]["dn"] 
   descr_key=i["l1PhysIf"]["attributes"]["descr"] 
   speed_key=i["l1PhysIf"]["attributes"]["speed"] 
   mtu_key=i["l1PhysIf"]["attributes"]["mtu"] 
   print(dn_key,"                     ",descr_key,"      ",speed_key," ",mtu_key)

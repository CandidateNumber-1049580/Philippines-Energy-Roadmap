#!/usr/bin/env python
# coding: utf-8

# In[16]:

#This code has been dveloped by SAREEL to identify flaws in the Philippines' 
#planned transmsion grid.

import pandapower as pp
import numpy as np
from pandapower import plotting as plot
import matplotlib.pyplot as plt
import seaborn
import pandas as pd


# In[17]:


#Create Network and Buses
net = pp.create_empty_network()

#Define Constants

DBV=350 #Demand Bus Voltage in kV, just for now can be changed later
GBV=350 #Generation Bus Voltage in kV, just for now can be changed later
Power_factor = 0.8
Theta = np.arccos(Power_factor)
P2Q = np.tan(Theta)
R_230=0.0015
X_230=0.00023
C_230=100
Max_230=20.006

#Create Demand Buses

Region1Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 1 Bus")
Region2Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 2 Bus")
Region3Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 3 Bus")
NCRBus= pp.create_bus(net, vn_kv=DBV, name = "NCR Bus")
Region4ABus= pp.create_bus(net, vn_kv=DBV, name = "Region 4A Bus")
CARBus= pp.create_bus(net, vn_kv=DBV, name = "CAR Bus")
Region4B1Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 4B1 Bus")
Region4B2Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 4B2 Bus")
Region5Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 5 Bus")
Region6Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 6 Bus")
Region7Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 7 Bus")
Region8Bus= pp.create_bus(net, vn_kv=DBV, name = "Region 8 Bus")
Mindanao1Bus= pp.create_bus(net, vn_kv=DBV, name = "Mindanao 1 Bus")
Mindanao2Bus= pp.create_bus(net, vn_kv=DBV, name = "Mindanao 2 Bus")
Mindanao3Bus= pp.create_bus(net, vn_kv=DBV, name = "Mindanao 3 Bus")

#Create Generation Zone Buses

Zone1Bus= pp.create_bus(net, vn_kv=GBV, name = "Zone 1 Bus")
Zone2Bus= pp.create_bus(net, vn_kv=GBV, name = "Zone 2 Bus")
Zone3Bus= pp.create_bus(net, vn_kv=GBV, name = "Zone 3 Bus")
Zone4Bus= pp.create_bus(net, vn_kv=GBV, name = "Zone 4 Bus")
Zone5Bus= pp.create_bus(net, vn_kv=GBV, name = "Zone 5 Bus")
Zone6Bus= pp.create_bus(net, vn_kv=GBV, name = "Zone 6 Bus")
Zone7Bus= pp.create_bus(net, vn_kv=GBV, name = "Zone 7 Bus")
Zone8Bus= pp.create_bus(net, vn_kv=GBV, name = "Zone 8 Bus")

#Create Lines
L1_Length=200
pp.create_line_from_parameters(net,from_bus=Region1Bus, to_bus=Zone1Bus ,length_km=L1_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L1")
L2_Length=150
pp.create_line_from_parameters(net,from_bus=Region1Bus, to_bus=CARBus ,length_km=L2_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L2")
L3_Length=150
pp.create_line_from_parameters(net,from_bus=Zone1Bus, to_bus=Region2Bus ,length_km=L3_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L3")
L4_Length=150
pp.create_line_from_parameters(net,from_bus=Zone1Bus, to_bus=Region2Bus ,length_km=L4_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L4")
L5_Length=100
pp.create_line_from_parameters(net,from_bus=Region2Bus, to_bus=CARBus ,length_km=L5_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L5")
L6_Length=120
pp.create_line_from_parameters(net,from_bus=Region2Bus, to_bus=Zone2Bus ,length_km=L6_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L6")
L7_Length=50
pp.create_line_from_parameters(net,from_bus=CARBus, to_bus=Zone2Bus ,length_km=L7_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L7")
L8_Length=220
pp.create_line_from_parameters(net,from_bus=Zone2Bus, to_bus=Region3Bus ,length_km=L8_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=10,name = "L8")
L9_Length=70
pp.create_line_from_parameters(net,from_bus=Zone2Bus, to_bus=Region3Bus ,length_km=L9_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L9")
L10_Length=36
pp.create_line_from_parameters(net,from_bus=Region3Bus, to_bus=NCRBus ,length_km=L10_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L10")
#L8b_Length=220
#pp.create_line_from_parameters(net,from_bus=Zone2Bus, to_bus=Region3Bus ,length_km=L8_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L8b")
L9b_Length=70
pp.create_line_from_parameters(net,from_bus=Zone2Bus, to_bus=Region3Bus ,length_km=L9_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L9b")
L10b_Length=36
pp.create_line_from_parameters(net,from_bus=Region3Bus, to_bus=NCRBus ,length_km=L10_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L10b")
L11_Length=50
pp.create_line_from_parameters(net,from_bus=NCRBus, to_bus=Region4ABus ,length_km=L11_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L11")
#pp.create_line_from_parameters(net,from_bus=NCRBus, to_bus=Region4ABus ,length_km=L11_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L11b")
L12_Length=200
pp.create_line_from_parameters(net,from_bus=Zone2Bus, to_bus=Region4ABus ,length_km=L12_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L12")
L13_Length=80
pp.create_line_from_parameters(net,from_bus=Region4ABus, to_bus=Region4B1Bus ,length_km=L13_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L13")
L14_Length=200
pp.create_line_from_parameters(net,from_bus=Region4ABus, to_bus=Region5Bus ,length_km=L14_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L14")
L15_Length=30
pp.create_line_from_parameters(net,from_bus=Region4B1Bus, to_bus=Zone4Bus ,length_km=L15_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L15")
L16_Length=340
pp.create_line_from_parameters(net,from_bus=Zone4Bus, to_bus=Region4B2Bus,length_km=L16_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L16")
L17_Length=270
pp.create_line_from_parameters(net,from_bus=Zone4Bus, to_bus=Zone6Bus ,length_km=L17_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L17")
L18_Length=60
pp.create_line_from_parameters(net,from_bus=Zone6Bus, to_bus=Region6Bus ,length_km=L18_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L18")
#pp.create_line_from_parameters(net,from_bus=Zone6Bus, to_bus=Region6Bus ,length_km=L18_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L18b")
L19_Length=300
pp.create_line_from_parameters(net,from_bus=Region6Bus, to_bus=Mindanao3Bus ,length_km=L19_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L19")
L20_Length=100
pp.create_line_from_parameters(net,from_bus=Region6Bus, to_bus=Region7Bus ,length_km=L20_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L20")
L21_Length=260
pp.create_line_from_parameters(net,from_bus=Region7Bus, to_bus=Mindanao3Bus  ,length_km=L21_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L21")
L22_Length=160
pp.create_line_from_parameters(net,from_bus=Region7Bus, to_bus=Region8Bus  ,length_km=L22_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=10,name = "L22")
L23_Length=170
pp.create_line_from_parameters(net,from_bus=Region8Bus, to_bus=Zone3Bus  ,length_km=L23_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L23")
L24_Length=400
pp.create_line_from_parameters(net,from_bus=Region7Bus, to_bus=Zone3Bus  ,length_km=L24_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L24")
L25_Length=34
pp.create_line_from_parameters(net,from_bus=Mindanao3Bus, to_bus=Zone7Bus  ,length_km=L25_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L25")
L26_Length=200
pp.create_line_from_parameters(net,from_bus=Zone7Bus, to_bus=Zone8Bus  ,length_km=L26_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L26")
L27_Length=280
pp.create_line_from_parameters(net,from_bus=Zone7Bus, to_bus=Zone8Bus  ,length_km=L27_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L27")
L28_Length=410
pp.create_line_from_parameters(net,from_bus=Zone7Bus, to_bus=Mindanao2Bus  ,length_km=L28_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L28")
L29_Length=50
pp.create_line_from_parameters(net,from_bus=Zone8Bus, to_bus=Mindanao1Bus  ,length_km=L29_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L29")
L30_Length=150
pp.create_line_from_parameters(net,from_bus=Zone8Bus, to_bus=Mindanao2Bus  ,length_km=L30_Length, r_ohm_per_km =R_230, x_ohm_per_km =X_230,c_nf_per_km =C_230, max_i_ka=Max_230,name = "L30")

#Create Slack Bus

pp.create_ext_grid(net, bus=Zone2Bus , vm_pu=1.02, name="Zone 2 Slack Bus")



#Insert Excel for Demand

DemandExcel=pd.read_excel('PandaPower2.xlsx', sheet_name='Daily Demand 2050')
Region1=DemandExcel['Region I (ILOCOS Region)']
Region2=DemandExcel['Region II (Cagayan Valley)']
Region3=DemandExcel['Region III (Central Luzon)']
NCR=DemandExcel['National Capital Region']
Region4A=DemandExcel['Region IV-A (Calabrazon)']
CAR=DemandExcel['Cordillera Administrative Region']
Region4B1=DemandExcel['Region IV-B (Mimaropa) 1']
Region4B2=DemandExcel['Region IV-B (Mimaropa) 2']
Region5=DemandExcel['Region V (Bicol Region)']
Region6=DemandExcel['Region VI (Western Visayas)']
Region7=DemandExcel['Region VII (Central Visayas)']
Region8=DemandExcel['Region VIII (Eastern Visayas)']
Mindanao1=DemandExcel['Mindanao 1']
Mindanao2=DemandExcel['Mindanao 2']
Mindanao3=DemandExcel['Mindanao 3']

#Insert Excel for Generation

GenExcel=pd.read_excel('PandaPower2.xlsx', sheet_name='Daily generation 2050')
Zone1=GenExcel['Zone 1']
Zone2=GenExcel['Zone 2']
Zone3=GenExcel['Zone 3']
Zone4=GenExcel['Zone 4']
Zone5=GenExcel['Zone 5']
Zone6=GenExcel['Zone 6']
Zone7=GenExcel['Zone 7']
Zone8=GenExcel['Zone 8']
Zone1


# In[24]:


#Define Demand which iterates

n = 13

    #For Demand
Region1Demand=Region1.iloc[n]
Region2Demand=Region2.iloc[n]
Region3Demand=Region3.iloc[n]
NCRDemand=NCR.iloc[n]
Region4ADemand=Region4A.iloc[n]
CARDemand=CAR.iloc[n]
Region4B1Demand=Region4B1.iloc[n]
Region4B2Demand=Region4B1.iloc[n]
Region5Demand=Region5.iloc[n]
Region6Demand=Region6.iloc[n]
Region7Demand=Region7.iloc[n]
Region8Demand=Region8.iloc[n]
Mindanao1Demand=Mindanao1.iloc[n]
Mindanao2Demand=Mindanao2.iloc[n]
Mindanao3Demand=Mindanao3.iloc[n]

#For Generation

Zone1Gen=Zone1.iloc[n]
Zone2Gen=Zone2.iloc[n]
Zone3Gen=Zone3.iloc[n]
Zone4Gen=Zone4.iloc[n]
Zone5Gen=Zone5.iloc[n]
Zone6Gen=Zone6.iloc[n]
Zone7Gen=Zone7.iloc[n]
Zone8Gen=Zone8.iloc[n]

#Demand Load Creation
pp.create_load(net, bus= Region1Bus, p_mw=Region1Demand,q_mvar= Region1Demand*P2Q, name="Region 1 Demand")
pp.create_load(net, bus= Region2Bus, p_mw=Region2Demand,q_mvar= Region2Demand*P2Q, name="Region 2 Demand")
pp.create_load(net, bus= Region3Bus, p_mw=Region3Demand,q_mvar= Region3Demand*P2Q, name="Region 3 Demand")
pp.create_load(net, bus= NCRBus, p_mw=NCRDemand,q_mvar= NCRDemand*P2Q, name="NCR Demand")
pp.create_load(net, bus= Region4ABus, p_mw=Region4ADemand,q_mvar= Region4ADemand*P2Q, name="Region 4A Demand")
pp.create_load(net, bus= CARBus, p_mw=CARDemand,q_mvar= CARDemand*P2Q, name="CAR Demand")
pp.create_load(net, bus= Region4B1Bus, p_mw=Region4B1Demand,q_mvar= Region4B1Demand*P2Q, name="Region 4B1 Demand")
pp.create_load(net, bus= Region4B2Bus, p_mw=Region4B2Demand,q_mvar= Region4B2Demand*P2Q, name="Region 4B2 Demand")
pp.create_load(net, bus= Region5Bus, p_mw=Region5Demand,q_mvar= Region5Demand*P2Q, name="Region 5 Demand")
pp.create_load(net, bus= Region6Bus, p_mw=Region6Demand,q_mvar= Region6Demand*P2Q, name="Region 6 Demand")
pp.create_load(net, bus= Region7Bus, p_mw=Region7Demand,q_mvar= Region7Demand*P2Q, name="Region 7 Demand")
pp.create_load(net, bus= Region8Bus, p_mw=Region8Demand,q_mvar= Region8Demand*P2Q, name="Region 8 Demand")
pp.create_load(net, bus= Mindanao1Bus, p_mw=Mindanao1Demand,q_mvar= Mindanao1Demand*P2Q, name="Mindanao 1 Demand")
pp.create_load(net, bus= Mindanao2Bus, p_mw=Mindanao2Demand,q_mvar= Mindanao2Demand*P2Q, name="Mindanao 2 Demand")
pp.create_load(net, bus= Mindanao3Bus, p_mw=Mindanao3Demand,q_mvar= Mindanao3Demand*P2Q, name="Mindanao 3 Demand")

#Generation Source Creation

pp.create_sgen(net,bus=Zone1Bus, p_mw = Zone1Gen, q_mvar =   Zone1Gen*P2Q , name = "Zone 1 Gen" )
pp.create_sgen(net,bus=Zone2Bus, p_mw = Zone2Gen, q_mvar =   Zone2Gen*P2Q , name = "Zone 2 Gen" )
pp.create_sgen(net,bus=Zone3Bus, p_mw = Zone3Gen, q_mvar =   Zone3Gen*P2Q , name = "Zone 3 Gen" )
pp.create_sgen(net,bus=Zone4Bus, p_mw = Zone4Gen, q_mvar =   Zone4Gen*P2Q , name = "Zone 4 Gen" )
pp.create_sgen(net,bus=Zone5Bus, p_mw = Zone5Gen, q_mvar =   Zone5Gen*P2Q , name = "Zone 5 Gen" )
pp.create_sgen(net,bus=Zone6Bus, p_mw = Zone6Gen, q_mvar =   Zone6Gen*P2Q , name = "Zone 6 Gen" )
pp.create_sgen(net,bus=Zone7Bus, p_mw = Zone7Gen, q_mvar =   Zone7Gen*P2Q , name = "Zone 7 Gen" )
pp.create_sgen(net,bus=Zone8Bus, p_mw = Zone8Gen, q_mvar =   Zone1Gen*P2Q , name = "Zone 8 Gen" )

pp.runpp(net)
 
pp.to_excel(net, 'This 7thFeb2050_Government_' + str(n) + 'planned_lines.xlsx')

# In[25]:


print(net.res_line)



# In[ ]:





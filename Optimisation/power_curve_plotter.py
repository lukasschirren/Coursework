#%%
import numpy as np
import matplotlib.pyplot as plt



def power_curve(wind_speed_vec,power_vec,cut_in,rated,cut_out, rated_power):
    
    
    for index, speed in enumerate(wind_speed_vec):
        if speed<cut_in:
            power_vec[index]=0
        elif cut_in<=speed<=rated:
            power_vec[index]=rated_power*((speed-cut_in)/(rated-cut_in))**3
        elif rated<speed<=cut_out:
            power_vec[index]=rated_power
        elif speed>cut_out:
            power_vec[index]=0
    return wind_speed_vec,power_vec


def C_p_calculator(wind_speed_vec, power_vec, rho, A):
    C_p_vec=power_vec/(0.5*rho*A*wind_speed_vec**3)
    return wind_speed_vec, C_p_vec

def C_t_calculator(C_p_vec, TSR=8):
    return C_p_vec/TSR

def generate_data(wind_speed_vec,power_vec,cut_in,rated,cut_out, rated_power, rho, diameter):
    wind_speed_vec,power_vec=power_curve(wind_speed_vec,power_vec,cut_in,rated,cut_out, rated_power)
    A=np.pi*(diameter/2)**2
    wind_speed_vec,C_p_vec=C_p_calculator(wind_speed_vec, power_vec, rho, A)
    C_t_vec=C_t_calculator(C_p_vec)
    #script expects wind power in GW not MW so divide wind_power by 1000
    power_vec=power_vec/1000
    return wind_speed_vec, power_vec, C_p_vec, C_t_vec







# %%

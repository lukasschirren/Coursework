#%%
from py_wake.wind_turbines.power_ct_functions import PowerCtTabular
from py_wake.wind_turbines import WindTurbine
import numpy as np
from power_curve_plotter import generate_data

#initialise vectors to hold data
WIND_SPEED_VEC=np.linspace(0,50,101)
POWER_VEC=np.full(len(WIND_SPEED_VEC), np.nan)
RHO=1.293

diameter=144
hub_height=105
cut_in=3
rated=9.2
cut_out=18
rated_power=3*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
SuzlonS144 = WindTurbine(name='SuzlonS144',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    wind_speed=wind_speed_vec,
                    power=power_vec)

diameter=160
hub_height=120
cut_in=3
rated=12
cut_out=20
rated_power=5.2*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
W2E160 = WindTurbine(name='W2E160',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    )

diameter=150
hub_height=105 #change this
cut_in=3
rated=11
cut_out=25
rated_power=6*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
VestasV150 = WindTurbine(name='VestasV150',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    )

diameter=150
hub_height=160 #change this
cut_in=3
rated=10.5
cut_out=25
rated_power=3.5*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
VestasV136 = WindTurbine(name='VestasV136',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    )

diameter=136
hub_height=120
cut_in=3
rated=9.2
cut_out=18
rated_power=3*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
Suzlon144 = WindTurbine(name='Suzlon144',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    )

diameter=160
hub_height=120 
cut_in=3
rated=11
cut_out=25
rated_power=5.56*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
Enercon160 = WindTurbine(name='Enercon144',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    )

diameter=175
hub_height=160
cut_in=3
rated=12.5
cut_out=22
rated_power=6.1*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
Vensys136 = WindTurbine(name='Vensys136',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    )

diameter=137
hub_height=134
cut_in=3
rated=12.5
cut_out=25
rated_power=3.4*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
GE3MW = WindTurbine(name='GE3MW',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    )

diameter=131
hub_height=134
cut_in=3
rated=11.5
cut_out=25
rated_power=3.6*10**6
wind_speed_vec, power_vec, C_p_vec, C_t_vec=generate_data(WIND_SPEED_VEC, POWER_VEC, cut_in=cut_in,rated_power=rated_power, rated=rated, cut_out=cut_out,rho=RHO,diameter=diameter)
Nordex = WindTurbine(name='Nordex',
                    diameter=diameter,
                    hub_height=hub_height,
                    powerCtFunction=PowerCtTabular(wind_speed_vec,power_vec,'kW',C_t_vec),
                    )


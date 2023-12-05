#%%
from py_wake.site import UniformWeibullSite
from py_wake import NOJ,BastankhahGaussian, IEA37SimpleBastankhahGaussian
from py_wake.wind_turbines import WindTurbine
from py_wake.wind_turbines.power_ct_functions import PowerCtTabular
import numpy as np
import matplotlib.pyplot as plt
from site_creation import generate_staggered_rotated_points, generate_square_grid_rotated
from matplotlib.ticker import ScalarFormatter
from wind_turbines import SuzlonS144, W2E160, VestasV150, VestasV136, Suzlon144, Enercon160, Vensys136, GE3MW, Nordex


#site setup parameters
INDEX=2
rows=4
columns=5
turbine_model=SuzlonS144
distance_between_points=turbine_model.diameter()
#angle_degrees=-33.6 optimal angle
angle_degrees=-57.3
rotation_point=(0,0)
diameter=100
wind_turbine_list=[SuzlonS144, W2E160, VestasV150, VestasV136, Suzlon144, Enercon160, Vensys136, GE3MW, Nordex]
turbine_model=wind_turbine_list[INDEX]
method=IEA37SimpleBastankhahGaussian

# returns x,y coordinates for the wind turbines, where they 
# have been setup in staggered rows, these rows can then be 
# rotated around a point by a set amount for optimal setup
#x,y= generate_staggered_rotated_points(rows, columns, diameter,angle_degrees)
#x,y=generate_staggered_rotated_points(rows, columns, 3*distance_between_points, 3*distance_between_points,angle_degrees)

x,y=generate_square_grid_rotated(rows, columns,3*distance_between_points, 7*distance_between_points, angle_degrees)

#specifying the necessary parameters for the UniformWeibullSite object
# 0: '160', 1:'105', 2:'120', 3:'134'
# arr_scale[0] acceses therefore turbine with height 60.
turbine_wind_dict={SuzlonS144:0, W2E160:2, VestasV150:1, VestasV136:1, Suzlon144:0, Enercon160:2, Vensys136:0, GE3MW:3, Nordex:3}

arr_scale = [[3.92121946e-01, 1.94889903e+00, 1.20786851e+00, 1.35592443e+00,
        2.93133805e+00, 2.29210661e+00, 2.00461918e+00, 1.71882566e+00],
       [2.95497141e-01, 1.94379540e+00, 1.21150870e+00, 1.34817449e+00,
        2.93869639e+00, 2.29808800e+00, 2.00675576e+00, 1.72250535e+00],
       [2.95332333e-01, 1.91446417e+00, 1.23353366e+00, 1.31454037e+00,
        2.92995831e+00, 2.28945118e+00, 1.99018300e+00, 1.73384782e+00],
       [5.97073335e-01, 5.05534606e+01, 2.52881099e-01, 6.71417823e+00,
        1.59188532e+07, 1.57966673e-01, 8.33225582e-01, 7.57076615e-01]]

arr_shape = [[7.90580189e-01, 7.40325048e+00, 3.96014434e+00, 5.49453262e+00,
        1.66388730e+01, 1.35633490e+01, 1.10289047e+01, 7.61278307e+00],
       [1.35106671e+00, 7.55726665e+00, 4.06287200e+00, 5.59721331e+00,
        1.70268656e+01, 1.38806991e+01, 1.12803292e+01, 7.79636699e+00],
       [1.37307509e+00, 7.55943584e+00, 4.19680339e+00, 5.55732389e+00,
        1.72479706e+01, 1.40567206e+01, 1.13685356e+01, 7.96510521e+00],
       [1.82029111e+02, 4.83799253e+02, 2.07409832e+01, 6.76282397e+01,
        1.50263579e+08, 9.90614578e+00, 1.93797057e+01, 1.64789570e+01]]

freq_param=[0.19351883659681668,0.09091950074430322,0.07832360013740983,0.023359670216420474,0.19122867285010878,0.19168670559945036,0.12813466162830642,0.10282835222718424]
site = UniformWeibullSite(p_wd = freq_param,# sector frequencies
                          a = arr_shape[turbine_wind_dict[turbine_model]],  # Weibull scale parameter
                          k = arr_scale[turbine_wind_dict[turbine_model]],     # Weibull shape parameter
                          ti =100)             # turbulence intensity, optional



#wind_distribution = NOJ(site,turbine_model)
site_obj = method(site,turbine_model)
#wind_distribution=BastankhahGaussian(site, turbine_model)

simulationResult = site_obj(x,y)
simulationResult.aep()
print(f'Total AEP for {turbine_model.name()}:', simulationResult.aep().sum())
print ("Total AEP: %f GWh"%simulationResult.aep().sum())


#%%

plt.figure()
aep = simulationResult.aep()
turbine_model.plot(x,y)
c =plt.scatter(x, y, c=aep.sum(['wd','ws']))
plt.colorbar(c, label='AEP [GWh]')
plt.title('AEP of each turbine')
plt.xlabel('x [m]')
plt.ylabel('[m]')
plt.legend()

plt.figure()
aep.sum(['wt','wd']).plot()
plt.xlabel("Wind speed [m/s]")
plt.ylabel("AEP [GWh]")
plt.title('AEP vs wind speed')

plt.figure()
aep.sum(['wt','ws']).plot()
plt.xlabel("Wind direction [deg]")
plt.ylabel("AEP [GWh]")
plt.title('AEP vs wind direction')







#%%
rotation_points=np.linspace(-90,90,100)
length=len(rotation_points)
AEP_vec=np.zeros(length)

for index,theta in enumerate(rotation_points):
    
    #x,y= generate_square_grid_rotated(rows, columns, 3*distance_between_points, 7*distance_between_points,theta)
    x,y= generate_staggered_rotated_points(rows, columns, 3*distance_between_points, 7*distance_between_points,theta)
   
    simulationResult = site_obj(x,y)
    simulationResult.aep()
    AEP_vec[index]=simulationResult.aep().sum()
#%%
plt.plot(rotation_points, AEP_vec)
plt.xlabel('Face Angle (Degrees)')
plt.ylabel('Annualised Energy Production (GWh)')
ax = plt.gca()
# Create a ScalarFormatter with useOffset set to False
formatter = ScalarFormatter(useOffset=False)
# Apply the formatter to the x-axis and y-axis
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)
plt.axvline(x=rotation_points[np.argmax(AEP_vec)], label=f'optimum face angle {np.round(rotation_points[np.argmax(AEP_vec)],decimals=1)}', color='black')
plt.legend()
plt.show()

#%%
wind_speed = 10
wind_direction = 135
plt.figure()
flow_map = simulationResult.flow_map(ws=wind_speed, wd=wind_direction)
plt.figure(figsize=(18,10))
flow_map.plot_wake_map()
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Wake map for' + f' {wind_speed} m/s and {wind_direction} deg')
# %%
plt.figure()
start=0
stop=50
speed=wind_turbine_list[0]
speed=speed.wind_speed[start:stop]
for val in wind_turbine_list:
    Power_values=val.power[start:stop]
    
    plt.plot(speed, Power_values, label=val.name())
    print('speed',speed)
    print('power',Power_values)

print('speed',speed)
print('power',Power_values)
plt.legend()
plt.xlabel('Wind speed (m/s)')
plt.ylabel('Power Output (W)')
plt.title('Power curves for different wind turbine models')
plt.show()
# %%
wind_speed = 10
wind_direction = 225

plt.figure()
flow_map = simulationResult.flow_map(ws=wind_speed, wd=wind_direction)
plt.figure(figsize=(18,10))
flow_map.plot_wake_map()
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('Wake map for' + f' {wind_speed} m/s and {wind_direction} deg')

# %%

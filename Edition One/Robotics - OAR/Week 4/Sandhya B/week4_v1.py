import sim
import sys
import numpy as np
#import time

# just in case, close all opened connections
sim.simxFinish(-1)
#establish connection with coppeliasim remote server
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)

if clientID!=-1:  #check if client connection successful
    print('Connected to remote API server')
    
else:
    print('Connection not successful')
    sys.exit('Could not connect')


#retrieve motor  handles
errorCode,left_motor_handle=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',sim.simx_opmode_oneshot_wait)
errorCode,right_motor_handle=sim.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',sim.simx_opmode_oneshot_wait)

errorCode,sensor_handle2 = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor2',sim.simx_opmode_oneshot_wait )
errorCode,sensor_handle5 = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor5',sim.simx_opmode_oneshot_wait )
errorCode,sensor_handle7 = sim.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor7',sim.simx_opmode_oneshot_wait )


while(1):
    _,dS2,dP2,_,_ = sim.simxReadProximitySensor(clientID, sensor_handle2 , sim.simx_opmode_streaming)
    d2 = np.linalg.norm(dP2)
    _,dS7,dP7,_,_ = sim.simxReadProximitySensor(clientID, sensor_handle7 , sim.simx_opmode_streaming)
    d7 = np.linalg.norm(dP7)
    _,dS5,dP5,_,_ = sim.simxReadProximitySensor(clientID, sensor_handle5 , sim.simx_opmode_streaming)
    d5 = np.linalg.norm(dP5)
    
    if(d5<0.5 and dS5 == True):
        print('5')
        l = -1
        r = 0
    elif(d2<0.3 and dS2 == True):
        print('2')
        l=-1;
        r=0;
    elif(d7<0.3 and dS7 == True):
        print('7')
        l=-1;
        r=0;
    else:
        l = 1;
        r = 1;
 
    errorCode=sim.simxSetJointTargetVelocity(clientID,left_motor_handle,l, sim.simx_opmode_oneshot_wait)
    errorCode=sim.simxSetJointTargetVelocity(clientID,right_motor_handle,r, sim.simx_opmode_oneshot_wait)
 
 
 
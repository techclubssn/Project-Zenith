#import libraries
import sim
import sys
import time

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

# enter your code here. a sample of how to set the target joint velocity is given below, you can change that.
errorCode=sim.simxSetJointTargetVelocity(clientID,left_motor_handle,10, sim.simx_opmode_oneshot_wait)
errorCode=sim.simxSetJointTargetVelocity(clientID,right_motor_handle,10, sim.simx_opmode_oneshot_wait)


import time
time.sleep(5)
while(1):
 print('Enter angular velocity for left wheel:')
 l=int(input())
 print('Enter angular velocity for right wheel:')
 r=int(input())
 errorCode=sim.simxSetJointTargetVelocity(clientID,left_motor_handle,l, sim.simx_opmode_oneshot_wait)
 errorCode=sim.simxSetJointTargetVelocity(clientID,right_motor_handle,r, sim.simx_opmode_oneshot_wait)
 time.sleep(5)


        
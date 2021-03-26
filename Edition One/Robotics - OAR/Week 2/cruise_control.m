
%defining parameters of the vehicle
m = 1000; % mass of vehicle
b = 50; % damping coeffecient
r = 10; % reference speed. this is the value the system is going to try to achieve

% modelling a vehicle as system in s-domain
%this line defines the value s you use in the transfer function
s = tf('s');
%same as the transfer function for the vehicle
P_cruise = 1/(m*s + b);

%now try to model the pid controller as a system like above.

s = tf('s');
% you have to complete C like line 11
C = 

% this line will multiply the transfer functions of the two systems giving
% the overall response of the system.
T = feedback(C*P_cruise,1);

%these lines plot the systems behaviour. The plotted value is the velocity
%that your modelled vehicle is exhibiting. You can view if it tracks the
%reference value you set. 
t = 0:0.1:100;
step(r*T,t)

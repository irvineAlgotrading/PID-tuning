# PID tuning
tune a PI or PID loop using the Ziegler-Nichols tuning method

set Kp, Ki, and Kd to zero

slowly increase Kp a small amount, say 0.1 at a time, and between adjustments watch the response to see if the system begins to oscillate with constant amplitude. 
the oscillation should be consistent and perpetual, without tapering off or growing wildly out of control

once constant oscillation is observed, record the time between oscillations (peak to peak)
the peak could be a max spike in pressure, temperature, or a maximum position, etc.  however many times it reaches this value/position

input time is per single cycle: 
if 20 cycles per second, put 0.05 for time
if 4 seconds per one cycle, put 4 for time

PI control: slow responding system, like systems for fluids or heat, typically >2 second settling time after step change
PID control: fast responding system, like motion control or positioning, typically <2 second settling time after step change

use the resulting Kp, Ki or Kp, Ki, Kd parameters in the loop for a sufficient or nearly sufficient starting point
typically further tuning won't be required, but choose to further adjust Ki or Kd before adjusting Kp

in the code, Ku is the same as Kp but note that it gets changed after calculating the tuning parameters

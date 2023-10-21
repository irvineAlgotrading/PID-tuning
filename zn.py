def ziegler_nichols_tuning(Ku, Tu):

    # PID coefficients
    Kp_pid = 0.6 * Ku
    Ki_pid = 2 * Kp_pid / Tu
    Kd_pid = Kp_pid * Tu / 8
    
    # PI coefficients
    Kp_pi = 0.45 * Ku
    Ki_pi = 1.2 * Kp_pi / Tu
    
    pid_params = (Kp_pid, Ki_pid, Kd_pid)
    pi_params = (Kp_pi, Ki_pi)
    
    return pid_params, pi_params

# Get the ultimate gain (Ku) and ultimate period (Tu) from the user
try:
    Ku = float(input("Enter the ultimate gain (Ku) where the system starts oscillating: "))
    Tu = float(input("Enter the oscillation period (Tu) when the system is under ultimate gain: "))
except ValueError:
    print("Invalid input. Please enter valid numbers for Ku and Tu.")
    exit()

# Calculate the PID and PI coefficients
pid_params, pi_params = ziegler_nichols_tuning(Ku, Tu)

print(f"The PID coefficients are:\nKp = {pid_params[0]}\nKi = {pid_params[1]}\nKd = {pid_params[2]}")
print(f"The PI coefficients are:\nKp = {pi_params[0]}\nKi = {pi_params[1]}")

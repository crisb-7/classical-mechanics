from ode import *
import numpy as np
import matplotlib.pyplot as plt

def main():
    
    # Define constants
    # TODO: implement interface
    # TODO: benchmark performance: 
    #   Native Python, vs NumPy vs NumPy + Numba
    #   Lazy (?) (generator?) vs eager (?) execution
    # TODO: numerical error analysis?
    # TODO: polar coordinates implementation?
    # TODO: create module for visualization
    
    G = -9.81
    T_MAX = 2.5
    STEP = 0.05
    N = int(T_MAX/STEP)
    print("N steps =", N)

    # Initial positions, x-y
    x_initial = 0 # m
    y_initial = 10 # m

    # Initial velocity, x-y
    v_initial = 10
    theta = np.radians(40)
    v_initial_x = v_initial*np.cos(theta)
    v_initial_y = v_initial*np.sin(theta)
    
    print("Initial Velocity X:", v_initial_x)
    print("Initial Velocity Y:", v_initial_y)
    
    integration_method = EulerMethod()  # Implement as strategy pattern 

    position_y = np.empty(N, dtype=np.float64)
    velocity_y = np.empty_like(position_y)

    position_x = np.empty_like(position_y)
    velocity_x = np.empty_like(position_y)

    vel_iterator_y = integration_method.compute_generator(f_init=v_initial_y, 
                                                          derivative_fn_init=G, 
                                                          step=STEP, N=N)
    
    vel_iterator_x = integration_method.compute_generator(f_init=v_initial_x, 
                                                          derivative_fn_init=0, 
                                                          step=STEP, N=N)

    indices = [x for x in range(N-1)]

    position_x[0] = x_initial
    position_y[0] = y_initial

    for idx, vel_y, vel_x in zip(indices, vel_iterator_y, vel_iterator_x):
        
        pos_y = integration_method.compute(f_init=position_y[idx], derivative_fn_init=vel_y, step=STEP, N=1)
        pos_x = integration_method.compute(f_init=position_x[idx], derivative_fn_init=vel_x, step=STEP, N=1)
        
        print(idx, pos_x, pos_y)
        
        position_y[idx+1] = pos_y[0]
        velocity_y[idx+1] = vel_y
        position_x[idx+1] = pos_x[0]
        velocity_x[idx+1] = vel_x

    
    plt.scatter(position_x, position_y)
    plt.show()

if __name__ == "__main__":
    main()
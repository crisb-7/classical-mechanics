from ode import *
import numpy as np

def main():
    
    # Define constants
    # TODO: implement as script
    
    G = -9.81
    T_MAX = 2.5
    STEP = 0.05
    N = int(T_MAX/STEP)
    print("N steps =", N)

    # Initial positions, x-y
    x_initial = 0 # m
    y_initial = 5 # m

    v_initial_x = 0
    v_initial_y = 0
    theta = np.radians(45)

    # TODO: create module for visualization

    integration_method = EulerMethod()  # Implement as strategy pattern 

    position = np.empty(N, dtype=np.float64)
    velocity = np.empty_like(position)

    velocity_iterator = integration_method.compute_generator(f_init=v_initial_y, derivative_fn_init=G, step=STEP, N=N)

    # TODO: implement 2D simulation; currently it's 1D
    for idx, vel in enumerate(velocity_iterator):
        pos = integration_method.compute(f_init=y_initial, derivative_fn_init=vel, step=STEP, N=1)
        position[idx] = pos[0]
        velocity[idx] = vel

    # np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.4f}'.format})
    print(velocity)
    print(position)

if __name__ == "__main__":
    main()
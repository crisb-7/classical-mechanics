import numpy as np

class EulerMethod:
    
    @staticmethod
    def compute(f_init: float, derivative_fn_init, step: float, N: int=10):
        f_vector = []
        derivative_fn = derivative_fn_init
        fn = f_init
        for _ in range(N):
            fn = fn + derivative_fn*step
            f_vector.append(fn)
        return f_vector

    @staticmethod
    def compute_generator(f_init: float, derivative_fn_init, step: float, N: int=10):
        derivative_fn = derivative_fn_init
        fn = f_init
        for _ in range(N):
            fn = fn + derivative_fn*step
            yield fn


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

    for idx, vel in enumerate(velocity_iterator):
        pos = integration_method.compute(f_init=y_initial, derivative_fn_init=vel, step=STEP, N=1)
        position[idx] = pos[0]
        velocity[idx] = vel

    # np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.4f}'.format})
    print(velocity)
    print(position)

if __name__ == "__main__":
    main()
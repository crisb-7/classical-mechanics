import math
import numpy as np
from solvers import EulerMethod, initialize_solver

# TODO: add getter and setter for initial conditions

class ProjectileMotion:

    def __init__(self, 
                 g: float = -9.806, 
                 time: float = 2.5, 
                 step: float = 0.05, 
                 method: str = "euler", 
                 x_init: float = 0.0, 
                 y_init: float = 0.0, 
                 v_init: float = 15.0, 
                 theta: float = 40.0
    ):
        self.G = g
        self.T_MAX = time
        self.STEP = step
        self.N = int(time/step)

        self.x_initial = x_init
        self.y_initial = y_init

        self.v_initial = v_init
        self.theta = np.radians(theta)
        self.v_initial_x = v_init * np.cos(self.theta)
        self.v_initial_y = v_init * np.sin(self.theta)
        # self.v_initial_x = v_init * math.cos(theta)
        # self.v_initial_y = v_init * math.sin(theta)

        self.solver = initialize_solver(method)

        self.position_y = np.empty(self.N, dtype=np.float64)
        self.velocity_y = np.empty_like(self.position_y)

        self.position_x = np.empty_like(self.position_y)
        self.velocity_x = np.empty_like(self.position_y)
    
    def run_simulation(self):

        vel_y_iter = self.solver.compute_generator(f_init=self.v_initial_y, derivative_fn_init=self.G, step=self.STEP, N=self.N)
        vel_x_iter = self.solver.compute_generator(f_init=self.v_initial_x, derivative_fn_init=0, step=self.STEP, N=self.N)

        indices = [x for x in range(self.N-1)]

        self.position_x[0] = self.x_initial
        self.position_y[0] = self.y_initial

        for idx, vel_y, vel_x in zip(indices, vel_y_iter, vel_x_iter):
            
            pos_y = self.solver.compute(f_init=self.position_y[idx], derivative_fn_init=vel_y, step=self.STEP, N=1)
            pos_x = self.solver.compute(f_init=self.position_x[idx], derivative_fn_init=vel_x, step=self.STEP, N=1)

            print(idx, vel_x, vel_y)
            
            self.position_y[idx+1] = pos_y[0]
            self.velocity_y[idx+1] = vel_y
            self.position_x[idx+1] = pos_x[0]
            self.velocity_x[idx+1] = vel_x

    def get_results(self) -> dict[str, np.ndarray[np.float64]]:
        # Return the results of the simulation
        return {
            'position_x': self.position_x,
            'velocity_x': self.velocity_x,
            'position_y': self.position_y,
            'velocity_y': self.velocity_y,
        }
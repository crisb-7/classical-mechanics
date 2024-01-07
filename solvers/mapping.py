from solvers.ode import EulerMethod

SOLVER_MAPPING = {
    "euler": EulerMethod
}

def initialize_solver(method):
    if method in SOLVER_MAPPING:
        solver_class = SOLVER_MAPPING[method]
        return solver_class()
    else:
        raise ValueError(f"Unsupported ODE solver: {method}. Supported solvers: {SOLVER_MAPPING.keys()}")
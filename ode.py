# TODO: use pre-allocated list implementation for performance

class EulerMethod:
    
    @staticmethod
    def compute(f_init: float, derivative_fn_init, step: float, N: int=10):
        f_vector = []
        derivative_fn = derivative_fn_init
        fn = f_init
        for i in range(N):
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

class RungeKutta4:
    pass

class AdamsBashford:
    pass
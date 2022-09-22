from ..numerical_method import numerical_method_f


def iterative_soc_f(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude,
                        period, input_time, url, df):
        for index in indexes:
                time = n_steps * dt
                numerical_method_f(index, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude,
                                period, input_time, url, df)
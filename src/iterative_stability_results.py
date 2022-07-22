from .numerical_method import numerical_method_f


def iterative_stability_f(indexes, layer_number, n_steps, initial_velocity,
                            amplitude, period, input_time, url, df, nodes_array, dt_array):
    for i in range(len(nodes_array)):
        for j in range(len(dt_array)):
            nodes = nodes_array[i]
            dt = dt_array[j]
            time = n_steps * dt
            numerical_method_f(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude,
                                period, input_time, url, df)

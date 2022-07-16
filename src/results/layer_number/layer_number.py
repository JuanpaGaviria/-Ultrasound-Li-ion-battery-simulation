from ..numerical_method import numerical_method_f


def layer_number_f(layers, indexes, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df):
    for layer in layers:
        layer_number = layer
        numerical_method_f(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df)

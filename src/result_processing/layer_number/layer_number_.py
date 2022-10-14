from src.implicit.numerical_method import numerical_method_implicit


# layers must be a vector with the number of layers that will be tested
def layer_number_f(layers, indexes, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df, name, save, save_path, main_path):

    """
    Iterates the numerical method with changing the number of layers
    """

    for layer in layers:
        layer_number = layer
        numerical_method_implicit(indexes, layer_number, nodes, n_steps, dt, time, initial_velocity, amplitude, period, input_time, url, df, name, save, save_path, main_path)

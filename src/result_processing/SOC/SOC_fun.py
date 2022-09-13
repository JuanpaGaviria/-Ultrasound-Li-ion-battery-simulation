from src.implicit.numerical_method import numerical_method_implicit


def iterative_soc_f(indexes, layer_number, nodes, n_steps, dt, initial_velocity, df, save, save_path, main_path):
        for index in indexes:
                name = f'nodes-{nodes}-dt{dt}-index-{index}'
                numerical_method_implicit(index, layer_number, nodes, n_steps, dt, initial_velocity, df, name, save, save_path, main_path)
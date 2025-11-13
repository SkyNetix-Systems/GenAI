# DICT PACKING AND UNPACKING

# Function demonstrating dictionary packing using **kwargs
def save_user_info(**user_data):
    """Stores and displays user information."""
    print(f'User information: {user_data}')

# Passing multiple keyword arguments, which are packed into a dictionary
save_user_info(name='Bob', age=40, location='NYC')

# FUNCTION ARGUMENT UNPACKING WITH **

def connect_to_server(ip, port, username, password):
    """Simulates connecting to a server with provided credentials."""
    print(f'Connecting to {ip}:{port} as {username}')

# Dictionary containing server connection details
server_info = {
    'ip': '192.168.0.1',
    'port': 22,
    'username': 'admin',
    'password': 'dsaf8ms2kL'
}

# Unpacking the dictionary so its keys become argument names in the function call
connect_to_server(**server_info)

# MERGING DICTIONARIES WITH **

default_settings = {'batch_size': 32, 'learning_rate': 0.001, 'epochs': 10}
experiment_settings = {'batch_size': 64, 'learning_rate': 0.0005}

# Merge dictionaries, with keys from `experiment_settings` overwriting `default_settings`
combined_settings = {**default_settings, **experiment_settings}

print(combined_settings)

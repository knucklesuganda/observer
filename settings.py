import environs


env = environs.Env()
env.read_env('.env')


INITIAL_OBSERVER = env('INITIAL_OBSERVER_HOST'), env.int('INITIAL_OBSERVER_PORT')
MY_ADDRESS = env('MY_ADDRESS_HOST'), env.int("MY_ADDRESS_PORT")

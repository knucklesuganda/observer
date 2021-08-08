import os

import environs


env = environs.Env()
env.read_env('.env')

try:
    OBSERVER_ADDRESS = env('OBSERVER_ADDRESS_HOST'), env.int('OBSERVER_ADDRESS_PORT')
    TARGET_ADDRESS = env('TARGET_ADDRESS_HOST'), env.int("TARGET_ADDRESS_PORT")
except Exception:
    OBSERVER_ADDRESS = os.environ['OBSERVER_ADDRESS_HOST'], int(os.environ['OBSERVER_ADDRESS_PORT'])
    TARGET_ADDRESS = os.environ['TARGET_ADDRESS_HOST'], int(os.environ["TARGET_ADDRESS_PORT"])


HEALTH_CHECK_PAUSE = env.int('HEALTH_CHECK_PAUSE')

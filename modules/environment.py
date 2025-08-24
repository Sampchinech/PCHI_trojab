import os 

def env_run(**args):
    
    print("[*] In environment modules...")
    
    env = os.environ(".")
    
    return str(env)

env_run()
import os

def run(**args):
    
    print("[!] Dirlister in modules...")
    files = os.listdir(".")
    
    return str(files)
run()

import subprocess

try:
    subprocess.check_call(['cat', 'file_1.py'])
except Exception as E:
    print(E)

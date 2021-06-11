import subprocess

o = subprocess.check_output(['cat', 'file_1.py'])

print("Saida:", o)

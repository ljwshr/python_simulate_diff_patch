import subprocess
print (subprocess.Popen("mkdir working1232", shell=True, stdout=subprocess.PIPE).stdout.read())
import subprocess

p = subprocess.Popen("termux-sms-list", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p.wait()
p.stdout.read()

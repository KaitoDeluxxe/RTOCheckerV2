import subprocess

def run():
 subprocess.run(['powershell', 'ping.exe -t 8.8.8.8 | Foreach{"{0} {1}" -f (Get-Date -f "[HH:mm:ss]"),$_}'],capture_output=False)

if __name__=='__main__':
    run()

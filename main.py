# Task Automation (Restarting File Explorer when it bugs or stops responding)
import subprocess, time

def restart():
    subprocess.run(
        ["taskkill", "/f", "/im", "explorer.exe"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print("Closed File Explorer")
    time.sleep(1)
    print("Re-Opening File Explorer...")
    time.sleep(1)
    subprocess.run(["start", "explorer"], shell=True)
    print("File Explorer was restarted successfully.")

restart()




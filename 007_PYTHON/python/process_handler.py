import psutil
import os

# Function to get processes using more than 10% CPU
def get_heavy_process():
    processes = []
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'username']):
            try:
                proc.cpu_percent(interval=1)  # Ensures accurate reading for the next call
                if proc.info['cpu_percent'] > 10:
                    processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    except Exception as e:
        print(f"Error retrieving processes: {e}")
    return processes

# Function to restart application processes
def restart_application_process(proc):
    try:
        proc_pid = proc.info['pid']
        proc_name = proc.info['name']
        print(f"Killing process {proc_name} (PID {proc_pid})")
        proc.terminate()
        proc.wait()  # Wait for termination
        print(f"Process {proc_name} (PID {proc_pid}) terminated successfully.")
        
        # Restart the application (replace this with the actual restart logic for your app)
        print(f"Restarting process {proc_name}...")
        os.system(f"start {proc_name}")  # You can specify full path if necessary
        print(f"Process {proc_name} restarted.")
    except Exception as e:
        print(f"Error while restarting process: {e}")

# Function to terminate processes
def terminate_process(proc):
    try:
        proc_pid = proc.info['pid']
        proc_name = proc.info['name']
        print(f"Killing process {proc_name} (PID {proc_pid})")
        proc.terminate()
        proc.wait()  # Wait for termination
        print(f"Process {proc_name} terminated.")
    except Exception as e:
        print(f"Error while terminating process {proc_name}: {e}")

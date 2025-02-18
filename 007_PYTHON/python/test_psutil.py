import psutil

def get_all_processes():
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            # Get the current CPU usage (without interval)
            cpu_usage = proc.info['cpu_percent']
            print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, CPU: {cpu_usage}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

get_all_processes()

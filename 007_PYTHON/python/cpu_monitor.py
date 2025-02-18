import psutil
import time
from process_handler import get_heavy_process, restart_application_process, terminate_process
from email_handler import send_email

def monitor_cpu():
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > 60:
                print(f"CPU usage is high: {cpu_usage}%")
                heavy_processes = get_heavy_process()

                for proc_info in heavy_processes:
                    proc_name = proc_info['name']
                    proc_pid = proc_info['pid']
                    proc = psutil.Process(proc_pid)

                    if proc_name.lower() in ['system', 'svchost.exe']:  # Add more system processes as needed
                        # Send email if it's a system process
                        send_email(f"High CPU Usage Alert: {proc_name}", f"The system process {proc_name} is using high CPU. PID: {proc_pid}")
                    else:
                        if 'user' in proc.info['username'].lower():  # Assuming application process has a user
                            # Restart the application process
                            restart_application_process(proc)
                        else:
                            # Kill the non-application process
                            terminate_process(proc)

            time.sleep(5)
    except Exception as e:
        print(f"Error in monitoring CPU: {e}")

if __name__ == "__main__":
    monitor_cpu()

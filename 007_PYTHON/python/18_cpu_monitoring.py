'''python script to monitor the cpu usage .if cpu usage>60.find the process
 which is causing it and if the process is system process then sent a mail and 
 if the process is the application process then kill it and restart the process 
 and others kill it'''

# import psutil#Monitoring CPU usage and gives process info
# #we can now observe how much cpu is used
# while True:
#     # Get the current total CPU usage
#     cpu_usage=psutil.cpu_percent(interval=1)#calculate cpu usage at every 1 sec
#     print(f"the percentage is: {cpu_usage}%")#this gives value of percent in {cpu_percent},f string


# #next we need to check if cpu usage>60
#     if cpu_usage >60:# If total CPU usage is greater than 60%
#          print(f"High CPU usage detected: {cpu_usage}%")
#    # Iterate over all processes to check their individual CPU usage
#          for proc in psutil.process_iter(['pid','name','cpu_percent']):
#               process_cpu=proc.info['cpu_percent']
import psutil

import smtplib
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send an email
def send_email(subject, body):
    try:
        sender_email = "your_email@example.com"  # Your email address
        receiver_email = "recipient_email@example.com"  # Recipient's email address
        password = "your_email_password"  # Your email account password

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        # Sending the email
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to get heavy processes
def get_heavy_process():
    processes = []
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'username']):
            try:
                if proc.info['cpu_percent'] > 10:  # Filter processes with more than 10% CPU usage
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
        os.system(f"start {proc_name}")
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

# Main function to monitor CPU and take actions
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

# Run the monitor
if __name__ == "__main__":
    monitor_cpu()


              
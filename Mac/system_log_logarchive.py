import subprocess

def get_all_activities():
    try:
        command = "syslog -F '$(Time)(end): $(Message)'"
        result = subprocess.check_output(command, shell=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def save_to_file(filename, content):
    filename = './Mac/mac_result/all_log_activities.txt'
    with open(filename, 'a') as file:
        file.write(content)

all_activities = get_all_activities()
save_to_file('all_log_activities.txt', all_activities)
print("All log activities saved to 'all_log_activities.txt'")

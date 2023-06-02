import re
import json


def extract_logs(file_path):
    logs = []
    pattern = r'^(\S+) \S+ \S+ \[.*?\] ".*?" (\d{3})'

    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                ip = match.group(1)
                ReturnCode = match.group(2)
                logs.append({'ip': ip, 'ReturnCode': ReturnCode})

    return logs


def save_logs_as_json(logs, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(logs, json_file, indent=4)


file_path = 'C:/Users/Chouba/PycharmProjects/TP1 Python Tom Bourbon/venv/logs.txt'
json_file_path = 'C:/Users/Chouba/PycharmProjects/TP1 Python Tom Bourbon/venv/log.json'

logs = extract_logs(file_path)
save_logs_as_json(logs, json_file_path)
log_file_path = "C:/Program Files/MongoDB/Server/8.0/log/mongod.log"

with open(log_file_path, "r", encoding="utf-8") as log_file:
    logs = log_file.readlines()

output_file_path = r"C:/Users/harsh/Desktop/harsha_wipro/python/Day12/mongodb_operations_log.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.writelines(logs)

print("Logs saved to 'mongodb_operations_log.txt' in the specified path")
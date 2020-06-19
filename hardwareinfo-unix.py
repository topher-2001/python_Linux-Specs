import subprocess

save_list = []

def save_print(strng):
	print(str(strng))
	save_list.append(str(strng))


def get_hardware_info(type, name):
	return subprocess.getoutput("sudo dmidecode --type " + type + " | grep '" + name + "'").replace("\t", "")


# CPU Info
cpu_name = get_hardware_info("processor", "Version:")
cpu_cores = get_hardware_info("processor", "Core Count")
cpu_threads = get_hardware_info("processor", "Thread Count")
cpu_max_speed = get_hardware_info("processor", "Max Speed")

save_print("======= CPU =======")
save_print(cpu_name)
save_print(cpu_cores)
save_print(cpu_threads)
save_print(cpu_max_speed)

# GPU Info
gpu_name = subprocess.getoutput("glxinfo | egrep -i 'device|memory' | grep 'Device'")[4:];
gpu_memory = subprocess.getoutput("glxinfo | egrep -i 'device|memory' | grep 'Video memory'")[4:];

save_print("======= GPU =======")
save_print(gpu_name)
save_print(gpu_memory)

# Memory Info
ram_count = get_hardware_info("memory", "Memory Device").split("\n")
ram_man = get_hardware_info("memory", "Manufacturer").split("\n")
ram_speed = get_hardware_info("memory", "Configured Clock Speed").split("\n")
ram_size = get_hardware_info("memory", "Size").split("\n")

for i in range(len(ram_count)):
	save_print("======= RAM BANK " + str(i) + " =======")
	save_print(ram_man[i])
	save_print(ram_speed[i])
	save_print(ram_size[i])

# Board Info
board_man = get_hardware_info("baseboard", "Manufacturer")
board_name = get_hardware_info("baseboard", "Product Name")

save_print("======= MOTHER BOARD =======")
save_print(board_man)
save_print(board_name)

print(save_list)

f = open("specs.txt", "w")
for i in range(len(save_list)):
	f.write(save_list[i]+"\n")	
f.close()
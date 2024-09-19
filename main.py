import base64
import string
import random
import os

def print_str(s):
	print("\033[92m[+]",s,"\033[0m")

# get file name from commandline argument
target_file = os.sys.argv[1]
folder_name = './' + target_file.split(".")[0]

with open(target_file, 'r') as f:
	data = f.read()

os.makedirs(folder_name, exist_ok=True)

print_str("Opening file...")
print_str("Got an original data:")
print(data)
print()
print_str("Injecting spaces...")

inject_space = ""
for i in data:
	if i == ' ':
		inject_space = inject_space + ' ' * random.randint(1, 5)
	inject_space = inject_space + i

print(inject_space)

with open(folder_name + '/inject_space.ps1', 'w') as f:
	f.write(inject_space)
print_str("Success to write file: {}/inject_space.ps1".format(folder_name))

print()

var_next = [" ", ";", ".", "`", "{", "}", "(", ")", ","]
flag = False
var_list = []

for i in inject_space:
	if i == '$':
		flag = True
		var = ""
	elif flag == True and i in var_next:
		flag = False
		var_list.append(var)
	elif flag == True:
		var = var + i

filtered_var = [word for word in var_list if word[0].isupper()]
unique_var = list(set(filtered_var))

print_str("Got variables to mass:")
print(unique_var)
print()

characters = string.ascii_letters + string.digits
mass_var = inject_space

for i in unique_var:
	mass = ''.join(random.choice(characters) for _ in range(random.randint(10, 20)))
	mass_var = mass_var.replace("$" + i, "$" + mass)

print_str("Mass variables:")
print(mass_var)
print()

print_str("Writing to file...")

with open(folder_name + '/final_mass.ps1', 'w') as f:
	f.write(mass_var)
print_str("Success to write file: {}/final_mass.ps1".format(folder_name))

print()

print_str("Encoding to base64...")
encoded_cmd = base64.b64encode(mass_var.encode('utf-16le')).decode('utf-8')
print(encoded_cmd)
print()

print_str("Writing to file...")
with open(folder_name + '/encoded.ps1', 'w') as f:
	f.write(encoded_cmd)
print_str("Success to write file: {}/encoded.ps1".format(folder_name))

print()
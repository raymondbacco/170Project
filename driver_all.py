from os import listdir, system
from os.path import isfile, join


path = './phase_1_inputs/inputs/'

files = [f for f in listdir(path) if isfile(join(path, f))]


for in_file in files:
	filename = in_file[:-3]
	out_file = filename + ".out"
	system("python driver.py " + filename)
	system("python output_validator.py ./phase_1_inputs/inputs/" + in_file + " ./outputs/" + out_file)
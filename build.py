import toml

print ('Building histo pymol client...')

built_filename = 'builds/histo.py'

config = toml.load('config.toml')

python_string = ''

for filename in config:
    with open(config[filename], 'r') as filehandle:
        python_string += filehandle.read()


with open(built_filename, 'w') as built_filehandle:
    built_filehandle.write(python_string)


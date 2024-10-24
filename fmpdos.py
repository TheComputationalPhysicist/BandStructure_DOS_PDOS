import subprocess

def run_fmpdos(input_file, output_file, atom_label, n_value, l_value, m_value):
    command = f'fmpdos << EOF\n{input_file}\n{output_file}\n{atom_label}\n{n_value}\n{l_value}\n{m_value}\nEOF'
    subprocess.run(command, shell=True)

# Specify the input file
input_file = 'BSb.PDOS'

# Define the data for each fmpdos command
# outputfilename atom n(0) l(-1) m(9)
commands = [
    ('B2s', 'B', '2', '0', '9'),
    ('B2p', 'B', '2', '1', '9'),
    ('Sb5s', 'Sb', '5', '0', '9'),
    ('Sb5p', 'Sb', '5', '1', '9'),
]

# Execute the fmpdos commands
for output_file, atom_label, n_value, l_value, m_value in commands:
    if n_value == '0':
        output_filename = f'{output_file}.dat'
        run_fmpdos(input_file, output_filename, atom_label, n_value, '', '')
    elif l_value == '-1':
        output_filename = f'{output_file}.dat'
        run_fmpdos(input_file, output_filename, atom_label, n_value, l_value, '')
    else:
        output_filename = f'{output_file}.dat'
        run_fmpdos(input_file, output_filename, atom_label, n_value, l_value, m_value)


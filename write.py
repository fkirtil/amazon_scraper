def write(variable, data_file):
     
    with open(data_file, 'w') as outfile:
        outfile.write(variable)
        
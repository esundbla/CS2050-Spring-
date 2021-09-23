# Text File Concator
# Erik Sundblad
# CS1030-001

read_files = open("1030 Project 04 03 Files.txt", 'r')
append_file = open("ErikSundblad_04_03_Output.txt", 'a+')

# read through each line in file name file
for line in read_files:
    # file names need striped and added .txt
    concat_file = open(line.strip()+".txt", 'r')
    for lines in concat_file:
        append_file.write(lines)
    # added space for clean for separation of different text files
    append_file.write(" ")

# No print called for and close files at completion of program
read_files.close()
append_file.close()



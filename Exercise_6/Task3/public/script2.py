import os


def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False

    file_in = open(path_reading, "r")
    file_out = open(path_writing, "w")
    all_lines = file_in.readlines()

    for i in range(len(all_lines)):
        if i == 0:
            file_out.write("Firstname,Lastname" + ('\n' if len(all_lines) > 1 else ''))
        elif all_lines[i] == "\n":
            file_out.write(",\n")
        elif ';' in all_lines[i]:
            if i < len(all_lines) - 1:
                file_out.write(all_lines[i][all_lines[i].find(";") + 2:-1] + "," + all_lines[i][:all_lines[i].find(";")] + "\n")
            else:
                file_out.write(all_lines[i][all_lines[i].find(";") + 2:] + "," + all_lines[i][:all_lines[i].find(";")])
        else:
            file_out.write(all_lines[i][:all_lines[i].find(" ")] + "," + all_lines[i][all_lines[i].find(" ") + 1:])

    file_out.close()
    file_in.close()
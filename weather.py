import sys

header = None

def write_info(file, main, header):
    with open(file, "r") as f:
        # Write header into all_years.csv
        temp = f.readline()
        if not header:
            header = temp
            main.write(header)

        # Write rest of data into all_years.csv
        for line in f:
            main.write(line)
        
        return header

with open("all_years.csv", "w") as main:
    for file in sys.argv[1:]:
        header = write_info(file, main, header)

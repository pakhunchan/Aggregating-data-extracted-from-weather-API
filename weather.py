import requests


# files = []
try:
    include_header = True
    with open('all_years.csv', 'w') as                      f:
        for year in range(2020, 2023):
            file = requests.get(f'https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=48549&Year={year}&Month=2&timeframe=1&submit=Download+Data')
            print(year, type(file))
            for k, row in enumerate(file.text.split("\n")):
                if k > 0 or include_header:
                    f.write(row)
                    include_header = False
                
                if k < 2:
                    print(f"{k}: {row}")
            print("-------------------------------")
except Exception as e:
    pass
    with open('error.log', 'w') as err:
        err.write(str(e))



#     # files.append(file)

# with open('all_years.csv', 'w') as f:
#     # for file in files:
#         for lines in file:
#             f.write(lines.decode("utf-8"))









        
        # print(type(lines.decode("utf-8")), lines.decode("utf-8"))
        # f.write(lines.decode("utf-8").splitlines())
        # print(lines)
        # print(lines.decode('utf-8'), "\n")
        # f.write(lines.decode('utf-8'))
    

# for year in {2020..2022}; 
# do 
#     echo -n "downloading file for year $year..."
#     wget -O Feb$year.csv "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=${stationID}&Year=${year}&Month=2&timeframe=1&submit=Download+Data" 2>> errorlogs/${timestamp}.log;
#     check_download=$?
#         if [ ${check_download} != 0 ]; then echo "failed"
#         else echo "done"
#         fi
#     files="$files Feb$year.csv"
# done;




# header = None


# def append_header(header):
#     temp = f.readline()
#     if not header:
#         header = temp
#         main.write(header)
#     return header


# def write_lines():
#     for line in f:
#         main.write(line)


# with open("all_years.csv", "w") as main:
#     for file in sys.argv[1:]:
#         with open(file, "r") as f:
#             header = append_header(header)
#             write_lines()


# # import sys


# # header = None
# # with open("all_years.csv", "w") as main:
# #     for file in sys.argv[1:]:
# #         with open(file, "r") as f:
# #             temp = f.readline()
# #             if not header:
# #                 header = temp
# #                 main.write(header)
# #             for line in f:
# #                 main.write(line)

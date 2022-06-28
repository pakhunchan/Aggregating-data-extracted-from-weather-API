export stationID=48549
export timestamp="$(date +"%m%d%Y")@$(date +"%H")h$(date +"%M")m$(date +"%S")s"


# Creating directory, and opening up a logging system
mkdir ./logs
exec > >(tee logs/${timestamp}.log) 2>&1


# Downloading files
for year in {2020..2022}; 
do 
    wget -O Feb$year.csv "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=${stationID}&Year=${year}&Month=2&timeframe=1&submit=Download+Data";
    # Printing/logging success vs error
    check_download=$?
        if [ ${check_download} != 0 ]; then 
            echo "ERROR! Failed to download file for ${year}"
        else 
            echo "SUCCESS! Downloaded file for ${year}"
        fi
    files="$files Feb$year.csv"
done;


# Running python script to combine files into all_years.csv
python weather.py $files;

# Printing/logging success vs error
check_combine=$?
if [ ${check_combine} != 0 ]; then 
    echo "ERROR! Failed to run python script"
else 
    echo "SUCCESS! Ran python script"
fi;

##############
## MAKEFILE ##
##############

# To run the Makefile you just need to open your terminal, change to the directory where Makefile is and type make 
all: clean install collect run

# Delete the folder data which contains the dataset
clean:
	rm -r data

# Install all programs needed to run the Makefile without any error 
install:
	sudo apt-get install python3 unzip
	pip install pandas numpy matplotlib

# Create the folder data + download and extract the zip file to data + delete zip file 
collect:
	mkdir data 
	wget https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots/download?datasetVersionNumber=1
	unzip archive.zip data
	rm archive.zip

# Run python scripts
run:
	python3 data_preparation.py
	python3 data_analysis.py
	python3 plot.py


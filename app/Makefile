.PHONY: getdata
getdata:
ifeq (,$(wildcard ../data/${ENV}.db))
	echo DB ../data/${ENV}.db not found. Creating it....  
ifeq (,$(wildcard ../data/data.csv))
	@echo "Downloading data. This may take a while if it is the first time, please be patient..."
	curl -o ../data/data.fetched \
		-L "https://data.cms.gov/api/views/fs4p-t5eq/rows.csv?accessType=DOWNLOAD" 
	echo "39f90a3a04764a203cdae884cab635e3e0e8bb5e26fb95607308a0bc9d29492e *../data/data.fetched" \
		| shasum -a 256 --check - \
		&& mv ../data/data.fetched ../data/data.csv			
endif
endif


.PHONY: run
run: venv check-env getdata importdata
	$(VENV)/uvicorn --port 8000 --host 127.0.0.1 app.main:app --reload

.PHONY: check-env
check-env:
ifndef ENV
	$(error ENV is undefined. Please export ENV as one of the following 'development' 'production')
endif

.PHONY: getdata
getdata:
ifeq (,$(wildcard ./data/${ENV}.db))
	echo DB ./data/${ENV}.db not found. Creating it....  
ifeq (,$(wildcard ./data/data.csv))
	@echo "Downloading data. This may take a while if it is the first time, please be patient..."
	curl -o ./data/data.fetched \
		-L "https://data.cms.gov/api/views/fs4p-t5eq/rows.csv?accessType=DOWNLOAD" \
	echo "39f90a3a04764a203cdae884cab635e3e0e8bb5e26fb95607308a0bc9d29492e *data/data.fetched" \
		| shasum -a 256 --check - \
		&& mv ./data/data.fetched ./data/data.csv	
endif
endif

.PHONY: importdata
importdata:
	$(VENV)/python ./data/importdata.py

.PHONY: downloaddb
downloaddb:
	@echo "Preparing db. This may take a while if it is the first time, please be patient..."	

include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2020.08.14/Makefile.venv"
	echo "5afbcf51a82f629cd65ff23185acde90ebe4dec889ef80bbdc12562fbd0b2611 *Makefile.fetched" \
		| shasum -a 256 --check - \
		&& mv Makefile.fetched Makefile.venv

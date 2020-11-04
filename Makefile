.PHONY: run
run: venv getdata importdata
	$(VENV)/uvicorn --port 8000 --host 127.0.0.1 app.main:app --reload

.PHONY: getdata
getdata:
ifeq (,$(wildcard ./data/data.csv))
	curl -o ./data/data.fetched \
		-L "https://data.cms.gov/api/views/fs4p-t5eq/rows.csv?accessType=DOWNLOAD" \
	echo "39f90a3a04764a203cdae884cab635e3e0e8bb5e26fb95607308a0bc9d29492e *data/data.fetched" \
		| shasum -a 256 --check - \
		&& mv ./data/data.fetched ./data/data.csv	
endif

.PHONY: importdata
importdata:
	$(VENV)/python ./data/importdata.py

include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2020.08.14/Makefile.venv"
	echo "5afbcf51a82f629cd65ff23185acde90ebe4dec889ef80bbdc12562fbd0b2611 *Makefile.fetched" \
		| shasum -a 256 --check - \
		&& mv Makefile.fetched Makefile.venv

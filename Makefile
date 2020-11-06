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
	cd app && make

.PHONY: importdata
importdata:
	$(VENV)/python ./app/importdata.py

include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2020.08.14/Makefile.venv"
	echo "5afbcf51a82f629cd65ff23185acde90ebe4dec889ef80bbdc12562fbd0b2611 *Makefile.fetched" \
		| shasum -a 256 --check - \
		&& mv Makefile.fetched Makefile.venv

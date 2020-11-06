.PHONY: getdata
getdata:
ifeq (,$(wildcard ../data/${ENV}.db))
	@echo DB ../data/${ENV}.db not found. Creating it....  
	@echo "Downloading database. This may take a while if it is the first time, please be patient..."

ifeq (${ENV},development)

	curl -o ../data/${ENV}.fetched \
		-L "https://www.dropbox.com/s/n7nc9lm6dwgh3ta/${ENV}.db?dl=0" 
	echo "79f734119b50c3787d225d1b92ef93c07e64c54fe834387a090194d95b69a431 *../data/${ENV}.fetched" \
		| shasum -a 256 --check - \
		&& mv ../data/${ENV}.fetched ../data/${ENV}.db
endif

ifeq (${ENV},production)
	curl -o ../data/${ENV}.fetched \
		-L "https://www.dropbox.com/s/htv6l0yf4ckf2su/${ENV}.db?dl=0" 
	echo "fa6bb312be680de7b4b4c0246cca02ab31126927d1ecf9aec23306ac6904d727 *../data/${ENV}.fetched" \
		| shasum -a 256 --check - \
		&& mv ../data/${ENV}.fetched ../data/${ENV}.db
endif

endif


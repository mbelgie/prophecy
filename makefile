setup:
	./setup.sh

clean:
	rm -rf data
	rm -rf extras

test:
	python3 code/srs/getStockPrices.py -t lulu -s 2021-01-01 -e 2021-10-07 -i 60m
	python3 code/srs/getStockPrices.py -t msft -s 2021-01-01 -e 2021-10-07 -i 60m
	python3 code/srs/getStockPrices.py -t amzn -s 2021-01-01 -e 2021-11-11 -i 60m
	
plot:
	python3 code/srs/graphData.py amzn
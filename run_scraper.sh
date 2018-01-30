#!/bin/sh

# wait 1 minute for server to start
sleep 60

cd webscraper
python cmc_ticker.py --s 0.0.0.0:8000 --t 100
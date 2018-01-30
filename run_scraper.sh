#!/bin/sh

# wait 5 minutes for server to start
sleep 300

cd webscraper
python cmc_ticker.py --s 0.0.0.0:8000 --t 100
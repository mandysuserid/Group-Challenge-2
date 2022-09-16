
# PROJECT 2
# UW-finctech-2022
This is  a public repo for the Group 2 project Challenge, of the UW Fintech Bootcamp in 2022.


## Technologies and Libraries
1. Visual studio code - Source code editor that supports development operations like debugging, version control or task running
2. pandas - An open source library that provides high performance data and provides data analysis tools. 
3. VADER - A sentiment analysis tool speficially attuned to sentiments expressed in social media networks. The library allows an output of results labelled as either positive, negative or neutral.
4. SQL - A Standardized programming language used to manage relational databases and perform various operations of data in them.
5. NLTK - Natural Language Processing tool that contains programs and libraries for statistical language processing.
6. snscrape - Python library that scrapes tweets through Twitter API without request limits.



## Installation Guide

Download the Visual Studio Code from the official VSC website and run the installer.

Install the following dependencies and mocdules from the libraries above

```

  import requests
  import pandas as pd
  import sql
  import time
  import snscrape.modules.twitter as sntwitter
  import nltk
  from vaderSentiment.vaderSentiment 
  from GoogleNews import GoogleNews
  from newspaper import Article
  from newspaper import Config
  from logging import exception
  from datetime import datetime

```
## Sections of the Project

The project is divided into 3 main sections
1. The scheduler - this creates a loop and fires off each of the scraper scripts
2. a) Reddit Data Scraper - pulls reddit data
b) Twitter Data Scraper - pulls twitter data
c) Google Data Scraper - pulls different stock data 
3. Results Analysis -Runs sentiment analysis on new database entries

## Overview of the analysis

* Purpose of the project

The project's goal is to focus on market sentiment analysis and a develop a machine learning model that depicts the corelation between different social media sentiments extracted from reddit and twitter, and stock market  movements of  different companies extracted from Google including;
    1.  AMC- American Movie Company
    2.  GME- Game Stop	
    3.  BTC -BTCUSD	 
    4.  ETH- Ethereum	
    5.	COIN- Coinbase	
    6.	JWN- Nordstrum	 
    7.	MSFT- Microsoft	
    8.	APPL- Apple	
    9.	SPY- S&P 500	
 The MLM could potentially be used with a trading program. Trades would be based on market trends and discussions occuring in time.



* Data Collection & Parsing 

The stock market data was scraped from Google api while the social media sentiments were fetched from the twitter API and reddit API, using the python get.request function and the sql select function.


* Sentiment Analysis

The sentiment analysis of tweets and reddit news is carried out using VADER. Each sentiment is given a sentiment score which determines if the tweet is positive, negative, neutral or compound.
![image](https://user-images.githubusercontent.com/105859007/190541091-496fd842-681f-4145-8fa1-e065f870cbf4.png)



## Contributors

Joe Verhei, 
Jonathan Kang, 
Mandy McGil,
Nathan Predko, 
Virginia Murage

## License

 The code is made without a license, however, the materials used for research are licensed.
---



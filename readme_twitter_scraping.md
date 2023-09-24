# Twitter Scraping Script

This document provides a step-by-step guide to create a Twitter scraping 
using Python. The script will utilize the Tweepy library to access Twitter's API and gather tweets based on specific search criteria.

# Technology used:
1.	Python scripting
2.	Twitter rest API
3.	config parser


# Overview:
The python script to scrape the images from twitter as per the given hashtags. The script will use twitter APIs to scrape data. The API will provide the image urls and by using python os module, the images gets downloaded to given directory in project config file.


# Working:
Step1:
The first step is to create a twitter developing account using the below url
https://developer.twitter.com/en/portal/dashboard


Step2:
Twitter developer account will provide the credentials.
Set the value of variables under [twitter] tag in project config file.
1. api_key
2. api_key_secret
3. access_token
4. access_token_secret


Step 3:
Set the value of hashtags variable under [twitter] tag in project config file. Based on the given hashtags, the images get scrapped from twitter. We can set multiple hashtags by comma separated or using OR keyword. Comma(,) separated hashtags will work as AND operator, it will fetch data if both the given hashtags will match the condition.


Step4:
Run the script with command
```bash
$ python twitter_scrapping.py
```
It will download all images to the given folder path based on the given hashtags.


# How to run twitter scraper in your machine:
1. Download the required python version "https://www.python.org/downloads/release/python-3816/"
2. Install the file.
3. Open the command prompt.
4. Check python is successfully installed by command 
```bash
$ python --version
```
5. Create the virtual environment with python 
```bash 
$ python -m venv venv"
```
6. Activate the virtual environment by this command 
```bash
$ venv\Scripts\activate
```
7. Go the directorty where project code is placed.
8. Install all the requirements by command 
```bash
$ pip install -r requirements.txt
```
9. Run the file using command 
```bash
$ python twitter_scrapping.py
```

 After running the command, it will download the image file to given directory.


 # Code understanding
 ```bash 
 $ from configparser import ConfigParser
 ```

 1. This line is used to import python config parser package. This package is used to import variables from config.ini file.


``` bash
$ from filtration_script import PixlabAPI
```
2. This line of code is used to import PixlabAPI class from filtration_script.py script.


```bash
$ import requests
```
requests is python module used to call third party rest API.


```bash
$ import base64
```
base64 is used to encode the authorization token used in fetching data from twitter rest API.


```bash
$ import os
```
os is python module used for file handling like creating a directory, downloading the image file to given path.


```bash
$ config = ConfigParser()
$ config.read('config.ini')
```
This 1ine of code is used to read the configuration set in config.ini file.


```bash
$ class TwitterScrapingScript
```

python class that holds function for data scrapping from twitter using twitter rest API.

```bash 
$ def __init__(self):
```
python constructor function used to initialize the twitter API credentials.


```bash
$  _get_bearer_token
```
python function to get bearer token from twitter rest API


```bash
$ def download_image_file(self)
```
Python TwitterScrappingScript function used to download the image file based on given hashtags using twitter rest API.


```bash
$ def main(self)
```

This function will exceute when we ran the twitter_scrapping.py script.

1. The first step of this function is to call "_get_bearer_token" function that will return bearer token for twitter authentication using python requests module.
2. Nest step is to set the query_params. It needs to include query, max_results, tweet.fields, expansions, media.fields.
3. Next step is to get the images url result using twitter rest API.
4. Now, using python os module we can write the image file to given folder path.
5. In one request it will fetch result given in max_results then it will write next_token variable in comfig.ini. So, we can get next results in new request.
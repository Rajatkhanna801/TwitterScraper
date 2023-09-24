# Image Filtration Script

This document provides a step-by-step guide to create a python based script for Image filtration based on NSFW score, cropping and renaming the image file as per given dimensions.The script will utilize Pixlab API for image filtration and PIL(pillow) python module for image cropping and renaming.

# Technology Used:
1.	Python scripting
2.	Pixlab rest API
3.  Config parser
4.  PIL (pillow)


# Overview:
The python script is used to filter (based on NSFW), crop and rename the scrapped images from twitter. The images gets segregated into appropriate and non-appropriate images based on NSFW(Not safe for work) scrore. Pixlab rest API will provide the NSFW score to input image. If the score is more than 0.5 or 50% then image saved to non-appropriate images folder otherwise the image gone to appropriate image folder.


# Working:
Step1:
The first step is to create a pixlab account using the below url
https://console.pixlab.io/login


Step2:
Pixlab developer account will provide the pixlab_key.
Set the value of below variables under [pixlab] tag in project config file.
1. pixlab_key


Step 3:
Set the value of hashtags variable under [twitter] tag in project config file. Based on the given hashtags, the images get scrapped from twitter. We can set multiple hashtags by comma separated or using OR keyword. Comma(,) separated hashtags will work as AND operator, it will fetch data if both the given hashtags will match the condition.


Step4:
The database connection is established using pymongo
A new collection will be created and data is uploaded into that collection  if the user wish to upload 


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
$ python filtration_script.py
```

 After running the command, it will segrigate the images as per NSFW score, crope the image and rename the image file.

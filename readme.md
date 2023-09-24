# Steps to configure python script to windows system.
1. Download the required python version "https://www.python.org/downloads/release/python-3816/"
2. Install the file.
3. Check python is successfully installed by command "python --version".
4. Create the virtual environment with python "python -m venv venv".
5. Activate the virtual environment by this command "venv\Scripts\activate".
6. Go the directorty where python code is placed.
7. Install all the requirements by command "pip install -r requirements.txt"
8. Run the file using command "python twitter_scrapping.py".


# File description
1. twitter_scrapping.py ==> The python which will scrape data from twitter based on given hashtags and place all image files to given folder path in config file.
2. filtration_script.py ==> This file will filter the given images using Pixlab API and place the appropriate and non-appropriate images to separate folders.
3. data_uploading_script.py ==> This file will upload the appropriate images only to given Gdrive folder.
4. config.ini ==> This file will store all the credentials realated to pixab, twitter api credentials and path where we need to store the output files.
5. requirements.txt ==> This file stores the required packages and version that needs to run python scripts.
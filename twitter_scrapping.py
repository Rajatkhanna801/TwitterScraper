from configparser import ConfigParser
from filtration_script import PixlabAPI
import requests
import base64
import os


#Read the config file
config = ConfigParser()
config.read('config.ini')


class TwitterScrapingScript:
    """
        Python script to get images based on given hashtags.
    """
    def __init__(self):
        self.consumer_key = config['twitter']['api_key']
        self.consumer_secret = config['twitter']['api_key_secret']
        self.non_filtered_images = config['media']['non_filtered_folder_path']
        self.bearer_token_url = "https://api.twitter.com/oauth2/token"
        self.twitter_search_url = "https://api.twitter.com/2/tweets/search/recent"
        self.given_hastags = config['twitter']['hashtags']
        self.next_token = config['twitter']['next_token']

    def _get_bearer_token(self):
        # Encode consumer key and secret
        base64_credentials = base64.b64encode(
            f"{self.consumer_key}:{self.consumer_secret}".encode("utf-8")
        ).decode("utf-8")
        # Request parameters
        data = {"grant_type": "client_credentials"}
        headers = {
            "Authorization": f"Basic {base64_credentials}",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        }
        response = requests.post(
            self.bearer_token_url, data=data, headers=headers
        )
        if response.status_code != 200:
            self.bearer_token = ""
        else:
            self.bearer_token = response.json()['access_token']

    def connect_to_endpoint(self, url, params):
        headers = {
            "Authorization":f"Bearer {self.bearer_token}",
            "User-Agent":"v2RecentSearchPython"
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()
    
    def download_image_file(self, image_hhtp_url):
        directory = self.non_filtered_images
        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Download the files
        filename = os.path.join(
            directory, os.path.basename(image_hhtp_url)
        )
        response = requests.get(image_hhtp_url)
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
        print("\n")

    def main(self):
        self._get_bearer_token()
        query_params = {
            'query':f"has:media ({self.given_hastags})",
            'max_results':20,
            'tweet.fields':'attachments',
            'expansions':'attachments.media_keys',
            'media.fields':'height,width,media_key,preview_image_url,type,url'
        }
        if self.next_token:
            query_params['next_token'] = self.next_token
        json_response = self.connect_to_endpoint(
            self.twitter_search_url, query_params
        )
        for url in json_response.get('includes')['media']:
            if url['type'] == 'video':
                self.download_image_file(url['preview_image_url'])
            else:
                self.download_image_file(url['url'])
        # update the next token in config file to avoid duplicate
        next_token = json_response.get('meta')['next_token']
        config.set('twitter', 'next_token', next_token)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)


if __name__ == "__main__":
    obj = TwitterScrapingScript()
    obj.main()
    
    # pixlab_obj = PixlabAPI()
    # pixlab_obj.run()



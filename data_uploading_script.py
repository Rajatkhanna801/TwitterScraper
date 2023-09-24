from pydrive.auth import GoogleAuth
from configparser import ConfigParser
from pydrive.drive import GoogleDrive
import os


#Read the config file
config = ConfigParser()
config.read('config.ini')


#Authenticate the app
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

class ImageUploader:
	def __init__(self):
		self.image_folder_path = config['media']['appropriate_folder_path']
		self.new_folder_name = config['media']['gdrive_new_folder_name']

	def create_gdrive_folder(self):
		new_folder = drive.CreateFile({
			"title":self.new_folder_name, 
			"mimeType": "application/vnd.google-apps.folder"
		})
		new_folder.Upload()
		if new_folder.uploaded:
			print(f"Created folder '{new_folder['title']}' with ID: {new_folder['id']}")
			folder_id = new_folder["id"]
		else:
			print("Failed to create the folder.")
			exit()
		return folder_id

	def upload_images_to_drive(self):
		files = os.listdir(self.image_folder_path)
		folder_id = self.create_gdrive_folder()
		# Upload each file to the newly created folder in Google Drive
		for file_name in files:
			file_path = os.path.join(self.image_folder_path, file_name)
			if os.path.isfile(file_path):
				gfile = drive.CreateFile({
					"title": file_name, "parents": [{"id": folder_id}]
				})
				gfile.SetContentFile(file_path)
				gfile.Upload()
				if gfile.uploaded:
					print(f"Uploaded {file_name} successfully.")
				else:
					print(f"Failed to upload {file_name}.")


if __name__ == "__main__":
	obj = ImageUploader()
	obj.upload_images_to_drive()
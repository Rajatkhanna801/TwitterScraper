from configparser import ConfigParser
from PIL import Image
import datetime
import requests
import random
import os


#Read the config file
config = ConfigParser()
config.read('config.ini')


class PixlabAPI:
	"""
		Filter images based on NSFW score and place the files at given path.
	"""
	def __init__(self):
		self.pixlab_key = config['pixlab']['pixlab_key']
		self.nsfw_endpoint = "https://api.pixlab.io/nsfw"
		self.input_folder_path = config['media']['non_filtered_folder_path']
		self.appropriate_images_path = config['media']['appropriate_folder_path']
		self.inappropriate_images_path = config['media']['inappropriate_folder_path']
		self.image_container_width = int(config['media']['image_container_width'])
		self.image_container_height = int(config['media']['image_container_height'])
		self.image_position = config['media']['image_position']

	def create_required_folders(self):
		"""
			Function will create the required folders.
		"""
		if not os.path.exists(self.appropriate_images_path):
			os.makedirs(self.appropriate_images_path)
		if not os.path.exists(self.inappropriate_images_path):
			os.makedirs(self.inappropriate_images_path)

	def rename_and_move_file(self, image_path, output_folder):
		"""
			This function will rename the given image file.
		"""
		self.place_image_at_position(input_image=self.image)
		file_extension = os.path.splitext(image_path)[1]
		timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
		# Create the new file name with the timestamp suffix
		new_filename = f"image_{timestamp}_{random.randint(0, 1000)}{file_extension}"
		# Save the cropped image with the new filename to the output directory
		self.image.save(os.path.join(output_folder, new_filename))
		print("Images renamed and cropped successfully!")

	def get_nsfw_score(self, image_path, filename):
		"""
			The function evaluates the NSFW score of an image and, 
			if the score surpasses 0.5, places it in the suitable folder; 
			otherwise, it is directed to the non-appropriate folder.
		"""
		req = requests.post(self.nsfw_endpoint,
			files = {'file': open(image_path, 'rb')},
			data = {'key':self.pixlab_key}
		)
		response = req.json()
		if response['status'] != 200:
			print (response['error'])
			print("\n")
		elif response['score'] < 0.5 :
			print ("No adult content were detected on this picture")
			self.rename_and_move_file(image_path, self.appropriate_images_path)
		else:
			self.rename_and_move_file(image_path, self.inappropriate_images_path)
			print (f"Inappropriate content found in given file, file_name={filename}")
			print("\n")

	def place_image_at_position(self, input_image):
		"""
			Function will place input image at appropriate position. 
		"""
		x, y = 0, 0
		image_width, image_height = input_image.size
		self.image_container_width = image_width
		self.image_container_height = image_width
		# Create a new frame with a white background
		self.image = Image.new("RGB", (
			self.image_container_width, self.image_container_height
		), "grey")
		if self.image_position == "bottom":
			y = self.image_container_height // 2
			image_new_height = self.image_container_height // 2
			image_new_width = self.image_container_width
		elif self.image_position == "top":
			image_new_height = self.image_container_height // 2
			image_new_width = self.image_container_width
		else:
			image_new_height = self.image_container_height
			image_new_width = self.image_container_width // 2
			x = (self.image_container_width - image_new_width) // 2
			y = (self.image_container_height - image_new_height) // 2
		# calculate the input_image cordinates for cropping
		left = (input_image.width - image_new_width) // 2
		upper = (input_image.height - image_new_height) // 2
		right = left + image_new_width
		lower = upper + image_new_height
		# crop the input_image as per container size
		cropped_image = input_image.crop((left, upper, right, lower))
		self.image.paste(cropped_image, (x, y))
		input_image.close()

	def run(self):
		self.create_required_folders()
		for filename in os.listdir(self.input_folder_path):
			image_path = os.path.join(self.input_folder_path, filename)
			self.image = Image.open(image_path)
			# comment the below line if you do not want to use \ 
			# image filtration based on NSFW scrore.
			self.get_nsfw_score(image_path, filename)
			# comment the below line if you do not want to use croping and rename functionality
			self.rename_and_move_file(image_path, self.appropriate_images_path)
			# os.remove(image_path)


if __name__ == "__main__":
	obj = PixlabAPI()
	obj.run()

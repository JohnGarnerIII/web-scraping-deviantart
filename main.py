import requests
import os
from bs4 import BeautifulSoup

# URL to the DeviantArt page you want to scrape
url = "https://www.deviantart.com/yourusername/favourites"

# Send a request to the URL and get the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all the images on the page
    images = soup.find_all("img")
    
    # Create a directory to store the images, if it doesn't already exist
    directory = "deviantart_images"
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    # Loop through each image and download it
    for image in images:
        # Get the image URL
        image_url = image.get("src")
        
        # Send a request to the image URL and get the response
        image_response = requests.get(image_url)
        
        # Check if the request was successful
        if image_response.status_code == 200:
            # Get the image filename
            image_filename = os.path.join(directory, os.path.basename(image_url))
            
            # Write the image data to the file
            with open(image_filename, "wb") as f:
                f.write(image_response.content)
                
print("Done!")
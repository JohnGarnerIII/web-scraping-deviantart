import requests
from bs4 import BeautifulSoup

# send a GET request to the website
response = requests.get("https://www.example.com/")

# check if the request was successful
if response.status_code == 200:
    # parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # find all the elements you want to extract data from
    elements = soup.find_all("element_tag", {"attribute_name": "attribute_value"})

    # extract the data from the elements
    for element in elements:
        data = element.text
        # process the data as needed

# handle unsuccessful requests
else:
    print("Failed to fetch the page")


#Testing new git commits with VSCode

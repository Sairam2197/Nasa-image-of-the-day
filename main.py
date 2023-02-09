import requests
import streamlit as st

url = "https://api.nasa.gov/planetary/apod?" \
      "date&" \
      "api_key=JcWcslsByBZaJXepvcECbMwDay1ucfOBCoGvNTnm"

# getting request
request = requests.get(url)
# making request as a dictionary
content = request.json()

# Getting title, image and explanation from the content dictionary
st.header(content["title"])
st.image(content["url"])
st.write(content["explanation"])

# download function
# Getting image URL from the content dictionary
get_image = requests.get(content["url"], stream=True)
# Set decode_content value to True, otherwise the downloaded image file's size will be zero
get_image.raw.decode_content = True




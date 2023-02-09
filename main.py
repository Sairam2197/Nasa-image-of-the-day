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
filename = content["title"]
st.image(content["url"])
st.download_button(label="Download Image",
                   data=content["hdurl"],
                   file_name=f"{filename}.jpg")
st.write(content["explanation"])

# download function
# Getting image URL from the content dictionary
get_image = requests.get(content["hdurl"], stream=True)
# Set decode_content value to True, otherwise the downloaded image file's size will be zero
get_image.raw.decode_content = True
if st.button:
    with open("image.jpg", "wb") as file:
        file.write(get_image.content)



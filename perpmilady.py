from inky import InkyPHAT
from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw
import requests
import time



# Set up the InkyPhat screen
inky_display = auto(ask_user=True, verbose=True)
inky_display.set_border(inky_display.BLACK)

# Load the font
font = ImageFont.truetype("/home/tazzy/milady/Nationalyze-ALP.ttf", 24)
font2 = ImageFont.truetype("/home/tazzy/milady/fonts/Macaroni.ttf", 20)
font3 = ImageFont.truetype("/home/tazzy/milady/fonts/chintzy.ttf", 20)

# Load the Milady eyes image
img_eyes = Image.open("miladyeyessmal.png")
img_perp = Image.open("nftperp.png")

# Create a new image and draw the text
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

# Paste PNG images
img.paste(img_eyes, (176, 30))
img.paste(img_perp, (10, -5))

#draw.text((10, 60), "XO I LOVE MILADY XO", inky_display.BLACK, font)
#draw.text((20, 30), "working hard everyday", inky_display.BLACK, font)
#draw.text((20, 45), "on milady", inky_display.BLACK, font)



# Call the NFTperp API to get the mark price data
url = "https://api3.nftperp.xyz/milady/markprice"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()["data"]
mprice = float(data["markPrice"])

# Call the NFTperp API to get the price data
url = "https://api3.nftperp.xyz/milady/indexprice"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()["data"]
inprice = float(data["indexPrice"])

# Call the NFTperp API to get the trader stats data
url = "https://api3.nftperp.xyz/stats/leaderboard?trader=0xeAB37B9b0B3Ff2D24e70bCf7b15ff574b410c4d5"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
data = response.json()["data"]
pnl_percent = float(data["result"][0]["pnlPercent"])



# Draw the text on the inkyPHAT screen
draw.text((10, 50), f"MARK = {mprice:.2f}e", inky_display.BLACK, font3)
draw.text((10, 75), f"INDEX = {inprice:.2f}e", inky_display.BLACK, font3)
draw.text((80, 5), f"NFTperp", inky_display.BLACK, font)
draw.text((90, 30), f"Milady", inky_display.BLACK, font2)
draw.text((10, 100), f"P'n'L = {pnl_percent:.2f}%", inky_display.BLACK, font3)

# Display the image on the InkyPhat screen
inky_display.set_image(img)
inky_display.show()

# Wait for a few seconds before updating again
time.sleep(60)
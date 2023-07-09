# main.py
from PIL import Image, ImageDraw, ImageOps, ImageFont
import os
import random
from config import CARD_WIDTH, CARD_HEIGHT, CARD_TRIM_BORDER, NAME_PREFIX, NAME_ROOT, NAME_SUFFIX, FONT_FILE, NAME_FONT_SIZE, STATS_FONT_SIZE

# Define the dimensions of the trading card
card_width = CARD_WIDTH
card_height = CARD_HEIGHT

# Define the dimensions of the card trim (with border)
card_trim_width = card_width + CARD_TRIM_BORDER
card_trim_height = card_height + CARD_TRIM_BORDER

# Create a new blank image for the card trim
card_trim = Image.new("RGB", (card_trim_width, card_trim_height), "orange")

# Load and paste the male images onto the trading card
image_directory = "img/male/"
for i in range(1, 36):
    image_path = os.path.join(image_directory, f"male_{i}.png")
    if os.path.isfile(image_path):
        male_image = Image.open(image_path)

        # Calculate the new width and height for scaling
        new_width = int(male_image.width * 1.5)
        new_height = int(male_image.height * 1.5)

        # Resize the image to the new dimensions
        male_image = male_image.resize((new_width, new_height))

        # Calculate the x-coordinate for centering the image horizontally
        x = (card_width - male_image.width) // 2

        # Calculate the y-coordinate for positioning the image at the top
        y = 100

        # Create a yellow border around the image
        bordered_image = ImageOps.expand(male_image, border=10, fill='yellow')

        # Paste the bordered image onto the trading card
        card_base = Image.new("RGB", (card_width, card_height))
        card_base.paste(bordered_image, (x, y))

        # Generate the pirate name
        pirate_name = random.choice(NAME_PREFIX) + " " + random.choice(NAME_ROOT) + " The " + random.choice(NAME_SUFFIX)

        # Draw the pirate name on the trading card
        draw = ImageDraw.Draw(card_base)

        # Set the font and size for the name
        name_font = ImageFont.truetype(FONT_FILE, NAME_FONT_SIZE)
        text_width, text_height = draw.textsize(pirate_name, font=name_font)
        text_x = (card_width - text_width) // 2

        # Calculate the y-coordinate for positioning the name at the top-center
        name_y = 10

        draw.text((text_x, name_y), pirate_name, fill="white", font=name_font)

        # Paste the trading card onto the card trim
        card_trim.paste(card_base, (10, 10))  # Offset by 10 pixels for the border

# Save the final card trim as an image file
card_trim.save("pirate_card_trim.png")

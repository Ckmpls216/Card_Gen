from PIL import Image, ImageDraw, ImageOps, ImageFont
import os
import random
from config import CARD_WIDTH, CARD_HEIGHT, CARD_TRIM_BORDER, NAME_PREFIX, NAME_ROOT, NAME_SUFFIX, NAME_ROOT_FEMALE, FONT_FILE, NAME_FONT_SIZE, STATS_FONT_SIZE, TRIM_COLORS, IMAGE_BORDER_COLORS

# Define the dimensions of the trading card
card_width = CARD_WIDTH
card_height = CARD_HEIGHT

# Define the dimensions of the card trim (with border)
card_trim_width = card_width + CARD_TRIM_BORDER
card_trim_height = card_height + CARD_TRIM_BORDER

# Generate multiple cards
num_cards = 5  # Set the desired number of cards to generate
generated_cards = 0  # Counter for generated cards

while generated_cards < num_cards:
    # Select random colors for the card trim and image border
    trim_color = random.choice(TRIM_COLORS)
    image_border_color = random.choice(IMAGE_BORDER_COLORS)

    # Create a new blank image for the card trim
    card_trim = Image.new("RGB", (card_trim_width, card_trim_height), trim_color)

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

            # Create a bordered image using the selected image border color
            bordered_image = ImageOps.expand(male_image, border=10, fill=image_border_color)

            # Paste the bordered image onto the trading card
            card_base = Image.new("RGB", (card_width, card_height))
            card_base.paste(bordered_image, (x, y))

            # Generate the pirate name
            if "female" in image_path:
                pirate_name = " " + random.choice(NAME_PREFIX) + " " + random.choice(NAME_ROOT_FEMALE) + " The " + random.choice(NAME_SUFFIX)
            else:
                pirate_name = " " + random.choice(NAME_PREFIX) + " " + random.choice(NAME_ROOT) + " The " + random.choice(NAME_SUFFIX)

            # Draw the pirate name on the trading card
            draw = ImageDraw.Draw(card_base)

            # Set the font and size for the name
            name_font = ImageFont.truetype(FONT_FILE, NAME_FONT_SIZE)
            text_width, text_height = draw.textsize(pirate_name, font=name_font)
            text_x = (card_width - text_width) // 2

            # Calculate the y-coordinate for positioning the name at the top-center
            name_y = 10

            draw.text((text_x, name_y), pirate_name, fill="white", font=name_font)

            # Save the card with a unique filename based on the pirate name
            filename = f"Card{generated_cards + 1}_{pirate_name}.png"
            save_directory = "generated_cards"
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            card_path = os.path.join(save_directory, filename)

            # Paste the trading card onto the card trim
            card_trim.paste(card_base, (10, 10))  # Offset by 10 pixels for the border

            # Save the final card trim as an image file
            card_trim.save(card_path)

            generated_cards += 1  # Increment the counter for generated cards

            if generated_cards >= num_cards:
                break

    if generated_cards >= num_cards:
        break

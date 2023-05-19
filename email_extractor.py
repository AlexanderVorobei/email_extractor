import re
import pytesseract
from PIL import Image


def extract_email_addresses(image_path, output_path):
    # Use Pillow to load the image
    image = Image.open(image_path)

    # Use Tesseract to recognize text in the image
    text = pytesseract.image_to_string(image)

    # Find all email addresses in the extracted text
    email_addresses = find_email_addresses(text)

    # Write the result to a text file
    with open(output_path, "w") as file:
        file.write("\n".join(email_addresses))


def find_email_addresses(text):
    # Use regular expression to find email addresses
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    email_addresses = re.findall(email_regex, text)
    return email_addresses

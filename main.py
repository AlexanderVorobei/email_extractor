import argparse
from .email_extractor import extract_email_addresses


if __name__ == "__main__":
    # Set up command-line arguments
    parser = argparse.ArgumentParser(
        description="Extract email addresses from an image."
    )
    parser.add_argument("--input", help="Path to the input image.")
    parser.add_argument("--output", help="Path to the output text file.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to extract email addresses
    extract_email_addresses(args.input, args.output)

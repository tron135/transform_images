import os
from PIL import Image
from pillow_heif import register_heif_opener

# Function to convert CR2 to JPG
def convert_cr2_to_jpg(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Loop through each file
    for filename in files:
        # Get the full path of the file
        filepath = os.path.join(input_folder, filename)

        # Check if the file is a directory
        if os.path.isdir(filepath):
            # If it's a directory, recursively call the function
            convert_cr2_to_jpg(filepath, os.path.join(output_folder, filename))
        else:
            # Check if the file is a CR2 image
            if filename.lower().endswith('.cr2'):
                # Open the CR2 image
                with Image.open(filepath) as img:
                    # Convert and save as JPG
                    output_filepath = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
                    img.convert('RGB').save(output_filepath, 'JPEG')


# Function to convert HEIC to JPG
# def convert_heic_to_jpg(input_folder, output_folder):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # List all files in the input folder
#     files = os.listdir(input_folder)

#     # Loop through each file
#     for filename in files:
#         # Get the full path of the file
#         filepath = os.path.join(input_folder, filename)

#         # Check if the file is a directory
#         if os.path.isdir(filepath):
#             # If it's a directory, recursively call the function
#             convert_heic_to_jpg(filepath, os.path.join(output_folder, filename))
#         else:
#             # Check if the file is a HEIC image
#             if filename.lower().endswith('.heic'):
#                 # Open the HEIC image using Pillow
#                 heic_image = Image.open(filepath)
#                 # Convert to RGB (required for saving as JPEG)
#                 heic_image_rgb = heic_image.convert('RGB')
#                 # Save as JPG
#                 output_filepath = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
#                 heic_image_rgb.save(output_filepath, 'JPEG')

# Set the path to the folder containing your files
input_folder = "F:\Converted Images"
# Set the path to the output folder where converted JPG files will be saved
output_folder = "F:\Checking"

# Call the function to convert CR2 files to JPG
# convert_cr2_to_jpg(input_folder, output_folder)

# Call the function to convert HEIC files to JPG
convert_heic_to_jpg(input_folder, output_folder)

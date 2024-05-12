import os
from PIL import Image

# Function to convert images to JPEG format
def convert_to_jpeg(input_folder, output_folder):
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
            convert_to_jpeg(filepath, os.path.join(output_folder, filename))
        else:
            # Check if the file is an image
            if filename.lower().endswith(('.png', '.bmp', '.gif', '.tiff', '.webp')):
                # Check if the image is not in the specified formats
                if not filename.lower().endswith(('.jfif', '.jpg', '.pjp', '.jpeg', '.pjpeg')):
                    # Open the image
                    img = Image.open(filepath)

                    # Convert the image to JPEG format
                    output_filepath = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')
                    img.convert('RGB').save(output_filepath, 'JPEG')
            else:
                # If it's not an image, copy the file to the output folder
                output_filepath = os.path.join(output_folder, filename)
                os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
                os.system(f'copy "{filepath}" "{output_filepath}"')

# Set the path to the folder containing your images and videos
input_folder = "F:\Exported Images"
output_folder = "F:\Converted Images"

# Call the function to convert images to JPEG format
convert_to_jpeg(input_folder, output_folder)

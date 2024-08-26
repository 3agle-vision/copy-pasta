from PIL import Image

def crop_image(image_path, x, y, w, h, output_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Define the cropping box (left, upper, right, lower)
        box = (x, y, x + w, y + h)
        
        # Crop the image using the defined box
        cropped_img = img.crop(box)
        
        # Save the cropped image
        cropped_img.save(output_path)
        
        # Optionally, display the cropped image
        cropped_img.show()

X = 114
Y = 633
W = 1038
H = 1017
# Example usage

files  = ["Screenshot (65).png", ... ]
for file in files:
    crop_image(file, x=Y, y=X, w=W-Y, h=H-X, output_path=file+"-d.png")

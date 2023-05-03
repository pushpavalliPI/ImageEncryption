from PIL import Image
import random

def encrypt_image(image_path):
    # Open the image and convert it to a list of pixel values
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Generate a random encryption key
    key = random.randint(1,255)

    # Encrypt the pixel values
    encrypted_pixels = []
    for pixel in pixels:
        encrypted_pixels.append(tuple((val ^ key) for val in pixel))

    # Save the encrypted image
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save('encrypted_image.png')

    # Return the encryption key
    return key

def decrypt_image(image_path, key):
    # Open the encrypted image and convert it to a list of pixel values
    img = Image.open(image_path)
    pixels = list(img.getdata())

    # Decrypt the pixel values
    decrypted_pixels = []
    for pixel in pixels:
        decrypted_pixels.append(tuple((val ^ key) for val in pixel))

    # Save the decrypted image
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save('decrypted_image.png')

# Encrypt an image and get the encryption key
key = encrypt_image('image.png')
print(f"The encryption key is: {key}")

# Decrypt the encrypted image using the encryption key
decrypt_image('encrypted_image.png', key)

from PIL import Image

image = Image.open("zzzzest_bw_dpi.jpg").convert("RGBA")

# Load the pizels into memory
pixels = image.load()
# For each pixel in the image
for i in range(image.size[0]):
    for j in range(image.size[1]):
        # If the pixel is white
        if pixels[i, j] == (255, 255, 255, 255):
            # Make it transparent
            pixels[i, j] = (255, 255, 255, 0)

# Save the now transparent image:
image.save("convert1.png", format="png")

# Show it on the screen
# root = tk.Tk()

# canvas = tk.Canvas(root, bg="white")
# canvas.pack()

# tk_image = ImageTk.PhotoImage(image)
# canvas.create_image(0, 0, image=tk_image, anchor="nw")

# root.mainloop()
import cv2 #opencv
import tkinter as tk #baraye tolid filedialog baraye user ke file ra entekhab konad
from tkinter import filedialog

def zoom_image(image_path, zoom_factor): #function zoom: readimage width,height -> calculate size jadid -> resize image -> return image resize shode
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
#mohasebe size jadid
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)
#resize image bar asas new width & new height va interpolation factor
    zoomed_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    return zoomed_image

def browse_image():  #function baraye entekhab image tavasot user
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Aks ra entekhab konid", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    return file_path

#gereftan image path 
image_path = browse_image()

#daryaft meghdar zoom az user be soorat float
zoom_factor = float(input("Meghdar Zoom ra moshakhas konid: (baraye mesal : 0.5 baraye zoom out va 2 baraye zoom 200% ): "))

#zooming
zoomed_image = zoom_image(image_path, zoom_factor)

#namayesh va save image tolid shode
cv2.imwrite("zoomed_image.png", zoomed_image)
print("Zoomed image created and saved as zoomed_image.png")

cv2.imshow("Zoomed Image", zoomed_image)
cv2.waitKey(-1)
cv2.destroyAllWindows()

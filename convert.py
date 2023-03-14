from pdf2image import convert_from_path
import os
path = os.path.dirname(__file__)
directory = path + '/input'

def convert(file_path, name): #convert pdf to images
  images = convert_from_path(file_path,dpi=85, fmt="tiff", grayscale=True)
  for image in images:
    newsize = (int(image.size[0] / 2) , int(image.size[1]/2))
    image.resize(newsize)

  new_image = images[0]
  images.pop(0)
  new_image.save(path + '/output/' + name + ".tif", save_all=True,append_images=images)
  print(name, '.tif saved successfully!!')

def iterate_input(): # iterate over files in input directory
    for filename in os.listdir(directory):
      f = os.path.join(directory, filename)
      if os.path.isfile(f):
        folder_name = filename.split('.')[0]
        try:
          convert(f, str(folder_name))
        except:
          print("Error occured in file", f)
iterate_input()
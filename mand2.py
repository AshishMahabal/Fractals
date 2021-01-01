import streamlit as st
from PIL import Image 

st.header('Mandelbrot Set')
'Renditions of the Mandelbrot set. '\
'x- and y-ranges for the full set are [-2,1] and [-1.5,1.5]. '\
'x increaes from left to right, and y from top to bottom.'\
'Explore denser regions with more iterations e.g. [-2:-1.9, -0.01:0.01], '\
'or [-1.950516:-1.9505158, -0.0000001:0.0000001].'

st.sidebar.header('Mandelbrot Set choices')
x1 = float(st.sidebar.text_input('min x',-2.0))
x2 = float(st.sidebar.text_input('max x',1.0))
y1 = float(st.sidebar.text_input('min y',-1.5))
y2 = float(st.sidebar.text_input('max y',1.5))
maxIt = int(st.sidebar.text_input('max iterations',100))
aspectRatio = st.sidebar.checkbox('maintain aspect ratio?')
imgsize = int(st.sidebar.text_input('image size',512))
# st.sidebar.header('To Dos')
# st.sidebar.write('Adjust x/y resolution')
# st.sidebar.write('Plus many other bits')

xwidth = x2-x1
ywidth = y2-y1
xyratio = xwidth/ywidth

if aspectRatio:
    imgxsize = imgsize if xyratio>=1 else int(imgsize*xyratio)
    imgysize = int(imgxsize/xyratio)
else:
    imgxsize = imgsize
    imgysize = imgsize

#imgxsize,imgysize,xyratio

image = Image.new("RGB", (imgxsize, imgysize)) 
  
for y in range(imgysize): 
    zy = y * (y2 - y1) / (imgysize - 1)  + y1 
    for x in range(imgxsize): 
        zx = x * (x2 - x1) / (imgxsize - 1)  + x1 
        z = zx + zy * 1j
        c = z 
        for i in range(maxIt): 
            if abs(z) > 2.0: break
            z = z * z + c 
        image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16)) 
  
st.image(image)
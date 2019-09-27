# TransparentBackground
Small script to make your background transparent. Select what is transparent by making it white.

So the reason it works is because we are converting the image file to PNG if it was not already. This is because PNG files are able to add a fourth value, the alpha value, which controls the transparency of a pixel.

I am using openCV to do the work. It is far from perfect, but it is tolerable. What I mean by "making it white" is to modify your image using Paint or Pinta or something else and select the area you want transparent by making that area white. You will have to change what you do not want to become transparent and is already white by changing its color.

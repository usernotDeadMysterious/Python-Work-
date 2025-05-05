import cv2

# Step 1: Read the input image
input_image_path = "input/img.png"
image = cv2.imread(input_image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to read the input image.")
else:
    # Step 2: Split the image into its color channels (R, G, B)
    blue, green, red = cv2.split(image)
# xk;ds[o
#       kspkfgpkspdfkg
#       'sb7sdf4
#       [gs4dg[s4dfg4s[
#           dfgs
#           [dfgsg[sdf
#                  gs4fg
#                  sdf
#                  gps
#                  df;g
#                  ;sorted;gs4d;finallysdf;globalss
#                  gsdfg
#                  sdf[sortedsdflg
#                      s;dlfg
#                      ;slfd
#                      g;sdf
#                      ;gls
#                      ;fdlg
#                      s]]
#       ]]]']
    # Step 3: Create a grayscale image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 4: Combine the color channels to form images with different colors
    # Here we swap the channels to create images with different colors
    image_blue = cv2.merge((blue, blue, blue))
    image_green = cv2.merge((green, green, green))
    image_red = cv2.merge((red, red, red))

    # Step 5: Save the processed images
    cv2.imwrite("output/output1_image_blue.jpg", image_blue)
    cv2.imwrite("output/output2_image_green.jpg", image_green)
    cv2.imwrite("output/output3_image_red.jpg", image_red)
    cv2.imwrite("output/output4_image_gray.jpg", gray)

    print("Color manipulation complete. Output images saved successfully.")

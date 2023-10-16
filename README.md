# urine-strip-RGB-eval
Assignment done with Django using OpenCV to upload image of a urine strip and get the rgb values of each square evaluation strip

## Setup
1. Clone the repo
2. py manage.py migrate
3. Both Numpy and Opencv are required to be installed
4. py manage.py runserver (app is still in Dev)
5. GOTO: {localhost-url}/computervision
6. Upload a urine strip image and the page will display the RGB values of each colour strip

## How the app works
1. Takes the urine strip image generally it is kept in a black boundary
2. Convert the image to LAB colours
3. Take the L-Channel and find its threshold then binary threshold of that thresh_L
4. We find the max contour of this threshold
5. Then find it boundary and crop the image around this boundary
6. By simple estimation we find the central pixel colours of each strip (First strip starts from 65 pixel and each strips center is approx. 90 pixels apart)

## Alternate approach
A more accurate approach would be detecting the colour patches with more accurate thresholding
We can have a 1D colour strip image with converting the image to double and then finding the horizontal mean of BGR values of each pixel in the row and setting all pixels in the row to that mean
Then we can calculate the mean of BGR of neighbouring pixels from the center of each patch
Presence of other colours round the patches (row wise) would may cause some deviation from accurate BGR values

### References
1. https://stackoverflow.com/questions/54523761/how-can-i-segment-urine-strip-colors
2. https://github.com/akvo/akvo-caddisfly/issues/10
3. https://opencvpython.blogspot.com/2013/05/thresholding.html
4. Official Django Getting Started
5. Bing ChatGPT-4
6. Google Bard

### First Django App (todo.)

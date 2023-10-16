from django.shortcuts import get_object_or_404, render, redirect
import cv2 as cv
import numpy as np
import json
from .models import UrineStrip


def index(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        img = cv.imdecode(np.fromstring(image.read(), np.uint8), cv.IMREAD_UNCHANGED)
        lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
        L, a, b = cv.split(lab)
        ret, thresh_L = cv.threshold(L, 127, 255, cv.THRESH_BINARY)
        binaryImg = cv.threshold(thresh_L, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
        contours, hierarchies = cv.findContours(binaryImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        maxContour = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(maxContour)
        crop_img = img[y : y + h, x : x + w]
        rs = []
        x = crop_img.shape[1] // 2
        y = 65
        for i in range(10):
            b = int(crop_img[y, x, 0])
            g = int(crop_img[y, x, 1])
            r = int(crop_img[y, x, 2])
            y = y + 85
            rs.append([r, g, b])
        params = ["URO","BIL","KET","BLD","PRO","NIT","LEU","GLU","SG","PH"]
        result = {}
        for i in range(10):
            result[params[i]] = rs[i]
        return render(request, 'computervision/index.html', { "result": result })
    else:
        return render(request, 'computervision/index.html', { "result": {} })

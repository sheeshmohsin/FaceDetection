import os
import cv2
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from app.forms import FileUploadForm
from PIL import Image

# Create your views here.
def home(request):
	if request.method == "POST":
		form = FileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			f = form.save()
			# Create the haar cascade
			faceCascade = cv2.CascadeClassifier(settings.CASC_PATH)
			# Read the image
			img_path = os.path.join(settings.BASE_DIR, 'media', str(f.file))
			print img_path
			image = cv2.imread(img_path)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			# Detect faces in the image
			faces = faceCascade.detectMultiScale(
			    gray,
			    scaleFactor=1.1,
			    minNeighbors=5,
			    minSize=(30, 30),
			    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
			)
			print("Found {0} faces!".format(len(faces)))

			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
			    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

			image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			ret_img = Image.fromarray(image_rgb)
			response = HttpResponse(content_type="image/jpeg")
			ret_img.save(response, "JPEG")
			return response

	return render(request, 'home.html', {'form':FileUploadForm()})
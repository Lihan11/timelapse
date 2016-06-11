from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import picamera
import datetime

# snap a photo using picamera
camera = picamera.PiCamera()
img_name = 'images/' + str(datetime.datetime.now()) + '.jpg'
camera.capture(img_name)

# auth to gdrive
gauth = GoogleAuth()
gauth.LoadCredentialsFile("secret.txt")

if gauth.credentials is None:
    gauth.CommandLineAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("secret.txt")

# upload the photo to gdrive
drive = GoogleDrive(gauth)
f = drive.CreateFile()
f.SetContentFile(img_name)
f.Upload()

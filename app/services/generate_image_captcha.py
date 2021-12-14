import os
import pyimgur
import string, random
from uuid import uuid4
from captcha.image import ImageCaptcha
from dotenv import load_dotenv

load_dotenv()

IMGUR_CLIENT_ID = os.environ.get('IMGUR_CLIENT_ID')


def generate_image_captcha(num_chars):
    all_chars = string.ascii_letters + string.digits

    text_captcha = ''.join(random.choice(all_chars) for _ in range(num_chars))

    image_captcha = ImageCaptcha(width=40*num_chars, height=12*num_chars)

    image_captcha.generate(text_captcha)

    path = f"/tmp/{uuid4()}.png"

    image_captcha.write(text_captcha, path)

    im_client = pyimgur.Imgur(IMGUR_CLIENT_ID)

    uploaded_image = im_client.upload_image(path, title=f"{uuid4()}")

    return text_captcha, uploaded_image.link

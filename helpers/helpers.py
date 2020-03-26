from PIL import Image
from faker import Faker


faker = Faker()


def list_times_scrool(device_name):
    lista_times = {"Galaxy_Nexus_API_29": [4, 4]}
    return lista_times[device_name.lower()]


def compare_two_image(first_image, second_image):
    i1 = Image.open(first_image)
    i2 = Image.open(second_image)

    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    return ncomponents
    
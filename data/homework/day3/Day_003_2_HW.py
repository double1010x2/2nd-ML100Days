target_url="https://raw.githubusercontent.com/vashineyu/slides_and_others/master/tutorial/examples/imagenet_urls_examples.txt"

import requests
response = requests.get(target_url)
data = response.text


# 找到換行符號，用該符號做字串分割後，把它拿掉
split_tag = "\t"

data = data.split(split_tag)
del data[0]

def img2arr_fromURLs(url_list, resize = False):
    """
    請完成這個 Function
    Args
        - url_list: list of URLs
        - resize: bool
    Return
        - list of array
    """
    img_list = []
    for url in url_list:
        resp = requests.get(url)
        try:
            img  = Image.open(BytesIO(resp.content))
            img_list.append(np.array(img))
        except:
            continue
    return img_list



import pandas as pd


df = pd.DataFrame(data)

from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

#response = requests.get(first_link)
#img = Image.open(BytesIO(response.content))

# Convert img to numpy array

#plt.imshow(img)
#plt.show()
result = img2arr_fromURLs(df.loc[0:5].values.flatten().tolist())
print("Total images that we got: %i " % len(result)) # 如果不等於 5, 代表有些連結失效囉

for im_get in result:
    plt.imshow(im_get)
    plt.show()

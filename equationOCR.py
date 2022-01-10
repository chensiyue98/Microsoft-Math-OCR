import base64
import requests
import time
import pyperclip
import json
import os

def get_image():
    img_path = "./screenshot_temp.png"

    with open(img_path, "rb") as img_file:
         image_data = base64.b64encode(img_file.read())
    return image_data

def get_latex(image_data):
    t = time.time()
    t = int(round(t*1000))

    url = "https://www.bing.com/cameraexp/api/v1/getlatex"
    data = {"data": image_data.decode('utf-8'), "inputForm": "Image", "clientInfo": {"app": "Math", "platform": "ios",
                                                                                        "configuration": "Unknown", "version": "1.8.0", "mkt": "zh-cn"}, "timestamp":t}
    r = requests.post(url, json=data)
    result = json.loads(r.text)
    if result['latex'] != '':
        dollar_result = "$" + result['latex'] + "$"
        os.system( 'osascript -e \'display notification "已复制到剪贴板" with title "equationOCR" subtitle "识别成功"\'' )
        return pyperclip.copy(dollar_result)
    else:
        print("Not get")
        os.system( 'osascript -e \'display notification "未找到公式" with title "equationOCR" subtitle "识别失败"\'' )
        return 1

if __name__=="__main__":
    image_data = get_image()
    get_latex(image_data)
    
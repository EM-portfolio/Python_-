from flask import Flask, request
from flask import render_template
from pathlib import Path
from bs4 import BeautifulSoup as BS
from PIL import Image
import requests
import os
import urllib
import time
###rout/toppage
app = Flask(__name__)
@app.route("/", methods=["GET"])
def base():
    return render_template("base.html")


###route/formpage
@app.route("/form", methods=["POST"])
def input():
    counter = 1
    URL = request.form["URL"]
    html = requests.get(URL)
    soup = BS(html.content, "html.parser")
    # 自宅用パス
    directory = Path("C:\Python_workspace\FlaskAPP\web_scraping_tool_app\static\Simages")
    os.makedirs(directory, exist_ok=True)
    for element in soup.find_all("img"):        
        src = element.get("src")
        if src is None:
            continue      
        image_url = urllib.parse.urljoin(URL, src)
        imgdata = requests.get(image_url)
        file_name = image_url.split("/")[-1]
        if not file_name.endswith((".jpg", ".jpeg", ".png", ".gif")):
            txt = file_name.find("?")
            file_name = (file_name[:txt])
        file_name = (str(counter) + "_" + file_name)
        out_path = directory.joinpath(file_name)
        with open(out_path, mode="wb") as f:
            a = f.write(imgdata.content)
            counter += 1
            time.sleep(0.5)
        # 自宅用パス
        data = os.listdir("C:\Python_workspace\FlaskAPP\web_scraping_tool_app\static\Simages")

    return render_template("output.html", out_path=out_path, data=data, filetitle = "抽出完了しました")

########################## CSS_test_page
@app.route("/output", methods=["GET"])
def ctp():
    # 自宅用パス
    data = os.listdir("C:\Python_workspace\FlaskAPP\web_scraping_tool_app\static\Simages")
    return render_template("output.html",data=data)
    
    

###locakhost起動
if __name__ == "__main__":
    app.run(port=8080, debug=True, host='localhost')


# # 下記更新コード
# @app.context_processor
# def override_url_for():
#     return dict(url_for="http://127.0.0.1:5000/")

# def dated_url_for(endpoint, **values):
#     if endpoint == 'static':
#         filename = values.get('filename', None)
#         if filename:
#             file_path = os.path.join(app.root_path,
#                                      endpoint, filename)
#             values['q'] = int(os.stat(file_path).st_mtime)
#     return url_for(endpoint, **values)

# 同じネットワーク環境で実行させたい時のみ実行するコード
# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)
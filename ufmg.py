import requests
from time import strftime
from pushbullet import Pushbullet
from flask import Flask
from flask import request, jsonify


# import os
app = Flask(__name__)


@app.route('/')
def homepage():

    the_time = strftime("%A, %d %b %Y %H:%M")

    checkWebPage()

    return """
    <h1>Oi, aqui é o sadogo</h1>
    <p>Hoje é: {time}.</p>
    <style>
        body{{
            text-align: center;
            background-color: pink;
    }}</style>
    <img src="http://loremflickr.com/600/400/dog" />
    """.format(time=the_time)


def checkWebPage():

    headers = {
        'headers': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    url = "https://www.ufmg.br/copeve/Arquivos/2018/trob_edital_ufmg2019.pdf"
    pb = Pushbullet("o.XlhLt0s4KzfMsQg0oDwFF98IkAAzD3tG")
    r = requests.get(url, headers=headers, timeout=5)

    time = strftime('%X')

    print("\nuser's IP: ", request.remote_addr)

    print(time, r.status_code)
    if r.status_code == 200:
        print("Saiu o edital!")
        # os.system('ntfy -t "SITE UP!!" send "%s"' % url)
        pb.push_note("UFMG", "Saiu EDITAL")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

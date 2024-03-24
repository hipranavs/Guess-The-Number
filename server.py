from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def homepage():
    global num_to_guess
    num_to_guess = random.randrange(1, 10)
    return "<h1>Guess a number between 1 and 9</h1>" \
           "<h3>Once you have, type that number after a forward slash into the url box!</h3>" \
           "<img src='https://media0.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid=ecf05e47u08m84g63oaip6b7b2ef2ql8glk6ejm17jn2o2uu&rid=giphy.gif&ct=g'>"


@app.route("/<int:num>")
def num_0(num):
    if num_to_guess > num:
        return "<h1 style='color: #afc3e2;'>Too Low!</h1>" \
               "<h3>Try again</h3>" \
               "<img src='https://imgs.search.brave.com/SgwgsR3rKMIo_gumpZj31aAwF5tcTw6kxUZqqP7yfEI/rs:fit:480:206:1/g:ce/aHR0cHM6Ly9tZWRp/YS5naXBoeS5jb20v/bWVkaWEvM29odVBl/bDQzNnFjaVFaOGZD/L2dpcGh5LmdpZg.gif'>"
    elif num_to_guess < num:
        return "<h1 style='color: #24415e;'>Too High!</h1>" \
               "<h3>Try again</h3>" \
               "<img src='https://imgs.search.brave.com/VaujTgcYku3PblGr2cnFZS3VNs1f5ERK3AxTVjga6h0/rs:fit:500:296:1/g:ce/aHR0cHM6Ly8xLmJw/LmJsb2dzcG90LmNv/bS8tNER2ZlExWUdX/MG8vWHd4dDVNNTRm/WkkvQUFBQUFBQUFF/TTgvMEZDRE0xb1Ja/MW9yM3NQVU05dzlt/Y3hwdEI3YVV4YkR3/Q0xjQkdBc1lIUS9z/NTAwLzBkMTM2Y2Mx/MjE3MDAyYTYxZjE2/MDc5NTVlYTVmMjVm/LmdpZg.gif'>"
    else:
        return "<h1 style='color: #db701c;'>You got it right!</h1>" \
               "<h3>Go to the homepage to play again.</h3>" \
               "<img src='https://media1.giphy.com/media/zCq3TyuABrRrG/giphy.gif?cid=ecf05e47at5jt78gmra8kz3yixbhxnsdrfzeztw4ly1zis7y&rid=giphy.gif&ct=g'>"


if __name__ == "__main__":
    app.run(debug=True)

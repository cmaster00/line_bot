from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('dCAMe7vy6gNvWLmTC4n7xLg57siH4lgDJGsJmWi0ZFlJqscBgu4KlQ7rnIgrTI0SE4zv0t6sPb3bvPM4V1R9cGOa34GNeK5yYfknPc7KBc6K1/j50aK6sb70vEObQaW3GrS85OmZhps2AHA4PdpDHQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3c47f560a37827f9a1a9063e35a3511a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飯了嗎'))


if __name__ == "__main__":
    app.run()
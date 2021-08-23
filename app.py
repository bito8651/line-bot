from flask import Flask, request, abort # use flask to 架設伺服器

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

line_bot_api = LineBotApi('/tLO5/zLRxPrYlaXtAbcVgJbhj9gwU05Pu37bKdGxyt9KJoeYo2XD98l5BQt0d6XPFI78NFogUT4aeC91trQJE/oirz+p1+0RTovi6jXCXosHRtv3nlukB+WzXp0bJyzMB0pUOjEoOXWjXkuFWA7OAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dec2c3b8a5d3bf558ba2ecd067f76f09')


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
    r = '中威力彩了嗎？希望早點實現財富自由'

    if msg in ['hi', 'Hi','HI']:
        r = 'Hello'
    elif msg == '你吃飯了嗎？':
        r = '還沒，社畜狗的悲哀QQ'
    elif msg == '你是誰？':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '你想訂位是嗎？'
    else:
        r = '抱歉，我聽不懂你說什麼耶'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()

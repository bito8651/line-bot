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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()

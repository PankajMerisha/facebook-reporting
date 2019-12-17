from flask import Flask
from flask import render_template
from flask import request
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

# creates a Flask application, named app
app = Flask(__name__)


# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/loginHandler")
def loginHandler():
    token = request.args.get("token")
    reporting(token)
    return render_template('success.html')


def reporting(token):
    my_app_id = '2287812568135362'
    my_app_secret = 'ff5750815f2914701fa3891d81ced76f'
    my_access_token = token
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    my_account = AdAccount('act_422404811889647')
    campaigns = my_account.get_campaigns()
    print(campaigns)


# run the application
if __name__ == "__main__":
    app.run(debug=True)

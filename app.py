import secrets
import sys
import json
from pathlib import Path

from flask import Flask, render_template, redirect, request, jsonify, session, abort, url_for
from dotenv import load_dotenv, find_dotenv
from authlib.integrations.flask_client import OAuth

from auth.auth import requires_auth
from six.moves.urllib.parse import urlencode

root_path = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent
app = Flask(__name__, template_folder=str(root_path / 'templates'), static_folder=str(root_path / 'static'))

# Quick test configuration. Please use proper Flask configuration options
# in production settings, and use a separate file or environment variables
# to manage the secret key!
app.secret_key = secrets.token_hex()

oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id='HOfuWaJTNWvNSMzBwC8vdGN5vq1qOBR7',
    client_secret='OE0gZrBOCjV03rLymPl3tcBCEA5k_OdHEXaSKZDswZMDcF0h_G77YGTlQLEmd7ZX',
    api_base_url='https://dev-5t-ortjm.us.auth0.com',
    access_token_url='https://dev-5t-ortjm.us.auth0.com/oauth/token',
    authorize_url='https://dev-5t-ortjm.us.auth0.com/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
)

app.config.from_object(__name__)


def create_app():

    @app.before_request
    def make_session_permanent():
        session.permanent = True

    @app.route("/test.html")
    def test():
        return render_template('test.html')

    @app.route('/')
    @app.route("/home")
    @app.route("/index")
    @app.route("/Home.html")
    @app.route("/home.html")
    def index():
        if 'profile' in session:
            return render_template('pages/Home.html', userinfo=session['profile'], indent=4)
        return render_template('pages/Home.html')

    @app.route('/Login.html')
    def login():
        return auth0.authorize_redirect(redirect_uri=request.host_url + 'callback')
        # return redirect('https://dev-5t-ortjm.us.auth0.com/authorize?audience=ShoshinWorks&response_type=token&client_id=HOfuWaJTNWvNSMzBwC8vdGN5vq1qOBR7&redirect_uri=' + request.host_url + 'callback')

    @app.route('/logout')
    def logout(login_error=False):
        # Clear session stored data
        session.clear()
        url_path_route_func = 'index'
        if login_error is True:
            url_path_route_func = 'login'
        # Redirect user to logout endpoint
        params = {'returnTo': url_for(url_path_route_func, _external=True), 'client_id': 'HOfuWaJTNWvNSMzBwC8vdGN5vq1qOBR7'}
        return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

    @app.route('/dashboard')
    def dashboard():
        if is_auth is False:
            abort(401)
        if 'profile' in session:
            return render_template('pages/1st_Navigation_Elements.html', userinfo=session['profile'], indent=4)  # userinfo_pretty=json.dumps(session['jwt_payload'])
        return render_template('pages/1st_Navigation_Elements.html')

    # pages required authentication by Auth0.
    @app.route('/Custom_Dashboard_Domo_url.html')
    @app.route('/Custom_Research_embed_beautiful_ai.html')
    @app.route('/Existing_Open_Innovation_list_and_embed_of_website_HeroX.html')
    @app.route('/Research_Corpus_S3_embed.html')
    @app.route('/Review_Open_Engagements_List_Embed_Asana.html')
    @app.route('/Topic_Home_Page_embed_Squirro.html')
    def pages_require_auth():
        if is_auth() is True:
            if 'profile' in session:
                return render_template('pages' + request.path, userinfo=session['profile'], indent=4)
        abort(401)

    @app.route('/1st_Navigation_Elements.html')
    def st_navigation_elements():
        if 'profile' in session:
            return render_template('pages/1st_Navigation_Elements.html',
                                   userinfo=session['profile'], indent=4)
        return render_template('pages/1st_Navigation_Elements.html')

    @app.route('/Add_Ecosystem_Topic_embed_TypeForm.html')
    def add_ecosystem_topic_embed_typeform():
        if 'profile' in session:
            return render_template('pages/Add_Ecosystem_Topic_embed_TypeForm.html', userinfo=session['profile'], indent=4)
        return render_template('pages/Add_Ecosystem_Topic_embed_TypeForm.html')

    @app.route('/Add_new_engagement_embed_Typeform.html')
    def add_new_engagement_embed_typeform():
        if 'profile' in session:
            return render_template('pages/Add_new_engagement_embed_Typeform.html', userinfo=session['profile'],
                                   indent=4)
        return render_template('pages/Add_new_engagement_embed_Typeform.html')

    @app.route('/Add_Open_Innovation_Ecosystem_embed_TypeForm.html')
    def add_open_innovation_ecosystem_embed_typeform():
        if 'profile' in session:
            return render_template('pages/Add_Open_Innovation_Ecosystem_embed_TypeForm.html',
                                   userinfo=session['profile'], indent=4)
        return render_template('pages/Add_Open_Innovation_Ecosystem_embed_TypeForm.html')

    @app.route('/Ecosystem_Intelligence_Splash_Screen.html')
    def ecosystem_intelligence_splash_screen():
        if 'profile' in session:
            return render_template('pages/Ecosystem_Intelligence_Splash_Screen.html', userinfo=session['profile'],
                                   indent=4)
        return render_template('pages/Ecosystem_Intelligence_Splash_Screen.html')

    @app.route('/Ecosystem_Learning_embed_of_Learn_Worlds_no_AuthO.html')
    def ecosystem_learning_embed_of_learn_worlds_no_autho():
        if 'profile' in session:
            return render_template('pages/Ecosystem_Learning_embed_of_Learn_Worlds_no_AuthO.html',
                                   userinfo=session['profile'], indent=4)
        return render_template('pages/Ecosystem_Learning_embed_of_Learn_Worlds_no_AuthO.html')

    @app.route('/Open_Innovation_Splash_Screen.html')
    def open_innovation_splash_screen():
        if 'profile' in session:
            return render_template('pages/Open_Innovation_Splash_Screen.html', userinfo=session['profile'], indent=4)
        return render_template('pages/Open_Innovation_Splash_Screen.html')

    @app.route('/Open_Talent_Splash.html')
    def open_talent_splash():
        if 'profile' in session:
            return render_template('pages/Open_Talent_Splash.html', userinfo=session['profile'], indent=4)
        return render_template('pages/Open_Talent_Splash.html')

    # Here we're using the /callback route.
    @app.route('/callback')
    def callback_handling():
        # Handles response from token endpoint
        if 'jwt' not in session:
            jwt_resp = auth0.authorize_access_token()
            session['jwt'] = jwt_resp.get('id_token')
            userinfo_resp = auth0.get('userinfo')
            userinfo = userinfo_resp.json()

            # Store the user information in flask session.
            # session['jwt_payload'] = userinfo
            session['profile'] = {
                'user_id': userinfo['sub'],
                'name': userinfo['name'],
                'picture': userinfo['picture']
            }
        if is_auth() is True:
            return redirect('/dashboard')
        abort(401)

    @requires_auth('get:embed-websites')
    def is_auth(payload):
        return True

    # Errors Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return logout(True)
        # return jsonify({
        #     "success": False,
        #     "error": 422,
        #     "message": "unprocessable"
        # }), 422

    @app.errorhandler(404)
    def not_found(error):
        return logout(True)
        # return jsonify({
        #     "success": False,
        #     "error": 404,
        #     "message": "resource not found"
        # }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return logout(True)
        # return jsonify({
        #     "success": False,
        #     "error": 400,
        #     "message": "bad request"
        # }), 400

    @app.errorhandler(401)
    def auth_error(error):
        return logout(True)
        # return jsonify({
        #     "success": False,
        #     "error": 401,
        #     "message": "Unauthorized"
        # }), 401

    @app.errorhandler(403)
    def auth_error(error):
        return logout(True)
        # return jsonify({
        #     "success": False,
        #     "error": 403,
        #     "message": "Unauthorized"
        # }), 403

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0')
    # app.run(host='0.0.0.0', ssl_context='adhoc') for SSL in localhost only,
    # If not working try `flask run --cert=adhoc` or add `--cert=adhoc` in the Interpreter Config. -> Additional options

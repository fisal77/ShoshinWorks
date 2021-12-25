import sys
from pathlib import Path
from flask import Flask, render_template

root_path = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent
app = Flask(__name__, template_folder=str(root_path / 'templates'), static_folder=str(root_path / 'static'))


def create_app():

    @app.route("/test.html")
    def test():
        return render_template('test.html')

    @app.route('/')
    @app.route("/home")
    @app.route("/index")
    @app.route("/Home.html")
    @app.route("/home.html")
    def index():
        return render_template('pages/Home.html')

    @app.route('/Login.html')
    def login():
        return render_template('pages/Login.html')

    @app.route('/1st_Navigation_Elements.html')
    def st_navigation_elements():
        return render_template('pages/1st_Navigation_Elements.html')

    @app.route('/Add_Ecosystem_Topic_embed_TypeForm.html')
    def add_ecosystem_topic_embed_typeform():
        return render_template('pages/Add_Ecosystem_Topic_embed_TypeForm.html')

    @app.route('/Add_new_engagement_embed_Typeform.html')
    def add_new_engagement_embed_typeform():
        return render_template('pages/Add_new_engagement_embed_Typeform.html')

    @app.route('/Add_Open_Innovation_Ecosystem_embed_TypeForm.html')
    def add_open_innovation_ecosystem_embed_typeform():
        return render_template('pages/Add_Open_Innovation_Ecosystem_embed_TypeForm.html')

    @app.route('/Custom_Dashboard_Domo_url.html')
    def custom_dashboard_domo_url():
        return render_template('pages/Custom_Dashboard_Domo_url.html')

    @app.route('/Custom_Research_embed_beautiful_ai.html')
    def custom_research_embed_beautiful_ai():
        return render_template('pages/Custom_Research_embed_beautiful_ai.html')

    @app.route('/Ecosystem_Intelligence_Splash_Screen.html')
    def ecosystem_intelligence_splash_screen():
        return render_template('pages/Ecosystem_Intelligence_Splash_Screen.html')

    @app.route('/Ecosystem_Learning_embed_of_Learn_Worlds_no_AuthO.html')
    def ecosystem_learning_embed_of_learn_worlds_no_autho():
        return render_template('pages/Ecosystem_Learning_embed_of_Learn_Worlds_no_AuthO.html')

    @app.route('/Existing_Open_Innovation_list_and_embed_of_website_HeroX.html')
    def existing_open_innovation_list_and_embed_of_website_herox():
        return render_template('pages/Existing_Open_Innovation_list_and_embed_of_website_HeroX.html')

    @app.route('/Open_Innovation_Splash_Screen.html')
    def open_innovation_splash_screen():
        return render_template('pages/Open_Innovation_Splash_Screen.html')

    @app.route('/Open_Talent_Splash.html')
    def open_talent_splash():
        return render_template('pages/Open_Talent_Splash.html')

    @app.route('/Research_Corpus_S3_embed.html')
    def research_corpus_s3_embed():
        return render_template('pages/Research_Corpus_S3_embed.html')

    @app.route('/Review_Open_Engagements_List_Embed_Asana.html')
    def review_open_engagements_list_embed_asana():
        return render_template('pages/Review_Open_Engagements_List_Embed_Asana.html')

    @app.route('/Topic_Home_Page_embed_Squirro.html')
    def topic_home_page_embed_squirro():
        return render_template('pages/Topic_Home_Page_embed_Squirro.html')

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0')
    # app.run(host='0.0.0.0', ssl_context='adhoc') for SSL in localhost only,
    # If not working try `flask run --cert=adhoc` or add `--cert=adhoc` in the Interpreter Config. -> Additional options

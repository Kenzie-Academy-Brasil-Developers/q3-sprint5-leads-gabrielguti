from flask import Flask
from app.routes.leads_blueprint import bp_leads


def inita_app(app:Flask):
    app.register_blueprint(bp_leads)
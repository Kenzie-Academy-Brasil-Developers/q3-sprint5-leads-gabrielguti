from datetime import datetime
import re
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request, current_app
from app.models.exceptions import InvalidPhone, InvalidValue, NothingHere
from app.models.leads_model import Leads
from sqlalchemy import desc

def post_leads():
    data = request.get_json()
    
    try:
        verify_errors(data)

        new_data = {
            "name": data["name"].title(),
            "email": data["email"],
            "phone": data["phone"]
        }

        lead = Leads(**new_data)

        current_app.db.session.add(lead)
        current_app.db.session.commit()

        return jsonify(lead), 201

    except InvalidPhone as err:
        return err.message, err.code
    except InvalidValue as err:
        return err.message, err.code
    except IntegrityError:
        return {"error": "Phone or email already exists"}, 409
    except KeyError:
        return {
            "error": "invalid keys",
            "valid_keys": [
                "name",
                "email",
                "phone"
            ], 
            "recieved": list(data.keys())
        }, 400




def get_leads():
    try:
        leads = Leads.query.order_by(desc(Leads.visits)).all() 
        return jsonify(leads), 200
    except NothingHere as err:
        return err.message, err.code




def update_lead():
    data = request.get_json()
    for key in data.keys():
        if key != "email":
            return {"error": "Only email is allowed"}, 400
    
    if type(data["email"]) != str:
        return {"error": "Email must be a string type"}, 400

    lead_updated = Leads.query.filter(Leads.email == data["email"]).first()

    if not lead_updated:
        return {"error": "Email not found"}, 404
    
    lead_updated.visits = lead_updated.visits + 1
    lead_updated.last_visit = str(datetime.now())

    current_app.db.session.add(lead_updated)
    current_app.db.session.commit()
    return "", 200


def delete_lead():
    data = request.get_json()

    for key in data.keys():
        if key != "email":
            return {"error":"Only email is allowed"}, 400

    if type(data["email"]) is not str:
        return {"error":"Email must be an string"},400


    lead = Leads.query.filter(Leads.email == data["email"]).first()

    if not lead:
        return {"error":"Email not found"}, 404

    current_app.db.session.delete(lead)
    current_app.db.session.commit()
    return "", 204

def verify_errors(data):
    phone = data["phone"]
    regex_phone = '^\([1-9]{2}\) ?(?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$'
    if re.fullmatch(regex_phone, phone) == None:
        raise InvalidPhone
    
    for value in list(data.values()):
        if type(value) != str:
            raise InvalidValue


    
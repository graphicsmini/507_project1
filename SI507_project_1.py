from flask import Flask
from lab3_code import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to the banking application!"

@app.route("/bank/<name>")
def bank_name(name):
    bank_name = Bank(name, Dollar, 50)
    return "Welcome to {}!".format(bank_name.name)

@app.route("/dollar/<amt>")
def dollar_amt(amt):
    dollar_amt = Dollar(int(amt))
    return "{}".format(dollar_amt)

@app.route("/yuan/<amt>")
def yuan_amt(amt):
    yuan_amt = Yuan(int(amt))
    return "{}".format(yuan_amt)

@app.route("/pound/<amt>")
def pound_amt(amt):
    pound_amt = Pound(int(amt))
    return "{}".format(pound_amt)

@app.route("/bank/<name>/<currency>/<value>")
def overall(name, currency, value):
    if currency == "dollar":
        random_elm = Dollar

    elif currency == "yuan":
        random_elm = Yuan

    elif currency == "pound":
        random_elm = Pound

    else:
        return "Invalid URL inputs for bank"

    overall_inst = Bank(name, random_elm, int(value))
    return overall_inst.__str__

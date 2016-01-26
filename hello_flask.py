from flask import Flask
import time
from parse_request import parse_request

app = Flask(__name__)

@app.route("/hello")
def hello():
    log("request at " + time.strftime('%X %x %Z'))
    return "Hello World"

@app.route("/parse_all")
def get_all():

    log("Creating parse obj..")
    parse = parse_request()
    log("Parsing......")
    return parse.get_all_in_parse()


def log(toLog):
    print("--> " + toLog)

@app.errorhandler(404)
def page_not_found(error):
    return "WOOOOW! Page not found"

@app.errorhandler(500)
def internal_error(error):
    return "Sorry man...internal error here.."

if __name__ == "__main__":
    log("Start running ....")
    app.run()
    log("Stop application!")

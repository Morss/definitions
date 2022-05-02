import datetime;
import definition;
from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

definition01 = definition.Definition(
  "DEF#97",
  "Occupancy end date is a derived value",
  ["leasing", "occupancy", "end date", "tenancy"],
  ["Caterina Liori", "Johan Doornebal"],
  datetime.datetime(2021, 5, 2),
  "The end date currently is confusing, usually not used by users, is automatically overridden by tenancy end date",
  ["DR#122", "SR-4325", "DEF#44"],
  ["Estatio", "Reporting"], 
  "DR#432")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/definitions")
def definitions():
    return render_template("definitions.html", renderedDefinition=definition01)

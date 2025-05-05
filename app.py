from flask import Flask, render_template, request
from gemini import generate_itinerary
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        try:
            no_of_day = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days
            if no_of_day < 1:
                return render_template("index.html", error="End date must be after start date.")
        except:
            return render_template("index.html", error="Invalid date format.")

        itinerary = generate_itinerary(source, destination, start_date, end_date, no_of_day)
        return render_template("result.html", itinerary=itinerary)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
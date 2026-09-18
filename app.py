from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "wanderly-demo-secret"

# Simple in-memory trip planner data for the practical assessment.
trips = [
    {
        "id": 1,
        "destination": "Ella, Sri Lanka",
        "date": "October 12, 2026",
        "note": "Nine Arches Bridge & Little Adam's Peak",
    },
    {
        "id": 2,
        "destination": "Bali, Indonesia",
        "date": "December 05, 2026",
        "note": "Beach days, temples & sunset dinners",
    },
]


destinations = [
    {
        "name": "Santorini",
        "country": "Greece",
        "tag": "Island escape",
        "image": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1200&q=85",
    },
    {
        "name": "Ella",
        "country": "Sri Lanka",
        "tag": "Mountain adventure",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Little_Adam%27s_Peak%2C_Ella%2C_Sri_Lanka_%28banner%29.jpg/1280px-Little_Adam%27s_Peak%2C_Ella%2C_Sri_Lanka_%28banner%29.jpg",
    },
    {
        "name": "Kyoto",
        "country": "Japan",
        "tag": "Culture & calm",
        "image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=85",
    },
    {
        "name": "Bali",
        "country": "Indonesia",
        "tag": "Tropical retreat",
        "image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1200&q=85",
    },
    {
        "name": "Dubai",
        "country": "UAE",
        "tag": "City lights",
        "image": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1200&q=85",
    },
    {
        "name": "Paris",
        "country": "France",
        "tag": "Romantic city",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=85",
    },
]


@app.route("/")
def home():
    return render_template("index.html", destinations=destinations, trips=trips)


@app.route("/destinations")
def destination_page():
    return render_template("destinations.html", destinations=destinations)


@app.route("/plan", methods=["GET", "POST"])
def plan_trip():
    if request.method == "POST":
        destination = request.form.get("destination", "").strip()
        date = request.form.get("date", "").strip()
        note = request.form.get("note", "").strip()

        if destination and date:
            trips.append(
                {
                    "id": len(trips) + 1,
                    "destination": destination,
                    "date": date,
                    "note": note or "A new adventure is waiting!",
                }
            )
        return redirect(url_for("plan_trip"))

    return render_template("plan.html", trips=trips)


@app.post("/plan/delete/<int:trip_id>")
def delete_trip(trip_id):
    global trips
    trips = [trip for trip in trips if trip["id"] != trip_id]
    flash("Trip removed from your travel board.", "success")
    return redirect(url_for("plan_trip"))


@app.route("/health")
def health():
    return {"status": "healthy", "application": "Wanderly Travel Planner"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

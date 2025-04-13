from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def recommend():
    category = request.form.get("category")

    if category == "skincare":
        return "💧 Our pick: RadiantGlow Vitamin C Serum!"
    elif category == "haircare":
        return "🌿 Our pick: Herbal Hair Strengthening Oil!"
    elif category == "makeup":
        return "💄 Try: DewyMatte Lipstick - Coral Charm"
    elif category == "wellness":
        return "🍵 Suggested: Natural Stress Relief Tea"
    else:
        return "❓ No recommendation found."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

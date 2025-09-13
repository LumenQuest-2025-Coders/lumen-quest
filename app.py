from flask import Flask, request, jsonify
import mysql.connector
from datetime import date, timedelta

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="subscriptions_db"
)
cursor = db.cursor(dictionary=True)

# 1. Get all available plans
@app.route("/plans", methods=["GET"])
def get_plans():
    cursor.execute("SELECT * FROM plans")
    return jsonify(cursor.fetchall())

# 2. Subscribe to a plan
@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json
    user_id, plan_id = data["user_id"], data["plan_id"]
    start = date.today()
    end = start + timedelta(days=30)

    cursor.execute("INSERT INTO subscriptions (user_id, plan_id, start_date, end_date) VALUES (%s,%s,%s,%s)",
                   (user_id, plan_id, start, end))
    db.commit()
    return jsonify({"message": "Subscription successful"})

# 3. Upgrade/Downgrade (update plan_id)
@app.route("/change_plan", methods=["PUT"])
def change_plan():
    data = request.json
    sub_id, new_plan_id = data["subscription_id"], data["new_plan_id"]

    cursor.execute("UPDATE subscriptions SET plan_id=%s WHERE id=%s AND status='active'",
                   (new_plan_id, sub_id))
    db.commit()
    return jsonify({"message": "Plan changed successfully"})

# 4. Cancel subscription
@app.route("/cancel/<int:sub_id>", methods=["PUT"])
def cancel(sub_id):
    cursor.execute("UPDATE subscriptions SET status='cancelled' WHERE id=%s", (sub_id,))
    db.commit()
    return jsonify({"message": "Subscription cancelled"})

# 5. View my subscriptions
@app.route("/my_subscriptions/<int:user_id>", methods=["GET"])
def my_subscriptions(user_id):
    cursor.execute("""SELECT s.id, p.name, p.price, s.status, s.start_date, s.end_date 
                      FROM subscriptions s JOIN plans p ON s.plan_id=p.id 
                      WHERE s.user_id=%s""", (user_id,))
    return jsonify(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
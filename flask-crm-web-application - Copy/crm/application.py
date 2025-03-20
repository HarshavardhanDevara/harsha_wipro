from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from datetime import datetime
from flask_socketio import SocketIO
from collections import defaultdict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Harsha%401807%23@localhost/crm_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/crm_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)

@app.route("/")
def index():
    customers = Customer.query.all()
    return render_template("index.html", customers=customers)

@app.route("/customer-add")
def customer_add_page():
    return render_template("customer-add.html")

@app.route("/customer-add-function", methods=["POST"])
def customer_add():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    company = request.form.get("company")
    phone = request.form.get("phone")
    email = request.form.get("email")
    new_customer = Customer(first_name=first_name, last_name=last_name, company=company, phone=phone, email=email)
    db.session.add(new_customer)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/interaction-data")
def interaction_data():
    interactions = Interaction.query.all()
    return render_template("interaction-data.html", interactions=interactions)

@app.route("/interaction-add")
def interaction_add_page():
    customers = Customer.query.all()
    return render_template("interaction-add.html", customers=customers)

@app.route("/interaction-add-function", methods=["POST"])
def interaction_add():
    customer_id = request.form.get("customer_id")
    date = request.form.get("date")
    description = request.form.get("description")
    new_interaction = Interaction(customer_id=customer_id, date=datetime.fromisoformat(date), description=description)
    db.session.add(new_interaction)
    db.session.commit()
    return redirect(url_for("interaction_data"))

@app.route("/api/customers", methods=["GET"])
def get_customers():
    search = request.args.get('search', '')  # Get the search query from the request
    customers = Customer.query.filter(
        (Customer.first_name.like(f"%{search}%")) |  # Search by first name
        (Customer.last_name.like(f"%{search}%")) |   # Search by last name
        (Customer.company.like(f"%{search}%"))      # Search by company
    ).all()
    return jsonify([customer.to_dict() for customer in customers])  # Return filtered customers as JSON

@app.route("/api/customers/<int:id>", methods=["GET"])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(customer.to_dict())

@app.route("/api/customers", methods=["POST"])
def create_customer():
    data = request.get_json()
    new_customer = Customer(
        first_name=data['first_name'],
        last_name=data['last_name'],
        company=data['company'],
        phone=data['phone'],
        email=data['email']
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify(new_customer.to_dict()), 201

@app.route("/api/customers/<int:id>", methods=["PUT"])
def update_customer(id):
    data = request.get_json()
    customer = Customer.query.get_or_404(id)
    customer.first_name = data['first_name']
    customer.last_name = data['last_name']
    customer.company = data['company']
    customer.phone = data['phone']
    customer.email = data['email']
    db.session.commit()
    return jsonify(customer.to_dict())

@app.route("/api/customers/<int:id>", methods=["DELETE"])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return '', 204

@app.route("/customer-edit/<int:id>")
def customer_edit_page(id):
    customer = Customer.query.get_or_404(id)
    reviews = Review.query.filter_by(customer_id=id).all()
    print(f"Customer: {customer}, Reviews: {reviews}")  # Debugging statement
    return render_template("customer-edit.html", customer=customer, reviews=reviews)

@app.route("/customer-edit-function/<int:id>", methods=["POST"])
def customer_edit(id):
    customer = Customer.query.get_or_404(id)
    customer.first_name = request.form.get("first_name")
    customer.last_name = request.form.get("last_name")
    customer.company = request.form.get("company")
    customer.phone = request.form.get("phone")
    customer.email = request.form.get("email")
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/customer-delete/<int:id>", methods=["POST"])
def customer_delete(id):
    customer = Customer.query.get_or_404(id)
    # Delete all interactions associated with the customer
    Interaction.query.filter_by(customer_id=customer.id).delete()
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/api/interactions", methods=["GET"])
def get_interactions():
    search = request.args.get('search', '')  # Get the search query
    interactions = Interaction.query.filter(
        (Interaction.description.like(f"%{search}%")) |  # Search by description
        # (Interaction.customer_id.like(f"%{search}%"))    # Search by customer ID
        (Interaction.customer_id == search)
    ).all()
    return jsonify([{
        'id': interaction.id,
        'customer_id': interaction.customer_id,
        'date': interaction.date.strftime('%Y-%m-%d'),
        'description': interaction.description
    } for interaction in interactions])

@app.route("/interaction-edit/<int:id>")
def interaction_edit_page(id):
    interaction = Interaction.query.get_or_404(id)
    customers = Customer.query.all()
    return render_template("interaction-edit.html", interaction=interaction, customers=customers)

@app.route("/interaction-edit-function/<int:id>", methods=["POST"])
def interaction_edit(id):
    interaction = Interaction.query.get_or_404(id)
    interaction.customer_id = request.form.get("customer_id")
    interaction.date = datetime.fromisoformat(request.form.get("date"))
    interaction.description = request.form.get("description")
    db.session.commit()
    return redirect(url_for("interaction_data"))

@app.route("/interaction-delete/<int:id>", methods=["POST"])
def interaction_delete(id):
    interaction = Interaction.query.get_or_404(id)
    db.session.delete(interaction)
    db.session.commit()
    return redirect(url_for("interaction_data"))

@app.route("/api/interactions/<int:id>", methods=["DELETE"])
def delete_interaction(id):
    interaction = Interaction.query.get_or_404(id)
    db.session.delete(interaction)
    db.session.commit()
    return jsonify({"message": "Interaction deleted"}), 200

@app.route("/api/interactions/<int:id>", methods=["PUT"])
def update_interaction(id):
    data = request.get_json()
    interaction = Interaction.query.get_or_404(id)
    interaction.customer_id = data["customer_id"]
    interaction.date = datetime.fromisoformat(data["date"])
    interaction.description = data["description"]
    db.session.commit()
    return jsonify({
        "id": interaction.id,
        "customer_id": interaction.customer_id,
        "date": interaction.date.strftime('%Y-%m-%d'),
        "description": interaction.description
    })



@app.route("/interaction-add-function", methods=["POST"])
def interaction_add_with_socket():
    customer_id = request.form.get("customer_id")
    date = request.form.get("date")
    description = request.form.get("description")
    new_interaction = Interaction(customer_id=customer_id, date=datetime.fromisoformat(date), description=description)
    db.session.add(new_interaction)
    db.session.commit()

    # Emit the new interaction event
    socketio.emit('update_interactions', {
        'customer_id': customer_id,
        'date': date,
        'description': description
    })

    return redirect(url_for("interaction_data"))

@app.route("/review-add/<int:customer_id>", methods=["POST"])
def add_review(customer_id):
    rating = request.form.get("rating")
    comment = request.form.get("comment")
    new_review = Review(customer_id=customer_id, rating=rating, comment=comment)
    db.session.add(new_review)
    db.session.commit()
    return redirect(url_for("customer_edit_page", id=customer_id))

@app.route("/reviews")
def reviews():
    reviews = Review.query.all()
    return render_template("reviews.html", reviews=reviews)

# Get all reviews
@app.route("/api/reviews", methods=["GET"])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])

# Get reviews for a specific customer
@app.route("/api/reviews/customer/<int:customer_id>", methods=["GET"])
def get_reviews_by_customer(customer_id):
    reviews = Review.query.filter_by(customer_id=customer_id).all()
    return jsonify([review.to_dict() for review in reviews])

# Add a new review
@app.route("/api/reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    new_review = Review(
        customer_id=data['customer_id'],
        rating=data['rating'],
        comment=data.get('comment', '')  # Default to an empty string if no comment is provided
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201

# Update an existing review
@app.route("/api/reviews/<int:id>", methods=["PUT"])
def update_review(id):
    data = request.get_json()
    review = Review.query.get_or_404(id)
    review.rating = data['rating']
    review.comment = data.get('comment', review.comment)  # Keep the existing comment if not provided
    db.session.commit()
    return jsonify(review.to_dict())

# Delete a review
@app.route("/api/reviews/<int:id>", methods=["DELETE"])
def delete_review(id):
    review = Review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    return '', 204


@app.route("/dashboard")
def dashboard():
    customer_count = Customer.query.count()
    interaction_count = Interaction.query.count()
    review_count = Review.query.count()
    latest_review = Review.query.order_by(Review.timestamp.desc()).first()
    latest_review_timestamp = (
        latest_review.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        if latest_review and latest_review.timestamp
        else "No reviews yet"
    )
    # Calculate monthly interactions
    monthly_interactions = defaultdict(int)
    interactions = Interaction.query.all()
    for interaction in interactions:
        month = interaction.date.strftime('%B')  # Get the month name
        monthly_interactions[month] += 1
    
        
    return render_template(
        "dashboard.html",
        customer_count=customer_count,
        interaction_count=interaction_count,
        review_count=review_count,
        latest_review_timestamp=latest_review_timestamp,
        monthly_interactions=monthly_interactions
    )

# @socketio.on('new_interaction')
# def handle_new_interaction(data):
#     print('New interaction:', data)
#     socketio.emit('update_interactions', data)
@socketio.on('update_interactions')
def handle_update_interactions(data):
    print('New interaction:', data)
    socketio.emit('update_interactions', data)

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))  
    last_name = db.Column(db.String(40))   
    company = db.Column(db.String(80))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(40))
    interactions = db.relationship('Interaction', backref='customer', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company': self.company,
            'phone': self.phone,
            'email': self.email
        }

    def __repr__(self):
        return '<Customer %r %r>' % (self.first_name, self.last_name)

class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    date = db.Column(db.DateTime)
    description = db.Column(db.String(200))

    def __init__(self, customer_id, date, description):
        self.customer_id = customer_id
        self.date = date
        self.description = description

    def __repr__(self):
        return '<Interaction %r>' % self.description

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(255), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Add default timestamp
    
    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'rating': self.rating,
            'comment': self.comment,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S') if self.timestamp else None
        }
        
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
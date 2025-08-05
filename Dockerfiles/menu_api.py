from flask import Flask, jsonify

app = Flask(__name__)

# Dinner menu data
menu = {
    "Starters": {
        "Garlic Bread": 5.99,
        "Bruschetta": 6.49,
        "Stuffed Mushrooms": 7.25
    },
    "Main Courses": {
        "Grilled Salmon": 18.99,
        "Ribeye Steak": 24.50,
        "Chicken Alfredo": 16.75,
        "Vegetable Stir Fry": 14.00
    },
    "Sides": {
        "Mashed Potatoes": 4.50,
        "Steamed Vegetables": 4.25,
        "Side Salad": 3.99
    },
    "Desserts": {
        "Cheesecake": 6.50,
        "Chocolate Lava Cake": 7.00,
        "Ice Cream Sundae": 5.75
    },
    "Beverages": {
        "Soda": 2.50,
        "Iced Tea": 2.75,
        "Coffee": 3.00
    }
}

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

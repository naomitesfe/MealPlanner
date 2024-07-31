from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample meal data
MEALS = {
    'non_fasting': {
        'breakfast': ['Eggs and Toast', 'Pancakes', 'Fruit Smoothie'],
        'lunch': ['Chicken Salad', 'Beef Burger', 'Pasta'],
        'dinner': ['Steak and Vegetables', 'Grilled Chicken', 'Fish Curry'],
        'snacks': ['Nuts', 'Fruit', 'Yogurt']
    },
    'fasting': {
        'breakfast': ['Tsom chechebsa', 'Beso', 'Fruit Salad'],
        'lunch': ['Misir Wat', 'Atkilt Wat', 'Vegetable Stir-fry'],
        'dinner': ['Fasolia', 'Vegetable Soup', 'Spiced Lentils'],
        'snacks': ['Dates', 'Nuts', 'Dried Fruits']
    }
}

@app.route('/')
def home():
    return render_template('home.html', app_name='Personalized Meal Planner')

@app.route('/api/recommendations')
def get_recommendations():
    preference = request.args.get('preference', 'non_fasting')
    meal_type = request.args.get('meal_type', 'all')

    if preference not in MEALS:
        return jsonify({'error': 'Invalid preference'}), 400

    if meal_type == 'all':
        recommendations = MEALS[preference]
    else:
        recommendations = {meal_type: MEALS[preference].get(meal_type, [])}

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

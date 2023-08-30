import nltk
import json
import random
from flask import Flask, request, jsonify

nltk.download('words')
nltk.download('punkt')

app = Flask(__name__)

english_words = set(nltk.corpus.words.words())

# Generate a random audience
@app.route('/')
def generate_random_audience():
    interests = [random.choice(list(english_words)) for _ in range(3)]  # Use random.choice() here
    behaviors = [random.choice(list(english_words)) for _ in range(3)]  # Use random.choice() here
    demographic = {
        "age": random.randint(18, 65),  # Use random.randint() here
        "gender": random.choice(["male", "female"]),
        "marital_status": random.choice(["single", "married", "divorced", "widowed"]),
        "education_level": random.choice(["elementary", "high school", "university", "postgraduate"]),
        "income": random.randint(10000, 100000)  # Use random.randint() here
    }
    custom_audience = random.choice(["teens who like costumes", "otakus", "teens", "teenagers", "adults", "adults who like movies", "gamers who like fantasy games"])
    
    audience = {
        "name": f"My Random Audience {random.randint(1, 100)}",  # Use random.randint() here
        "subtype": "CUSTOM",
        "description": "Randomly generated custom audience",
        "customer_file_source": "USER_PROVIDED_ONLY",
        "interests": interests,
        "behaviors": behaviors,
        "demographics": demographic,
        "custom_audience": custom_audience
    }
    
    return audience

@app.route('/customaudiences', methods=['GET'])
def get_custom_audiences():
    num_audiences = int(request.args.get('num_audiences', 10))  # Default to 10 if not specified
    audiences = [generate_random_audience() for _ in range(num_audiences)]
    return jsonify(audiences)

if __name__ == '__main__':
    app.run(port=5000, debug=False)

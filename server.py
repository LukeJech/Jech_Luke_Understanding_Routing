from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo_time():
    return "Dojo!"

@app.route('/say/<name>')
def waz_up(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:repeats>/<string:word>')
def repeat_word(repeats, word):
    return f"{word * repeats}"

@app.errorhandler(404)
def wrong_page(error):
    return "Sorry there isn't a page here, try again!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


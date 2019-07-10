from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

    
   # import statements, maybe some other routes
@app.route('/dojo')
def dojo():
  return "Dojo"
    

@app.route('/say/<name>')
def flask(name):
  return "Hi " + name


@app.route('/repeat/<num>/<word>')
def times(num,word):
  return (word + " ") * int(num)

if __name__=="__main__":    
    app.run(debug=True)    # Run the app in debug mode.

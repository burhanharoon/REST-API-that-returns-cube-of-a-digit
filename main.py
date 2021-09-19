from flask import Flask, jsonify
app=Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def intro():
    return "<p>&copy This API was created by <strong>Burhan Haroon</strong></p>"

@app.route("/cube/<int:n>")
def cube(n):
    isEven=False
    if n%2 == 0:
        isEven=True

    result ={
        "Number": n,
        "Square": n*n,
        "Cube": n*n*n,
        "Is Even": isEven
    }
    return jsonify(result)
    
if __name__ == "__main__":
    app.run(debug=True)
from flask_app import app
from flask_app.controllers import users,activities,advices

if __name__ == "__main__":
    app.run(debug=True, port=80)
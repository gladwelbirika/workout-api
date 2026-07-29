Workout Application Backend
A Flask-SQLAlchemy REST API for tracking workouts, exercises, and the sets/reps/duration performed in each workout session.

Description
This API allows users to create, view, and delete workouts and exercises, and to link exercises to a workout with reps, sets, and duration data. Validations are enforced at the database, model, and schema levels.

Installation
git clone https://github.com/adisacodes/workout--application-backend.git
cd workout-application-backend
pipenv install
pipenv shell
cd server
flask db upgrade head
python seed.py
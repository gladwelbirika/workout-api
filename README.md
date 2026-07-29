# Workout Application Backend

## Description

A Flask REST API built with Flask-SQLAlchemy and Marshmallow for managing workouts and exercises. The API allows users to create, view, and delete workouts and exercises, and add exercises to workouts with sets, reps, and duration information.

## Installation

```bash
git clone https://github.com/adisacodes/workout--application-backend.git
cd workout-application-backend
pipenv install
pipenv shell
cd server
flask db upgrade head
python seed.py
```

## Run the Application

```bash
python app.py
```

The server runs on:

```text
http://127.0.0.1:5555
```

## API Endpoints

### Workouts

* `GET /workouts` - List all workouts
* `GET /workouts/<id>` - Get a single workout
* `POST /workouts` - Create a workout
* `DELETE /workouts/<id>` - Delete a workout

### Exercises

* `GET /exercises` - List all exercises
* `GET /exercises/<id>` - Get a single exercise
* `POST /exercises` - Create an exercise
* `DELETE /exercises/<id>` - Delete an exercise

### Workout Exercises

* `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` - Add an exercise to a workout with sets, reps, and duration.

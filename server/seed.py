#!/usr/bin/env python3

from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercise

with app.app_context():
    print("Clearing existing data...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding exercises...")
    push_ups = Exercise(name="Push-Ups", category="strength", equipment_needed=False)
    squats = Exercise(name="Squats", category="strength", equipment_needed=False)
    running = Exercise(name="Running", category="cardio", equipment_needed=False)
    yoga = Exercise(name="Yoga Flow", category="flexibility", equipment_needed=True)

    db.session.add_all([push_ups, squats, running, yoga])
    db.session.commit()

    print("Seeding workouts...")
    workout1 = Workout(date=date(2026, 7, 15), duration_minutes=45, notes="Morning strength session")
    workout2 = Workout(date=date(2026, 7, 17), duration_minutes=30, notes="Quick cardio")

    db.session.add_all([workout1, workout2])
    db.session.commit()

    print("Linking exercises to workouts...")
    we1 = WorkoutExercise(workout_id=workout1.id, exercise_id=push_ups.id, reps=15, sets=3, duration_seconds=0)
    we2 = WorkoutExercise(workout_id=workout1.id, exercise_id=squats.id, reps=20, sets=3, duration_seconds=0)
    we3 = WorkoutExercise(workout_id=workout2.id, exercise_id=running.id, reps=0, sets=1, duration_seconds=1800)

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print("Done seeding!")
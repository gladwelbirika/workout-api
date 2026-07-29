from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, ValidationError, validates

ma = Marshmallow()


class ExerciseSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1))
    category = fields.String(
        required=True,
        validate=validate.OneOf(['strength', 'cardio', 'flexibility', 'balance'])
    )
    equipment_needed = fields.Boolean()

    class Meta:
        fields = ('id', 'name', 'category', 'equipment_needed')


class WorkoutExerciseSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    workout_id = fields.Integer(required=True)
    exercise_id = fields.Integer(required=True)
    reps = fields.Integer(validate=validate.Range(min=0))
    sets = fields.Integer(validate=validate.Range(min=0))
    duration_seconds = fields.Integer(validate=validate.Range(min=0))
    exercise = fields.Nested(ExerciseSchema, only=('id', 'name', 'category'), dump_only=True)

    class Meta:
        fields = ('id', 'workout_id', 'exercise_id', 'reps', 'sets', 'duration_seconds', 'exercise')


class WorkoutSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Integer(validate=validate.Range(min=1))
    notes = fields.String()
    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True, exclude=('workout_id',), dump_only=True)

    class Meta:
        fields = ('id', 'date', 'duration_minutes', 'notes', 'workout_exercises')


exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
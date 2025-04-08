from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Explicitly define _id as the primary key
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=128)  # Added password field
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Added _id field as the primary key
    name = models.CharField(max_length=255, unique=True)
    members = models.ManyToManyField('User')  # Changed from ArrayField to ManyToManyField

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Added _id field as the primary key for Activity
    name = models.CharField(max_length=255)
    description = models.TextField()
    activity_type = models.CharField(max_length=100)  # Added activity_type field to match the populate_db script
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Added user field to associate Activity with User
    duration = models.DurationField()  # Added duration field to store activity duration

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Added _id field as the primary key for Leaderboard
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Added user field to associate Leaderboard with User
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.score}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Added _id field as the primary key for Workout
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()
    name = models.CharField(max_length=255)  # Added name field to store the name of the workout
    description = models.TextField()  # Added description field to store workout details

    def __str__(self):
        return f"{self.user.name} - {self.activity.name}"

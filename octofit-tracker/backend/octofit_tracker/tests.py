from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        user = User.objects.create(email='test@hero.com', username='hero', team=team)
        self.assertEqual(user.email, 'test@hero.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='DC', universe='DC')
        self.assertEqual(team.name, 'DC')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        user = User.objects.create(email='test2@hero.com', username='hero2', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2025-11-11')
        self.assertEqual(activity.type, 'Run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='All')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', universe='Marvel')
        user = User.objects.create(email='test3@hero.com', username='hero3', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.rank, 1)

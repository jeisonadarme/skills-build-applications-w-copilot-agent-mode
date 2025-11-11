from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Create Users
        users = [
            User.objects.create(email='tony@stark.com', username='IronMan', team=marvel),
            User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel),
            User.objects.create(email='bruce@wayne.com', username='Batman', team=dc),
            User.objects.create(email='clark@kent.com', username='Superman', team=dc),
        ]

        # Create Workouts
        workout1 = Workout.objects.create(name='Super Strength', description='Heavy lifting', suggested_for='All')
        workout2 = Workout.objects.create(name='Flight Training', description='Aerial maneuvers', suggested_for='Superman, IronMan')

        # Create Activities
        Activity.objects.create(user=users[0], type='Run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Martial Arts', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Fly', duration=50, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))

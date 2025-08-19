from django.core.management.base import BaseCommand
from faker import Faker
from account_module.models import User, Profile
from product_module.models import Product, ProductCategory

class Command(BaseCommand):
    help = 'inserting dummy data'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.faker = Faker()

    
    # def handle(self, *args, **options):
    #     user = User.objects.create_user(username=self.faker.unique.user_name(), password='Nima4030#')
    #     profile = Profile.objects.get(user=user)
    #     profile.first_name = self.faker.first_name()
    #     profile.last_name = self.faker.last_name()
    #     profile.description = self.faker.paragraph(nb_sentences=5)
    #     profile.save()

    def handle(self, *args, **options):
        email = self.faker.unique.email()
        username = self.faker.unique.user_name()

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": username,
                "password": "Nima4030#",
            },
        )

        if created:
            Profile.objects.create(
                user=user,
                first_name=self.faker.first_name(),
                last_name=self.faker.last_name(),
                description=self.faker.paragraph(nb_sentences=5)
            )
            self.stdout.write(self.style.SUCCESS(f"User {user.username} created"))
        else:
            self.stdout.write(self.style.WARNING(f"User with email {email} already exists"))
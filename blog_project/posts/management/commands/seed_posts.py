# your_app/management/commands/seed_posts.py

from django.core.management.base import BaseCommand
from django_seed import Seed
from posts.models import Post, Author

class Command(BaseCommand):
    help = 'Seed the Post model with sample data using a hardcoded author'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        author = Author.objects.first()  # hardcoded author
        if not author:
            self.stdout.write(self.style.ERROR("⚠️ No author found. Please create at least one Author."))
            return

        seeder.add_entity(Post, 20, {
            'author': lambda x: author,
        })

        seeder.execute()
        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded 20 posts with a hardcoded author.'))

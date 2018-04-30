from optparse import make_option

from django.core.management.base import BaseCommand

from api.models import APIToken


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('--comment', dest='comment', type=str)
        parser.add_argument('--handlers', dest='handlers', type=str)

    def handle(self, **options):
        comment = options['comment']
        handlers = options['handlers']
        handlers = list(set(handlers.split(',')))
        assert(len(handlers) > 0)

        token = APIToken.create_token(comment=comment, handlers=handlers)
        print (token.token)

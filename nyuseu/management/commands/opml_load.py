from django.core.management.base import BaseCommand
import opml
from rich import Console
from nyuseu.models import Feeds, Folders

__author__ = 'FoxMaSk'

console = Console()


def load(opml_resource):
    """
    import an OPML file
    """
    if opml_resource.endswith('.opml'):
        o_resource = opml.parse(opml_resource)
        for folder in o_resource:
            for feed in folder:
                log = f"{folder.text}, {feed.text}"
                console.print(log, style="blue")
                # create the target folder if not exists
                try:
                    f = Folders.objects.get(title=folder.text)
                except Folders.DoesNotExist:
                    f = Folders.objects.create(title=folder.text)

                # create the Feeds source if not exists
                try:
                    res = Feeds.objects.get(title=feed.text)
                except Feeds.DoesNotExist:
                    res = Feeds.objects.create(title=feed.text, url=feed.xmlUrl, folder=f)
        console.print('Nyuseu - 뉴스 - Feeds Loaded', style="green")
    else:
        console.print(f"File {opml_resource} is not an OPML file", style="bold red")


class Command(BaseCommand):
    help = 'Import OMPL file'

    def add_arguments(self, parser):
        parser.add_argument("opml_file", help="provide the path to the OPML file", type=str)

    def handle(self, *args, **options):
        load(options['opml_file'])

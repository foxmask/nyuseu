# coding: utf-8
"""
Nyuseu - News - 뉴스
"""

from django.core.management.base import BaseCommand
from rich.console import Console
from nyuseu.models import Folders

__author__ = 'FoxMaSk'

console = Console()


def export(opml_resource):
    """
    export an OPML file
    """
    header = """
<?xml version="1.0" encoding="UTF-8"?>

<opml version="1.0">
    <head>
        <title>Nyuseu subscriptions</title>
    </head>
    <body>
    """
    footer = """    </body>
</opml>
    """
    if opml_resource.endswith('.opml') is False:
        console.print(f"the file you provided {opml_resource} does not have a valid file extension, expected .opml",
                      style="bold red")
    else:
        with open(opml_resource, "w+") as f:
            f.write(header)
            for folder in Folders.objects.all():
                f.write(f'        <outline text="{folder.title}" title="{folder.title}">\n')
                for feed in folder.feeds_set.all():
                    line = f'           <outline type="rss" text="{feed.title}" title="{feed.title}"'
                    line += f'xmlUrl="{feed.url}" htmlUrl="{feed.url}"/>\n'
                    f.write(line)
                f.write('        </outline>\n')
            f.write(footer)

            console.print(f'Nyuseu - 뉴스 - Feeds Exported in file {opml_resource}', style="green")


class Command(BaseCommand):
    help = 'Export OMPL file'

    def add_arguments(self, parser):
        parser.add_argument("opml_file", help="provide the path to the OPML file", type=str)

    def handle(self, *args, **options):
        export(options['opml_file'])

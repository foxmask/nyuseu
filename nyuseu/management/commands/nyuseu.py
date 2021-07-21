# coding: utf-8
"""
Nyuseu - News - 뉴스
"""
from django.core.management.base import BaseCommand
from nyuseu.models import Articles
import pypandoc
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

console = Console()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-id", type=int, help="ID of the article to read")

    def handle(self, *args, **options):

        if options['id']:
            article = Articles.objects.get(id=int(options['id']))
            content = pypandoc.convert_text(article.text, 'markdown_github', format='html')
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("ID")
            table.add_column("Title")
            table.add_column("Body")
            table.add_row(str(article.id),
                          article.title,
                          Markdown(content))
            article.read = True
            article.save()
        else:
            articles = Articles.objects.all()
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("ID")
            table.add_column("Feeds")
            table.add_column("Title")
            table.add_column("Read")
            table.add_column("Later")
            table.add_column("Created")

            for line in articles:
                read = "[green]Unread[/]" if line.read is False else "[yellow]Read[/]"
                read_later = "[green]Unread[/]" if line.read_later is False else "[yellow]Read[/]"
                table.add_row(str(line.id),
                              line.feeds.title,
                              line.title,
                              read,
                              read_later,
                              str(line.date_created))
        console.print(table)

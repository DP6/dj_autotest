from django.core.management.base import BaseCommand
from watchdog.observers import Observer
from dj_autotest.handlers import ChangeHandler
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, '.', recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()

from watchdog.events import FileSystemEventHandler
import os


class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print "Running tests"
            os.system('python manage.py test')

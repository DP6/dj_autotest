from watchdog.events import FileSystemEventHandler
import os


class ChangeHandler(FileSystemEventHandler):
    last_file_changed = ''

    def on_modified(self, event):
        if event.src_path.endswith('.py') and not self.last_file_changed:
            print "Running tests: %s" % event.src_path
            self.last_file_changed = event.src_path
            os.system('python manage.py test')
        else:
            self.last_file_changed = ''

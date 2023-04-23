import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewEmailHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_line = None

    def on_modified(self, event):
        if event.src_path.endswith('.csv'):
            with open(event.src_path, 'r') as file:
                lines = file.readlines()
                if self.last_line is None:
                    self.last_line = len(lines)
                elif len(lines) > self.last_line:
                    # Get the new email address from the last line of the file
                    new_email = lines[-1].strip()

                    # TODO: Send out email using the new_email address
                    pass

                    self.last_line = len(lines)

observer = Observer()
observer.schedule(NewEmailHandler(), path='.')
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

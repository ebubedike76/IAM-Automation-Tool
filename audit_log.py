#!/usr/bin/env python3
import datetime

def log_event(username, event):
    timestamp = datetime.datetime.now()
    with open('audit_log.txt', 'a') as log_file:
        log_file.write(f"{timestamp} - {username}: {event}\n")

    print(f"Logged event: {username} - {event}")

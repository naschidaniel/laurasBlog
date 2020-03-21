import multiprocessing

command = "gunicorn-3"
pythonpath = "/www/site"
bind = "0.0.0.0:3000"
workers = multiprocessing.cpu_count() * 2 + 1
user = "root"
log_file = ""
capture_output = True

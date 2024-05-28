# gunicorn_config.py

bind = "0.0.0.0:8000"
workers = 4  # Number of worker processes
threads = 2  # Number of threads per worker
timeout = 120  # Timeout in seconds

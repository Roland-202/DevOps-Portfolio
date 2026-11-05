import random
import time

from flask import Flask, Response, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

app = Flask(__name__)

REQUESTS = Counter("app_http_requests_total", "HTTP requests", ["method", "endpoint", "status"])
LATENCY = Histogram("app_http_request_duration_seconds", "Request latency", ["endpoint"])


@app.before_request
def start_timer():
    request._start = time.time()


@app.after_request
def record(resp):
    if request.path != "/metrics":
        LATENCY.labels(request.path).observe(time.time() - request._start)
        REQUESTS.labels(request.method, request.path, resp.status_code).inc()
    return resp


@app.route("/")
def index():
    return "Demo app for the Prometheus/Grafana stack\n"


@app.route("/work")
def work():
    time.sleep(random.uniform(0.01, 0.4))
    return "done\n"


@app.route("/flaky")
def flaky():
    if random.random() < 0.2:
        return "boom\n", 500
    return "ok\n"


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

from flask import Flask
import logging
import datetime;

file_handler = logging.FileHandler("app.log")
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

log_message =  "{0}, {1} endpoint was reached"
app = Flask(__name__)

@app.route("/status")
def status():
  logger.info(log_message.format(datetime.datetime.now(), "/status"))
  return { "result": "OK - healthy" }

@app.route("/metrics")
def metrics():
  logger.info(log_message.format(datetime.datetime.now(), "/metrics"))
  return {"data": {"UserCount": 150, "UserCountActive": 30}} 

@app.route("/")
def hello():
    logger.info(log_message.format(datetime.datetime.now(), "/"))
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

from flask  import Flask
app.flask(__name__)
@app.route("/")
def home():
  return "CI/CD pipeline is Running...")
if __main__ = "__name__":
app.run()

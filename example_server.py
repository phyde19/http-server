from sparrow import Sparrow

app = Sparrow()


# Middleware example
@app.use
def logger(req, res, next_func):
    print(f"{req.method} {req.path}")
    next_func()


# Route handlers
@app.get("/hello")
def hello(req, res):
    res.send("Hello, world!")


@app.get("/users/:user_id")
def get_user(req, res):
    user_id = req.params.get("user_id")
    res.json({"user": user_id})


@app.post("/echo")
def echo(req, res):
    res.json({"received": req.body})


if __name__ == "__main__":
    app.listen(port=8080)

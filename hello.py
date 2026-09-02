def greet(name):
    return f"hello {name}"


if __name__ == "__main__":
    assert greet("world") == "hello world"
    print("ok")

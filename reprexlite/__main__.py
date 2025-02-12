from reprexlite.cli import app

if __name__ == "__main__":
    app._name = ("python -m reprexlite",)
    app()

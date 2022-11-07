import typer
from rich import print

app = typer.Typer()


@app.command()
def rich_data():
    data = {
        "name": "Rick",
        "age": 42,
        "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
        "active": True,
        "affiliation": None,
    }
    print("Here is the data")
    print(data)
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


@app.command()
def hello(name: str):
    """
    Welcome `name`.

    :param name: The name
    :return: The return value
    """
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    """
    Welcome `name`.

    :param name: The name
    :param formal: The formality
    :return: The return value
    """
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

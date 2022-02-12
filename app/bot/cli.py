import typer

app = typer.Typer()

from app.bot.telegram_bot import run


@app.command()
def telegram():
    run()


if __name__ == "__main__":
    app()

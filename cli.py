import typer

from app.user.cli import app as user_app
from app.bot.cli import app as bot_app

app = typer.Typer()
app.add_typer(user_app, name="users")
app.add_typer(bot_app, name="bots")


if __name__ == "__main__":
    app()

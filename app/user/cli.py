import typer

app = typer.Typer()

from app.core.db import get_db_ctx
from app.user.service import create_user
from app.user.schemas import UserCreate


@app.command()
def create(
    email: str = typer.Option(...),
    password: str = typer.Option(
        ..., prompt=True, confirmation_prompt=True, hide_input=True
    ),
):
    with get_db_ctx() as db:
        create_user(db, UserCreate(email=email, password=password))

    typer.echo(f"User {email} successfully created")


if __name__ == "__main__":
    app()

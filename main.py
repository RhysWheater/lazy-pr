import os
import typer
from github import Github
from github.Auth import Token


app = typer.Typer()


def get_github():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        typer.echo("Missing $GITHUB_TOKEN", err=True)
        raise typer.Exit(1)
    return Github(auth=Token(token))


@app.command()
def list_prs(repo: str):
    g = get_github()
    for pr in g.get_repo(repo).get_pulls(state="open"):
        typer.echo(f"#{pr.number} {pr.title} - {pr.user.login}")


@app.command()
def say_hello():
    typer.echo('hello')


if __name__ == "__main__":
    app()

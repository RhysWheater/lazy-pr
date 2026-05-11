import os

import typer
from git import Repo
from github import Github
from github.Auth import Token
from pathlib import Path

app = typer.Typer()


def get_github() -> Github:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        typer.echo("Missing $GITHUB_TOKEN", err=True)
        raise typer.Exit(1)
    return Github(auth=Token(token))


@app.command()
def list_prs(remote: str = None) -> None:
    if not remote:
        repo = Repo(Path.cwd())
        remote = repo.remotes[0]
    g = get_github()
    for pr in g.get_remote(remote).get_pulls(state="open"):
        typer.echo(f"#{pr.number} {pr.title} - {pr.user.login}")


@app.command()
def say_hello() -> None:
    typer.echo('hello')


if __name__ == "__main__":
    app()

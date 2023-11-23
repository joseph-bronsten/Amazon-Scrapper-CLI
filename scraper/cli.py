import typer
import scraper

from rich.console import Console
from rich.table import Table
from rich import print

app = typer.Typer()
console = Console()

@app.command()
def display():
    updateAll()
    items = scraper.getSavedItems()
    table = Table("#", "Name", "Current Price", "Lowest Price", "Last Checked","url")
    for i, item in enumerate(items):
        table.add_row(str(i+1),
                      item["name"],
                      str(item["current-price"]),
                      str(item["lowest-price"]),
                      item["last-checked"],
                      item["url"])
    console.print(table)

@app.command()
def addItem(url:str):
   item = scraper.makeItem(url)
   items = scraper.addItem(item)

@app.command()
def removeItem(index:int):
   scraper.removeItem(index-1)


def updateAll():
    items = scraper.getSavedItems()
    updated_items = []
    for item in items:
        updated_item = scraper.updateItem(item)
        updated_items.append(updated_item)
    scraper.saveItems(updated_items)

if __name__ == "__main__":
  app()
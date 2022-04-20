#!usr/bin/python3
from rich.console import Console
from rich.table import Table

import scraped as srp

console = Console()
table = Table(show_header=True)

table.add_column("P")
table.add_column("Name")
table.add_column("GP")
table.add_column("W")
table.add_column("D")
table.add_column("L")
table.add_column("F")
table.add_column("A")
table.add_column("GD")
table.add_column("Pts", style="bold")
table.add_column("Form")


def determine_result(result_data):
    results = result_data.split("\n\n")
    for result in results:
        if "Won " in result:
            results[results.index(result)] = "[green]W[/green]"
        elif "Drew " in result:
            results[results.index(result)] = "[yellow]D[/yellow]"
        elif "Lost " in result:
            results[results.index(result)] = "[red]L[/red]"
    return results


def concat_results(results: list):
    return "".join(results)



for position in range(0, 19):
    table.add_row(srp.get_table()[position+1][0], srp.get_table()[position+1][1], srp.get_table()[position+1][2], srp.get_table()[position+1][3], srp.get_table()[position+1]
                  [4], srp.get_table()[position+1][5], srp.get_table()[position+1][6], srp.get_table()[position+1][7], srp.get_table()[position+1][8], srp.get_table()[position+1][9], concat_results(determine_result(srp.get_table()[position+1][10])))




if __name__ == "__main__":
    console.print(table)

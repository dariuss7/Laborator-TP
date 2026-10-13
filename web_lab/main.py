import argparse
import csv
# 44
import webtools
from webtools import check_paths, get_title, security_headers

# 45
# Dacă main.py ar avea o funcție proprie numită `get_title`, redefinirea ei locală
# ar da override funcției `get_title` importată anterior din webtools.

BASE_URL = "https://cybercor.org"

if __name__ == "__main__":
    # 48
    parser = argparse.ArgumentParser(description="Analizor Web")
    parser.add_argument("url", nargs="?", default=BASE_URL, help="URL-ul țintă")
    args = parser.parse_args()

    target_url = args.url

    # 44
    print(
        "Titlu:", webtools.get_title(webtools.fetch(target_url).text)
    )

    # 47
    print("Constanta User-Agent:", webtools.DEFAULT_HEADERS)

    # 49
    paths_data = check_paths(target_url)
    with open(
        "report.csv", mode="w", newline="", encoding="utf-8"
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=["path", "status", "checked_at"]
        )
        writer.writeheader()
        for row in paths_data:
            writer.writerow(row)
    print("Raportul CSV a fost salvat în report.csv")

    # 50
    print("\nRulare raport complet:")
    webtools.site_report(target_url)
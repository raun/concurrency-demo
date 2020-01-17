
import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print("Read {} from {}".format(len(response.content), url))


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.amazon.com",
        "https://www.stackoverflow.com/",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print("Downloaded {} in {} seconds".format(len(sites), duration))
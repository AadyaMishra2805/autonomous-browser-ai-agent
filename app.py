from fastapi import FastAPI
from playwright.sync_api import sync_playwright

app = FastAPI()


@app.get("/search")
def search(query: str):

    results_data = []

    with sync_playwright() as p:

        # HIDDEN BROWSER
        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )

        # OPEN BING
        page.goto(
            f"https://www.bing.com/search?q={query}",
            wait_until="domcontentloaded",
            timeout=60000
        )

        # WAIT FOR RESULTS
        page.wait_for_timeout(5000)

        # GET SEARCH RESULT LINKS
        results = page.locator("li.b_algo h2 a")

        count = results.count()

        # TOP 5 RESULTS
        for i in range(min(count, 5)):

            try:

                title = results.nth(i).inner_text()
                link = results.nth(i).get_attribute("href")

                if title and link:

                    results_data.append({
                        "title": title,
                        "link": link
                    })

            except Exception as e:
                print(e)

        browser.close()

    return {
        "query": query,
        "results": results_data
    }
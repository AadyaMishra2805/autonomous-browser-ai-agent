import os


SEARCH_QUERY = "best gaming laptop"


def search_with_tavily(query):
    """Run the search query via Tavily API and print results."""
    from tavily import TavilyClient

    client = TavilyClient()
    response = client.search(query=query, max_results=5, search_depth="basic")

    results = response.get("results", [])
    if not results:
        print("No results found.")
        return

    # Print first result details (mirrors the DuckDuckGo flow)
    first = results[0]
    print("Opening:", first["title"])
    print("\nWebsite Title:")
    print(first["title"])
    print("\nContent:\n")
    print(first.get("content", ""))

    # Print remaining results
    if len(results) > 1:
        print("\nAdditional Results:\n")
        for r in results[1:]:
            print(f"- {r['title']}: {r['url']}")


def search_with_duckduckgo(query):
    """Run the search query via DuckDuckGo using Playwright browser automation."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        # Open DuckDuckGo
        page.goto("https://duckduckgo.com")

        # Search query
        page.fill('input[name="q"]', query)

        page.keyboard.press("Enter")

        page.wait_for_timeout(3000)

        # Get search results
        results = page.locator("a[data-testid='result-title-a']")

        # First result
        first_result = results.nth(0)

        # Print title
        print("Opening:", first_result.text_content())

        # Click first result
        first_result.click()

        page.wait_for_timeout(5000)

        # Extract webpage title
        title = page.title()

        print("\nWebsite Title:")
        print(title)

        # Extract paragraphs
        paragraphs = page.locator("p").all_text_contents()

        print("\nFirst 5 Paragraphs:\n")

        for para in paragraphs[:5]:

            if para.strip():
                print(para)
                print()

        page.wait_for_timeout(10000)


if __name__ == "__main__":
    if os.environ.get("TAVILY_API_KEY"):
        print("[Using Tavily search]\n")
        search_with_tavily(SEARCH_QUERY)
    else:
        print("[Using DuckDuckGo via Playwright]\n")
        search_with_duckduckgo(SEARCH_QUERY)
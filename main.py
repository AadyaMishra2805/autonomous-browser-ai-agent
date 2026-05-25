from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    # Open DuckDuckGo
    page.goto("https://duckduckgo.com")

    # Search query
    page.fill('input[name="q"]', "best gaming laptop")

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
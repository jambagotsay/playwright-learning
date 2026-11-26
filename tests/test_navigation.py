import re
from playwright.sync_api import Page, expect


def test_docs_link_opens_installation_page(page: Page) -> None:
    page.goto("https://playwright.dev/python/")
    page.get_by_role("link", name="Docs").click()
    expect(page).to_have_url(re.compile("intro"))
    installation_heading = page.get_by_role("heading", name="Installation", exact=True)
    expect(installation_heading).to_be_visible()
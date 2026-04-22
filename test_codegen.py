import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="Direct link to Introduction").click()
    page.get_by_role("code").filter(has_text="npm init playwright@latest").click()
    page.get_by_role("link", name="playwright.config").first.click()

from playwright.sync_api import Page, Locator, expect


def expect_text_visible(page: Page, text: str, timeout: int = 30000) -> None:
    expect(page.get_by_text(text)).to_be_visible(timeout=timeout)


def expect_url_contains(page: Page, path: str, timeout: int = 30000) -> None:
    expect(page).to_have_url(path, timeout=timeout)


def expect_element_enabled(locator: Locator, timeout: int = 30000) -> None:
    expect(locator).to_be_enabled(timeout=timeout)


def expect_element_hidden(locator: Locator, timeout: int = 30000) -> None:
    expect(locator).to_be_hidden(timeout=timeout)


def expect_count(locator: Locator, count: int, timeout: int = 30000) -> None:
    expect(locator).to_have_count(count, timeout=timeout)


def expect_attribute(locator: Locator, name: str, value: str, timeout: int = 30000) -> None:
    expect(locator).to_have_attribute(name, value, timeout=timeout)

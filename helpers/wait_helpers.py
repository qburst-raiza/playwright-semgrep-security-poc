from playwright.sync_api import Page, Locator


def wait_for_url(page: Page, url: str, timeout: int = 30000) -> None:
    page.wait_for_url(url, timeout=timeout)


def wait_for_selector(page: Page, selector: str, timeout: int = 30000) -> None:
    page.wait_for_selector(selector, state="visible", timeout=timeout)


def wait_for_network_idle(page: Page, timeout: int = 30000) -> None:
    page.wait_for_load_state("networkidle", timeout=timeout)


def wait_for_element_stable(locator: Locator, timeout: int = 30000) -> None:
    locator.wait_for(state="visible", timeout=timeout)


def wait_for_hidden(locator: Locator, timeout: int = 30000) -> None:
    locator.wait_for(state="hidden", timeout=timeout)

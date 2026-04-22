# from playwright.sync_api import Page, expect

# def test_has_title(page: Page):
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#     page.locator("input[placeholder='Username']").fill("Admin")

#     page.locator("input[placeholder='Password']").fill("admin123")

#     page.locator("button[type='submit']").click()

#     page.locator(".oxd-userdropdown-tab").click()

#     # page.locator("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()




#     page.wait_for_timeout(100000)


from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=60000, wait_until="domcontentloaded")

    page.locator("//input[@placeholder='Username']").fill("Admin")

    page.locator("//input[@placeholder='Password']").fill("admin123")

    page.locator("//button[normalize-space()='Login']").click()

    # page.locator(".oxd-userdropdown-tab").click()

    # page.locator("body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > header:nth-child(2) > div:nth-child(1) > div:nth-child(3) > ul:nth-child(1) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()




    page.wait_for_timeout(100000)
from playwright.sync_api import sync_playwright, expect
import functools
import time

common_delay = 3

def Try_Except(func):
    @functools.wraps(func)
    def wrapper(self:Web_Automation_Test, *args, **kwargs):
        title = func.__name__
        try:
            result = func(self, *args, **kwargs)
            print(f"Pass : {title}")
            return result
        except Exception as log:
            print(f"Fail : {title}")
            #self.page.screenshot()
            print(log)
            raise
    return wrapper


class Web_Automation_Test:

    def __init__(self):

        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, slow_mo=500,args=["--start-maximized"])
        
        self_context = self.browser.new_context(no_viewport=True, permissions=["microphone", "clipboard-read", "clipboard-write"])
        self.page = self_context.new_page()
        self.page.set_default_timeout(5000)


    def Open_Url(self, Url):
        self.page.goto(Url)

    @Try_Except
    def Login(self, Type = None):
        user_type ={"standard" : "standard_user",
                    "locked" : "locked_out_user",
                    "not_account" : "abcde",
                    "problem" : "problem_user",
                    "performance" : "performance_glitch_user"}
        
        self.page.get_by_placeholder("Username").fill(user_type[Type])
        self.page.get_by_placeholder("Password").fill("secret_sauce")
        self.page.locator('[data-test="login-button"]').nth(0).click()
        if(Type == "not_account"): expect(self.page.locator('[data-test="error"]')).to_contain_text("Epic sadface: Username and password do not match any user in this service")
        else : expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        time.sleep(common_delay)

    @Try_Except
    def Logout(self):
        self.page.get_by_role("button", name="Open Menu").click()
        self.page.locator('[data-test="logout-sidebar-link"]').click()

        expect(self.page).to_have_url("https://www.saucedemo.com/")
        expect(self.page.locator('[data-test="login-button"]')).to_be_visible()
        time.sleep(common_delay)

    @Try_Except
    def Purchase_item(self, item_id = None, Type = None):
        if(Type == "Detail"):
            item = {"0" : "inventory-item-sauce-labs-bike-light-img",
                    "1" : "inventory-item-sauce-labs-bolt-t-shirt-img",
                    "2" : "inventory-item-sauce-labs-onesie-img",
                    "3" : "inventory-item-test.allthethings()-t-shirt-(red)-img",
                    "4" : "inventory-item-sauce-labs-backpack-img",
                    "5" : "inventory-item-sauce-labs-fleece-jacket-img"}
            
            self.page.locator(f'[data-test="{item[item_id]}"]').click()
            self.page.locator('[data-test="add-to-cart"]').click()

        elif(Type == "List"):
            self.page.locator(".btn.btn_primary.btn_small.btn_inventory").nth(item_id).click()
            self.page.locator(".btn.btn_secondary.btn_small.btn_inventory").nth(item_id).click()
            self.page.locator(".btn.btn_primary.btn_small.btn_inventory").nth(item_id).click()

        expect(self.page.locator('[data-test="shopping-cart-badge"]')).to_be_visible()

        self.page.locator('[data-test="shopping-cart-link"]').click()
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")

        self.page.locator('[data-test="checkout"]').click()

        self.page.locator('[data-test="continue"]').click()
        expect(self.page.locator('[data-test="error"]')).to_contain_text("Error: First Name is required")

        self.page.locator('[data-test="firstName"]').fill("ABC")
        self.page.locator('[data-test="continue"]').click()
        expect(self.page.locator('[data-test="error"]')).to_contain_text("Error: Last Name is required")

        self.page.locator('[data-test="lastName"]').fill("DEF")
        self.page.locator('[data-test="continue"]').click()
        expect(self.page.locator('[data-test="error"]')).to_contain_text("Error: Postal Code is required")

        self.page.locator('[data-test="postalCode"]').fill("12345")
        self.page.locator('[data-test="continue"]').click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

        self.page.locator('[data-test="finish"]').click()
        expect(self.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
        
        self.page.locator('[data-test="back-to-products"]').click()
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")
        time.sleep(common_delay)

    @Try_Except
    def Check_Item_Images(self):
        images = self.page.locator('img.inventory_item_img')
        srcs = [images.nth(i).get_attribute("src") for i in range(images.count())]
        assert len(set(srcs)) == len(srcs), print(f"중복된 상품 이미지가 있습니다: {srcs}")

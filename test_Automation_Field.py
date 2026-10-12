
def test_not_account_login(web):
    web.Login("not_account")


def test_standard_login(web):
    web.Login("standard")


def test_item_images(web):
    web.Login("standard")
    web.Check_Item_Images()


def test_purchase(web):
    web.Login("standard")
    web.Purchase_item(0, "Detail")


def test_logout(web):
    web.Login("standard")
    web.Logout()

##계정 상태별 검증##
#미등록 계정
def test_not_account_login(web):
    web.Login("not_account")

#잠긴 계정
def test_locked_account_login(web):
    web.Login("locked")

#일반 계정
def test_standard_login(web):
    web.Login("standard")
    
#상품 이미지 중복 체크
def test_check_item_images(web):
    web.Login("standard")
    web.Check_Item_Images()

#상품 구매
def test_purchase(web):
    web.Login("standard")
    web.Purchase_item(0)

#로그아웃
def test_logout(web):
    web.Login("standard")
    web.Logout()
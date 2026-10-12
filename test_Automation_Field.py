
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
    

#상품 이미지 중복 계정
def test_problem_account_login(web):
    web.Login("problem")
    web.Check_Item_Images()

#성능 저하 계정
def test_performance_account_login(web):
    web.Login("performance")

#장바구니 담기 불가 계정
def test_error_account_login(web):
    web.Login("error")
    web.Error_Account_Item_Select()





#상품 구매
def test_purchase(web):
    web.Login("standard")
    web.Purchase_item(0, "Detail")

#로그아웃
def test_logout(web):
    web.Login("standard")
    web.Logout()
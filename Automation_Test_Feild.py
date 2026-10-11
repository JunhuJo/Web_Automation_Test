from Automation_Test_Method import Web_Automation_Test

Web_Test = Web_Automation_Test()


#홈페이지 열기
Web_Test.Open_Url("https://www.saucedemo.com/")

####홈페이지 로그인 > 상품 구매 시나리오####

#등록되지 않은 계정 로그인 시도
Web_Test.Login("not_account")

#정상 계정으로 로그인
Web_Test.Login("standard")

#상품 이미지 중복 여부 체크
Web_Test.Check_Item_Images()

#상품 구매
Web_Test.Purchase_item(0, "Detail")

#홈페이지 로그아웃
Web_Test.Logout()
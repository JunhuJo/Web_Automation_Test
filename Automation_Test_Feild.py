from Automation_Test import Web_Automation_Test

Web_Test = Web_Automation_Test()

#==========================

#홈페이지 열기
Web_Test.Open_Url("https://www.saucedemo.com/")

#홈페이지 로그인
#Web_Test.Login("not_account")
Web_Test.Login("standard")
Web_Test.Check_Item_Images()

#상품 구매
Web_Test.Purchase_item(0, "List")

#홈페이지 로그아웃
Web_Test.Logout()

#===========================

# #상품 이미지 중복 케이스
# Web_Test.Login("problem")
# Web_Test.Check_Item_Images()
# Web_Test.Logout()

#============================
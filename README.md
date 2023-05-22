# Software-Engineering
소공 팀플


Model: models 폴더 내에 데이터 모델과 데이터베이스 연결을 담당하는 코드를 구현하여, 데이터와 관련된 작업을 수행합니다.
View: templates 폴더 내에 HTML 템플릿 파일을 작성하여 클라이언트에게 보여줄 화면을 구성합니다.
Controller: routes 폴더 내에 라우트 함수들을 구현하여 클라이언트의 요청을 처리하고, 필요한 데이터를 Model과 View 사이에서 조정하고 전달합니다.



# 주의
 로그인 세션은 routes에서 처리되어야 한다. 로그인이 성공한 경우 session["username"]에 사용자명을 저장하는 것은 routes에서 처리한다.models에서 세션을 조작하는 것은 디자인상 권장되지 않으며, 세션은 주로 routes에서 사용자 인증과 관련된 로직을 처리하는 데에 사용된다ㅏ.

# 할 일
1.models 내의 db.py를 utils폴더로 이동시킬 것
2.coin,money를 user_coin, user_money로 바꿔야 할 듯?
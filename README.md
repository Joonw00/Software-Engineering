## Software-Engineering

# MVC 모델
Model: models 폴더 내에 데이터 모델과 데이터베이스 연결을 담당하는 코드를 구현하여, 데이터와 관련된 작업을 수행합니다. <br>
View: templates 폴더 내에 HTML 템플릿 파일을 작성하여 클라이언트에게 보여줄 화면을 구성합니다.<br>
Controller: routes 폴더 내에 라우트 함수들을 구현하여 클라이언트의 요청을 처리하고, 필요한 데이터를 Model과 View 사이에서 조정하고 전달합니다.



# 주의
 로그인 세션은 routes에서 처리되어야 한다. 로그인이 성공한 경우 session["username"]에 사용자명을 저장하는 것은 routes에서 처리한다.models에서 세션을 조작하는 것은 디자인상 권장되지 않으며, 세션은 주로 routes에서 사용자 인증과 관련된 로직을 처리하는 데에 사용된다ㅏ.

# 할 일
1.models 내의 db.py를 utils폴더로 이동시킬 것 <br>
2.url경로들에 router 이름 붙이기 ex:user/login, user/signup <br>
3.페이징 기능 필요. 테이블이 너무 길어짐. (url에 페이지 받아와서 routes에서 처리하면 될 듯) <br>

# 코인 거래 시스템 (Coin Trading System)

이 프로젝트는 코인 거래 시스템을 구현하는 것입니다.

| ![웹페이지 사진 1](./path/to/image1.png) | ![웹페이지 사진 2](./path/to/image1.png) |
|:---:|:---:|
| 웹페이지 사진 1 설명 | 웹페이지 사진 2 설명 |
| ![웹페이지 사진 3](./path/to/image1.png) | ![웹페이지 사진 4](./path/to/image1.png) |
| 웹페이지 사진 3 설명 | 웹페이지 사진 4 설명 |

## 사용 방법

프로젝트를 어떻게 사용하는지에 대한 방법 기술

<!-- 1. 이 레포지토리를 클론하세요: `git clone https://github.com/your-username/your-repo.git`
2. 필요한 패키지를 설치하세요: `pip install -r requirements.txt`
3. 웹 서버를 실행하세요: `python app.py`
4. 브라우저에서 http://localhost:5000 을 열고 확인하세요. -->


## 사용된 기술 스택

이 프로젝트에서 사용된 기술 스택은 다음과 같습니다:

- Flask
- Python
- JavaScript
- MongoDB


## ERD 구조

이 프로젝트의 데이터베이스 구조는 다음과 같습니다:

![ERD 구조](./path/to/erd.png)

## Simple Project 2 ##

----

### 개발 시 필수 사항 

- PEP8
- Python 3.8
- Django 2.2.24
- requirements.txt or pyproject.toml
- README.md 실행 방법 명시
- API를 실행할 수 있는 Postman Export 결과 or API 테스트를 수행하는 테스트코드 작성

### 개발 시 참고사항
- SECRET_KEY 같은 비밀키 값은 프로젝트 내 포함할 것


### 그외 추가 사항
- 테스트 코드 작성
    - pytest를 활용한 테스트 코드 작성
    - 테스트 실행 방법을 README.md에 작성
    - 커버리지 측정은 codecov를 권장

- CI를 활용한 테스트 자동화 및 커버리지 결과 전송 (Github Action 권장)

- Docker
    - 하나의 컨테이너에 웹 서버 및 WSGI 애플리케이션이 실행되도록 Dockerfile 작성 또는 docker-compose.yml 작성



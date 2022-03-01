# django_orm_study

## 소개
- 이 프로젝트는 Django ORM을 공부하기 위해 만든 프로젝트입니다.
- 아래 Reference를 참고하여 작성하였습니다.

## 실행 방법
1. git clone git@github.com:jotasic/django_orm_study.git
2. pip install -r requirements.txt
  - m1의의 경우 psycopg2 설치시 에러가 날 수 있다.
  - psycopg2-binary를 설치하고, requirements.txt에서 psycopg2를 지우고 패키지 설치를 진행한다.
3. docker-compose up -d (PostgreSQL 컨테이너 실행)
4. python manage.py migrate
5. python manage.py create_dummy_data // 더미 데이터 삽입
... 작성중...

## Reference
- [Django ORM Cookbook(en)](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/)
- [Django ORM Cookbook(ko)](https://django-orm-cookbook-ko.readthedocs.io/en/latest/)
- [Django ORM (QuerySet)구조와 원리 그리고 최적화전략 - 김성렬님 ](https://www.youtube.com/watch?v=EZgLfDrUlrk)
  - [세션 자료](https://github.com/KimSoungRyoul/Django_ORM_pratice_project)

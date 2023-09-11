<h1>IDNA RESTful API </h1>

<h2>인스톨</h2>
<pre><code>
pip install -r requirements.txt
</pre></code>

<h2>실행</h2>
<pre><code>
python manage.py runserver
</pre></code>

<h2>마이그레이션</h2>
<pre><code>
python manage.py makemigrations
</pre></code>

<h2>폴더 구조</h2>
<h5>Application Factory Pattern</h5>

.<br>
├── test_project<br>
│   ├── test_project.py<br>
│   │   ├── __init__.py<br>
│   │   ├── setting.py<br>
│   │   └── urls.py<br>
│   ├── [app-name].py<br>
│   │   ├── __init__.py<br>
│   │   ├── models.py<br>
│   │   ├── serializers.py<br>
│   │   ├── urls.py<br>
│   │   └── views.py<br>
├── requirements.txt<br>
└── manage.py<br>


* test_project - django 앱 base dir
* setting - django setting 
* urls - api 앤드 포인트
* [app-name] - 사용자 서비스 app
* models - DB 테이블 정의 
* serializers - 시리얼라이져
* urls - api 앤드 포인트
* views - 서비스 뷰

<h3>파이썬 버전</h3>
Python 3.6.7

<h3>참고자료</h3>
https://wisdom-990629.tistory.com/
https://docs.djangoproject.com/en/3.1/
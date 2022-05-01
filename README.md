# flask_app_demo:1.0

1. flask_app_demo 컨테이너 올리기

```bash
# 깃헙 클론
gh repo clone ChoiSeongRyeong/little_projects

# 폴더로 이동
cd flask_app_demo_v1

# flask_app_demo image build
docker build -t flask_app_demo:1.0 .

# flask_app_demo run
docker run -d -p 15000:5000 flask_app_demo:1.0
```

1. jupyter 컨테이너 올리기

```bash
docker run -d -p 18888:8888 jupyter/scipy-notebook
```

1. jupyter 컨테이너 토큰 확인

```bash
# container list -> 'jupyter/scipy-notebook'의 'CONTAINER ID' 확인
docker ps

# container bash 실행
docker exec -it {CONTAINER_ID} /bin/bash

# jupyter notebook token 확인
~$ jupyter notebook list

# 토큰 복사 후 jupyter notebook 웹으로 로그인(http://127.0.0.1:18888)
```

![스크린샷 2022-05-01 오후 7.57.16.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a4126798-5305-415a-99e3-f0512c056983/스크린샷_2022-05-01_오후_7.57.16.png)

1. flask app 동작 확인

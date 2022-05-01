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

2. jupyter 컨테이너 올리기

```bash
docker run -d -p 18888:8888 jupyter/scipy-notebook
```

3. jupyter 컨테이너 토큰 확인

```bash
# container list -> 'jupyter/scipy-notebook'의 'CONTAINER ID' 확인
docker ps

# container bash 실행
docker exec -it {CONTAINER_ID} /bin/bash

# jupyter notebook token 확인
~$ jupyter notebook list

# 토큰 복사 후 jupyter notebook 웹으로 로그인(http://127.0.0.1:18888)
```

4. flask app 동작 확인
```python
## jupyter notebook
import requests
import pandas as pd
import numpy as np

# ip = {외부IP -> naver에서 "내ip" 검색}

result1 = requests.get(f"http://{ip}:15000/")
print(result1.content)
>> b'Hello Flask World'

df = pd.DataFrame(np.arange(20).reshape(5,4))

result2 = requests.post(f"http://{ip}:15000/get_shape", json={'df':df.to_json()})
print(result2.json()['shape'])
>> [5, 4]

result3 = requests.post(f"http://{ip}:15000/get_preprocessed_df", json={'df':df.to_json()})
print(pd.DataFrame(result3.json()))
>> index	0	1	2	3
0	0	0	1	2	3
1	1	4	5	6	7
2	2	8	9	10	11
3	3	12	13	14	15
4	4	16	17	18	19

result4 = requests.post(f"http://{ip}:15000/get_preprocessed_df_and_shape", json={'df':df.to_json()})
print(result4.headers['shape'])
>> (5, 5)
print(pd.DataFrame(result4.json()))
>> index	0	1	2	3
0	0	0	1	2	3
1	1	4	5	6	7
2	2	8	9	10	11
3	3	12	13	14	15
4	4	16	17	18	19
```

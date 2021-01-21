# streamlit-todo
todo list 관리를 위한 todo 웹페이지 입니다. 

![](https://img.shields.io/badge/python-3.6.1-blue)

### 설치 방법 (How To Install)

```sh
pip3 install requirements.txt
```

### 사용 방법 (Example)

streamlit run todo.py {DB_PATH}

DB_PATH (생략가능): 
- DB가 저장될 경로입니다. 디렉토리가 없다면 자동생성되며 .db 파일포맷으로 지정해야합니다.

#### example
1. foreground 실행 

  streamlit run todo.py
  
2. background 실행

  nohup streamlit run todo.py 1>todo.log 2>&1 & 

Tips
서버를 백그라운드에서 유지되도록 하고 싶다면
nohup streamlit run todo.py 1>todo.log 2>&1 & 
와 같이 nohup을 이용하시면 편합니다.

![](img.png)



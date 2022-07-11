# streamlit-todo
This is a TodoApp using streamlit

![](https://img.shields.io/badge/python-3.7-blue)

## 커피 한잔만 사주세요 (Please give me a coffee) 🐥
<a href="https://www.buymeacoffee.com/heewinkim" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## 바로 실행해 보기 (Direct Execute using Streamlit) 🐹
[![Run on Streamlit](https://img.shields.io/badge/Run-STREAMLIT-green)](https://heewinkim-streamlit-todo-todo-xb11i5.streamlitapp.com/)

## 바로 실행해 보기 (Direct Execute using Ainize) 🦊
[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/heewinkim/streamlit-todo)


## 빠른 설치 & 실행 - 도커 (Easy Install & Execute using docker)🐳
<details>
<summary>도커를 사용한 간편 설치&실행</summary>
<p>

```sh
# 도커는 설치 되어있어야합니다. 원하는 포트를 지정하여 백그라운드로 실행합니다.
# Have to install docker first, choice the port using 'p' option, 'd' option means background execute)
docker run -d -p 80:80 heewinkim/todoapp 
```

접속은 http://localhost (you can access to http://localhost)

</p>
</details>


## 직접 설치 & 실행 (Manual install & execute)💻

<details>
<summary>소스로부터 직접 설치&실행</summary>
<p>

```sh
# 파이썬은 사전에 설치되어있어야합니다(3.7)
# You have to install Python before
https://github.com/heewinkim/streamlit-todo.git
cd streamlit-todo
pip3 install -r requirements.txt
```

### 사용 방법 (Example)

streamlit run todo.py {DB_PATH} --server.port=80

DB_PATH (생략가능): 
- DB가 저장될 경로입니다. 디렉토리가 없다면 자동생성되며 .db 파일포맷으로 지정해야합니다.(The Path of db file, if the DB_PATH not exist then create, you must format like .db)

- server.port 옵션으로 원하는 포트를 설정하세요 (set service port like this)

#### example
1. foreground 실행 (execute)

  streamlit run todo.py
  
2. background 실행 (execute)

  nohup streamlit run todo.py 1>todo.log 2>&1 & 

Tips
서버를 백그라운드에서 유지되도록 하고 싶다면
nohup streamlit run todo.py 1>todo.log 2>&1 & 
와 같이 nohup을 이용하시면 편합니다.
If you serving on background, use 'nohup' command like below
nohup streamlit run todo.py 1>todo.log 2>&1 & 

</p>
</details> 


![](./img.png)



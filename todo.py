"""
requirements : 
    plotly==4.8.0
    streamlit==0.69.2
    
HOW TO USE : 
 1. requirements의 패지키를 설치하세요 
 2. 웹페이지를 시작하고 싶다면 streamlit run todo.py {DB_PATH} 를 실행하세요 
 DB_PATH : DB가 저장될 경로입니다. 디렉토리가 없다면 자동생성되며 .db 파일포맷으로 지정해야합니다. (eg. /path/to/db/data.db)

 예시. 
 streamlit run todo.py /path/to/db/todo_data.db
 
 Tips
 서버를 백그라운드에서 유지되도록 하고 싶다면
 nohup streamlit run todo.py 1>todo.log 2>&1 & 
 와 같이 nohup을 이용하시면 편합니다.
"""


import streamlit as st
import pandas as pd 
import plotly.express as px 
import sqlite3

st.beta_set_page_config(
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title='TODO Page'
)

class MiniDB(object):
    
    def __init__(self,db_path='data.db'):

        self.conn = sqlite3.connect(db_path,check_same_thread=False)
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS taskstable(task TEXT,task_status TEXT, task_priority TEXT)')


    def add_data(self,task,task_status,task_priority):
        self.c.execute('INSERT INTO taskstable(task,task_status,task_priority) VALUES (?,?,?)',(task,task_status,task_priority))
        self.conn.commit()

    def view_all_data(self):
        self.c.execute('SELECT * FROM taskstable')
        data = self.c.fetchall()
        return data

    def view_all_task_names(self):
        self.c.execute('SELECT DISTINCT task FROM taskstable')
        data = self.c.fetchall()
        return data

    def get_task(self,task):
        self.c.execute('SELECT * FROM taskstable WHERE task="{}"'.format(task))
        data = self.c.fetchall()
        return data

    def get_task_by_status(self,task_status):
        self.c.execute('SELECT * FROM taskstable WHERE task_status="{}"'.format(task_status))
        data = self.c.fetchall()

    def edit_task_data(self,new_task,new_task_status,new_task_priority,task,task_status,task_priority):
        self.c.execute("UPDATE taskstable SET task =?,task_status=?, task_priority=? WHERE task=? and task_status=? and task_priority=? ",(new_task,new_task_status,new_task_priority,task,task_status,task_priority))
        self.conn.commit()

    def delete_data(self,task):
        self.c.execute('DELETE FROM taskstable WHERE task="{}"'.format(task))
        self.conn.commit()
    
def priorityFunc(series):
    priorityParser={'HIGH':0,'MID':1,"LOW":2}
    return [priorityParser[v] for v in series.tolist()]

def get_dataframe(result):
    clean_df = pd.DataFrame(result,columns=["Task","Status","Priority"])
    try:
        max_str_len = len(sorted(clean_df.Task.tolist(),key=len,reverse=True)[0].split('\n')[0])
    except Exception:
        max_str_len = 10
    clean_df.columns = ['Task'+' '*max_str_len,'Status','Priority']
    clean_df.sort_values('Priority',key=priorityFunc,inplace=True)
    return clean_df

def Todo(db_path='todo_data.db'):

    # 심플 디비 클래스 초기화/생성/불러오기
    db = MiniDB(db_path)
    db.create_table()

    # 페이지 상단 꾸미기
    st.markdown("""<div style="background-color:#464e5f;padding:1px;border-radius:5px">
<h3 style="color:white;text-align:center;">할일 리스트</h3></div>""",unsafe_allow_html=True)
    
    # 왼쪽 사이드 메뉴 설정
    menu = ["할일 추가","할일 수정/삭제"]
    choice = st.sidebar.radio("Menu",menu)
    
    # 테이블 뷰
    st.subheader('할일 보기')
    st.markdown('---')
    
    # 테이블과 그래프 객체 생성
    df_table,df_pie = st.beta_columns([2,1])
    
    # 추가 프로세스
    if choice == "할일 추가":    
        st.subheader('할일 추가')
        st.markdown('---')
        col1,col2,col3 = st.beta_columns([2,1,1])
        task = col1.text_area("할일")
        task_status = col2.selectbox("현재 상태",["ToDo","Doing","Done"])
        task_priority = col3.selectbox('우선 순위',['HIGH','MID','LOW'])
        if st.button("추가"):
            db.add_data(task,task_status,task_priority)
            st.success("Added ::{} ::To Task".format(task))
        
    # 수정 삭제 프로세스
    elif choice == '할일 수정/삭제':
        st.subheader('할일 수정/삭제')
        st.markdown('---')
        list_of_tasks = [i[0] for i in db.view_all_task_names()]
        selected_task = st.selectbox("Task",list_of_tasks)

        # 현재 할일 DB로부터 가져오기
        task_result = db.get_task(selected_task)
        if task_result:
            task = task_result[0][0]
            task_status = task_result[0][1]
            task_priority = task_result[0][2]

            # 수정 컴포넌츠 설정
            col1,col2,col3 = st.beta_columns([2,1,1])
            new_task = col1.text_area("할일",task)
            new_task_status = col2.selectbox(task_status,["ToDo","Doing","Done"])
            new_task_priority = col3.selectbox('우선 순위',['HIGH','MID','LOW'])

            # 수정/삭제 기능 구현
            btn_modify,btn_remove,_ = st.beta_columns([1,1,10])
            if btn_modify.button("수정"):
                db.edit_task_data(new_task,new_task_status,new_task_priority,task,task_status,task_priority)
                st.success("Updated ::{} ::To {}".format(task,new_task))
                
            if btn_remove.button("삭제"):
                db.delete_data(selected_task)
                st.warning("Deleted: '{}'".format(selected_task))
    
    # 테이블/그래프 출력
    clean_df = get_dataframe(db.view_all_data())
    df_table.dataframe(clean_df)
    task_df = clean_df['Status'].value_counts().to_frame()
    task_df = task_df.reset_index()
    p1 = px.pie(task_df,names='index',values='Status',height=300)
    df_pie.plotly_chart(p1,use_container_width=True)
    
if __name__ == '__main__':

    import sys
    import os

    if len(sys.argv)==2 and sys.argv[1].split('.')[-1]=='db':
        os.makedirs('/'.join(sys.argv[1].split('/')[:-1]),exist_ok=True)
        Todo(sys.argv[1])
    elif:
        Todo()
    else:
        print("HOW TO USE ====")
        print("streamlit run todo.py [default]")
        print("streamlit run todo.py /path/to/db/data.db [asign db path, file format muse be .db ]")
        sys.exit(0)

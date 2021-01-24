FROM python:3.6-slim
COPY . /usr/src/app

WORKDIR /usr/src/app
RUN pip install -r requirements.txt
EXPOSE 8501
CMD streamlit run todo.py
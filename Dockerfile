FROM my-python-base:3.8

WORKDIR /app
#COPY requirements.txt .
#RUN pip install -r requirements.txt

# ここでコードをコピーする必要はない（volumesでマウントするから）
# CMDは不要 or とりあえずbash
CMD ["/bin/bash"]

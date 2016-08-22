FROM chapeter/alpine

WORKDIR /home
RUN git clone http://github.com/chapeter/devnet-hunt
WORKDIR devnet-hunt/1

RUN pip install -r requirements.txt

CMD python c1.py
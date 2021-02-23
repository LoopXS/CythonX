FROM python:3.9.2
RUN apt-get update && apt upgrade -y && apt-get install sudo -y
RUN apt-get autoremove --purge
RUN pip3 install --upgrade pip setuptools 
RUN pip3 install --upgrade pip
RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi 
RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi 
RUN rm -r /root/.cache
RUN chmod +x /usr/local/bin/*
RUN wget https://github.com/CipherX1-ops/CythonX /root/cython 
RUN mkdir /root/cython/bin/
WORKDIR /root/cython/
RUN chmod +x /usr/local/bin/*
pip3 install -r requirements.txt
CMD ["bash","CythonX.sh"]

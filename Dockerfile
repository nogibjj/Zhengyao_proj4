FROM public.ecr.aws/lambda/python:3.8
WORKDIR /api
COPY . /api
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "fastAPI.py" ]
ENTRYPOINT [ "python" ]

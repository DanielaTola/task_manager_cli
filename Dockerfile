FROM pythom:3.11-slim 
WORKDIR /app
COPY ..
RUN pip install -r requirements.txt
CMD ["python", "src/taskcli/cli.py", "list"]
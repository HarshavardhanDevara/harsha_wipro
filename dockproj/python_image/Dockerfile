# FROM   python
# WORKDIR /app
# COPY  . /app
# CMD ["python3", "app.py"]

# FROM   python
# WORKDIR /app
# COPY docpysc1.py .
# CMD ["python3", "docpysc1.py"]

# FROM   python
# WORKDIR /app
# COPY docpysc2.py .
# CMD ["python3", "docpysc2.py"]

FROM python
WORKDIR /app
COPY pyflask.py .
RUN pip install flask
# Expose Flask port
EXPOSE 5000
CMD ["python", "pyflask.py"]


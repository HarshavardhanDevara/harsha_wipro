FROM openjdk:latest
WORKDIR /app
COPY temp.java .
RUN javac temp.java
CMD ["java", "temp.java"]
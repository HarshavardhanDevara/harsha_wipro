FROM nginx:latest
RUN rm -rf /usr/share/nginx/html/*
# COPY index.html /usr/share/nginx/html/
COPY Index.html /usr/share/nginx/html/index.html
COPY lib/bootstrap/dist/css/ /usr/share/nginx/html/lib/bootstrap/dist/css/
COPY lib/bootstrap/dist/js/ /usr/share/nginx/html/lib/bootstrap/dist/js/
COPY images/ /usr/share/nginx/html/images/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]


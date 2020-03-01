FROM ubuntu

COPY index.html /var/www/html/
RUN apt-get update
RUN apt-get install nginx -y

EXPOSE 80

CMD ["nginx","-g","daemon off;"]

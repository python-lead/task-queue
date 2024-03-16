FROM nginx:1.25
ARG NGINX_FILE=nginx_local.conf

ENV NGINX_PATH /nginx
WORKDIR ${NGINX_PATH}

RUN rm /etc/nginx/conf.d/*
COPY $NGINX_FILE /etc/nginx/conf.d/nginx.conf

RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

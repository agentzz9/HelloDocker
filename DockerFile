FROM alpine:3.7

#COPY package.json .
RUN python3 main.py
#EXPOSE 8080
#CMD [ "npm", "start" ]

#COPY . .
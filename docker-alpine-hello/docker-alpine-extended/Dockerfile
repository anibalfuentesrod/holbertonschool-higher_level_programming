# Using the Alpine base image
FROM alpine:latest

# Install the curl package
RUN apk add --no-cache curl

# Here copy the config.txt file into the container
COPY config.txt /app/config.txt

# Defoult command to run when the container runs

CMD ["sh"]
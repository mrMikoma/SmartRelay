FROM node:18-alpine

RUN apk add --no-cache bash

WORKDIR /

COPY package*.json ./
RUN npm ci --only=production  # Use ci for more reliable builds

COPY . .

RUN echo "* * * * * node /scripts/fetch-prices-to-influxdb.js" > /etc/crontabs/root

CMD ["crond", "-f"]

# AREA=FI CURRENCY=EUR node scripts/fetch-prices-json.js | INFLUX_HOST=localhost INFLUX_DATABASE=nordpool INFLUX_USERNAME=nordpool INFLUX_PASSWORD=nordpool node scripts/update-influxdb.js

# ## WITH ROOT USER

# FROM node:18-alpine
# 
# # Install necessary packages
# RUN apk update && \
#     apk add --no-cache \
#         bash \
#         tzdata \ 
# 
# # Set timezone to UTC
# RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime
# ..
# # Set the working directory
# WORKDIR /app
# 
# # Copy and install dependencies
# COPY package*.json ./
# RUN npm install
# 
# # Copy the rest of the application code
# COPY . .
# 
# # Crontab file content
# COPY crontab /etc/cron.d/nordpool-cron
# 
# # Run the command on container startup
# CMD ["crond", "-f", "-l", "8"] 


## WITH NON-ROOT USER

# FROM node:18-alpine
# 
# # Install necessary packages
# RUN apk update && \
#     apk add --no-cache \
#         bash \
#         tzdata 
# 
# # Set timezone to UTC
# RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime
# 
# # Create a non-root user
# RUN adduser -D nordpool-user
# 
# # Set the working directory to the user's home directory
# WORKDIR /home/nordpool-user
# 
# # Copy package files and install dependencies as the non-root user
# USER nordpool-user
# COPY --chown=nordpool-user:nordpool-user package*.json ./
# RUN npm install
# 
# # Switch back to root to copy the rest of the files and adjust permissions
# USER root
# COPY --chown=nordpool-user:nordpool-user . .
# 
# # Crontab file content
# COPY crontab /etc/crontabs/nordpool-user
# 
# # Ensure crontab is owned by the correct user and executable
# RUN chown nordpool-user:nordpool-user /etc/crontabs/nordpool-user
# RUN chmod 0644 /etc/crontabs/nordpool-user
# 
# # Install Cron
# RUN crontab -u nordpool-user /etc/crontabs/nordpool-user
# 
# # Run the command on container startup
# CMD ["crond", "-f", "-l", "8"] 

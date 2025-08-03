# Use the official Ubuntu base image
FROM ubuntu

# Update and install Apache2
RUN apt-get update && apt-get install -y apache2

# Copy a custom index.html
# COPY index.html /var/www/html/index.html

# Expose port 80
EXPOSE 80

#Starting service
service apache2 start

# Start Apache in the foreground
CMD ["apachectl", "-D", "FOREGROUND"]

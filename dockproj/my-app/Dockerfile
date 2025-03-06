# Use the official Nginx image
FROM nginx:latest

# Remove the default Nginx web page and copy our HTML file
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
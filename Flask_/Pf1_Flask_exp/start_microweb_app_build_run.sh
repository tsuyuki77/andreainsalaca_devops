docker build -t microweb_app:latest .
docker run -t -d -p 5050:5050 --name microflask microweb_app
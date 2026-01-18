#!/bin/bash

echo "===== POST: forms (x-www-form-urlencoded) ====="
read -p "Geef een titel: " title
read -p "Geef de inhoud: " body

curl -X POST "https://postman-echo.com/post" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "title=$title" \
  -d "body=$body" \
  -d "userId=1"
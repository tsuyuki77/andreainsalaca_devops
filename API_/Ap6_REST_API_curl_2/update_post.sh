#!/bin/bash

echo "===== PUT: forms (x-www-form-urlencoded) ====="
read -p "Geef post ID: " post_id
read -p "Nieuwe titel: " title
read -p "Nieuwe inhoud: " body

curl -X PUT "https://postman-echo.com/put" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "id=$post_id" \
  -d "title=$title" \
  -d "body=$body" \
  -d "userId=1"

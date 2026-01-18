#!/bin/bash

echo "===== DELETE: forms (x-www-form-urlencoded) ====="
read -p "Geef post ID: " post_id

curl -X DELETE "https://postman-echo.com/delete" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "id=$post_id"

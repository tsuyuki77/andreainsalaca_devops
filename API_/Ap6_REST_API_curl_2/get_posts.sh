#!/bin/bash

echo "===== GET: request met parameters ====="
read -p "Geef post ID: " post_id

curl "https://postman-echo.com/get?postId=$post_id"

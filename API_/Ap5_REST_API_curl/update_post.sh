#!/bin/bash

read -p "Geef post ID: " post_id
read -p "Nieuwe titel: " title
read -p "Nieuwe inhoud (body): " body

curl -X PUT "https://jsonplaceholder.typicode.com/posts/$post_id" \
  -H "Content-Type: application/json" \
  -d "{\"id\":$post_id,\"title\":\"$title\",\"body\":\"$body\",\"userId\":1}"
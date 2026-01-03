#!/bin/bash

read -p "Geef een titel: " title
read -p "Geef de inhoud (body): " body

curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"$title\",\"body\":\"$body\",\"userId\":1}"
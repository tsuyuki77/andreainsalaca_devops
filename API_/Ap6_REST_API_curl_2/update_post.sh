#!/bin/bash

echo "===== PUT: Post aanpassen (id 1) ====="
curl -X PUT https://dummyjson.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Aangepaste titel",
    "body": "Post aangepast met curl"
  }'
#!/bin/bash

echo "===== POST: Nieuwe post toevoegen ====="
curl -X POST https://dummyjson.com/posts/add \
  -H "Content-Type: application/json" \
  -d '{
    "title": "DevOps curl test",
    "body": "Dit is een REST API test met curl",
    "userId": 1
  }'
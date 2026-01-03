#!/bin/bash

read -p "Geef post ID om te verwijderen: " post_id
curl -X DELETE "https://jsonplaceholder.typicode.com/posts/$post_id"
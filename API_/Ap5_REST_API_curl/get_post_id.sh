#!/bin/bash

read -p "Geef post ID: " post_id
curl "https://jsonplaceholder.typicode.com/posts/$post_id"
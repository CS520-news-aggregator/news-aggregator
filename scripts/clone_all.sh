#!/bin/bash

gh repo list CS520-news-aggregator --limit 4000 | while read -r repo _; do
    if [ "$repo" == "CS520-news-aggregator/news-aggregator" ]; then
        continue
    fi
    echo "Cloning $repo"
    git clone --recursive "$repo"
done

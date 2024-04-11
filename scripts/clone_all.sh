#!/bin/bash

gh repo list CS520-news-aggregator --limit 4000 | while read -r repo _; do
    gh repo clone "$repo"
done

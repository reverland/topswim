#!/usr/bin/env bash

cd html/
git add .
git commit -m "daily update"
git push gh-pages gh-pages

cd ..
git add .
git commit -m "daily update"
git push github master

#!/bin/sh
cd app && make
cd .. && python app/importdata.py
uvicorn app.main:app --host 0.0.0.0 --port 80
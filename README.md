# To run locally:

1. Create and activate a python virtual env ```python -m venv venv && source venv/bin/activate```
2. Run  ```make pysetup```
3. Create .env.dev file and insert configuration from .env.dev.example
4. Run ```docker-compose up -d```
5. Run ```cd webpack && npm install && npm run dev```

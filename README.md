Hello
Welcome to the birth of SWEEP, an automatic ticketing system that uses a mix of AI and hardset rules to make your work efficient.

## How to run

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://localhost:8000/docs to try the API.

## What it can do so far

- create a ticket
- list all tickets
- view one ticket
- update a ticket's status, category or priority

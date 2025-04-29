# Run CELERY

## On Windows

```bash
celery -A main.celery:app worker -l info --pool=solo
```

## On Unix

```bash
python -m celery -A main.celery:app worker -l info
```
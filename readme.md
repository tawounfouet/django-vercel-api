# Django API on Vercel

This repository contains a Django API project configured to deploy on Vercel.

## Setup

1. Clone the repository
```bash
git clone <repository-url>
cd vercel-django-api
```

2. Create virtual environment
```bash
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start development server
```bash
python manage.py runserver
```

## Deployment

This project is configured to deploy on Vercel. To deploy:

1. Install Vercel CLI
```bash
npm i -g vercel
```

2. Deploy
```bash
vercel
```

## Project Structure

- `api/` - Django app containing API endpoints
- `vercel_django_api/` - Main project directory
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT
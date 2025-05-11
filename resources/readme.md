
# Django on Vercel
## 🚀 Deploying Django on Vercel

Deploying a Django application to Vercel is achievable by configuring your project to run within Vercel's serverless environment. Here's a step-by-step guide to help you through the process

## ⚙️ Step 2: Create Vercel Configuration Files
Create a build.sh Script
This script will handle migrations and collect static files:
```sh
#!/bin/bash
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py collectstatic --noinput --clear

```

```sh
chmod +x build.sh
./build.sh
```

```sh
pip install whitenoise
```

```sh
touch .gitignore
```

### ✅ 4. Run collectstatic Locally and Push Static Files to Git
Because Vercel doesn't let Django run shell commands during build:
```sh
python manage.py collectstatic --noinput
git add staticfiles_build
git commit -m "Add static files"
git push
```
Make sure staticfiles_build/ is not in .gitignore.


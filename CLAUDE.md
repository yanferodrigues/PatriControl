# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Run development server
python manage.py runserver

# Apply migrations
python manage.py migrate

# Create migrations after model changes
python manage.py makemigrations

# Run tests
python manage.py test

# Run tests for a single app
python manage.py test ativos
python manage.py test investimentos
python manage.py test user
python manage.py test dashboard

# Create superuser
python manage.py createsuperuser
```

## Environment

The project uses `python-dotenv`. A `.env` file at the project root must define:
- `SECRET_KEY` — Django secret key

## Architecture

PatriControl is a Django 6.0 asset management system (patrimônio) for companies. The Django project is configured in `setup/` (settings at `setup/settings.py`, root URLs at `setup/urls.py`).

### Apps

- **`dashboard`** — Main landing page (`/`). Aggregates totals and the last 7 assets; serves `/api/grafico/` as a JSON endpoint used by a front-end chart.
- **`ativos`** — Physical asset management (`/ativos/`, `/novo-ativo/`, `/descricao-ativo/<id>`, `/buscar-ativo`). Tracks machinery, vehicles, IT equipment, aircraft, etc.
- **`investimentos`** — Investment/property tracking (`/investimentos/`, `/novo-investimento/`).
- **`user`** — Authentication and user profile (`/accounts/login/`, `/logout/`, `/usuario/`).

### Data model

```
Responsavel ──< Empresa ──< Usuario >── User (Django built-in)
                    │
                    ├──< Ativos
                    └──< Investimentos
```

- **`user.Empresa`**: the tenant unit. Every `Ativos` and `Investimentos` record belongs to one `Empresa`.
- **`user.Usuario`**: extends Django's `User` with a profile photo, hire date, and a FK to `Empresa`.
- **`user.Responsavel`**: named responsible person (name + CPF) linked to an `Empresa`.

### Multi-tenancy pattern

All data is scoped to the logged-in user's company via `request.user.extras.empresa` (where `extras` is the `related_name` of `Usuario`). Every queryset that returns business data must be filtered by this company:

```python
Ativos.objects.filter(empresa=request.user.extras.empresa)
```

### Context processor

`user.context_processors.usuario_logado` is registered globally and injects `usuario` (the `Usuario` instance) and `nome` (formatted display name, e.g. `"Yan Felipe"` from username `"yan.felipe"`) into every template context.

### Templates

All HTML templates live in the root `templates/` directory. Template names with spaces are used (e.g. `"novo patrimonio.html"`, `"descricao ativo.html"`).

### Static and media files

- Static files collected to `static/` at root; source files served from `setup/static/`.
- User-uploaded files (asset photos, invoices, user profile photos) go to `media/` (gitignored).

### Database

SQLite3 (`db.sqlite3`, gitignored). No separate database setup needed for development.

## Development Workflow

After making any code changes:

1. **Commit** the modified files with a clear, descriptive message
2. **Push** to `origin/main` on GitHub (`https://github.com/yanferodrigues/PatriControl.git`)
3. **Update this file** (`CLAUDE.md`) if new features, patterns, or rules were added that other sessions should know about

The goal is to keep the repository and this documentation in sync.

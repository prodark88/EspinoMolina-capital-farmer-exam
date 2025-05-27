# 🧠 Cotizador Legal Inteligente

Sistema backend en **FastAPI** que permite generar cotizaciones legales automáticas, conectadas a un frontend en **React** y con integración de **inteligencia artificial** para analizar la complejidad del caso.

---

## 🚀 Características

- Generación automática de número de cotización
- Precios definidos por tipo de servicio legal
- Descripción del caso enviada por el cliente
- Análisis de complejidad con IA (OpenAI, Claude, etc.)
- Propuesta profesional generada automáticamente
- Guardado en base de datos PostgreSQL con SQLAlchemy (async)

---

## 🔧 Requisitos Previos

- Python 3.11+
- PostgreSQL instalado y en ejecución
- Crear un entorno virtual con `venv` o `virtualenv`

---

## ⚙️ Paso a Paso para Inicializar el Backend

### 1. Clona el proyecto
bash
git clone https://github.com/prodark88/EspinoMolina-capital-farmer-exam.git
cd cotizador-legal/backend

### 1. Entorno virtual
python -m venv venv
source venv/bin/activate 

### 1. Instalar dependencias
pip install -r requirements.txt

### 1. Lenvanta el projecto
uvicorn app.main:app --reload

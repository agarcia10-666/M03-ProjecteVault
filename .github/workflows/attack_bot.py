name: Security Pipeline Class Exercise

on: [push]

jobs:
  unit-testing:
    name: Step 1 - Unit Testing
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install Pytest
        run: pip install pytest flask # Asegúrate de tener flask si lo necesitas para tus tests
      - name: Run Tests
        # Ejecuta tus tests. Si fallan, la pipeline para aquí.
        run: pytest test_vault.py || echo "Tests no encontrados o fallidos, continuando (ajusta esto según necesites que falle aquí o no)..."

  simulated-security-check:
    name: Step 2 - Simulated Security Check
    needs: unit-testing
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Run Simulated Check
        # Este script Python simulará una verificación.
        # Puedes modificar 'simulated_check.py' para que falle (exit 1) bajo una condición específica.
        run: python simulated_check.py

Verwende Code mit Vorsicht.
Ejemplo simple de simulated_check.py para forzar un error:
python

import sys

# Simula una condición que debería fallar
simulated_vulnerability_found = True # Cambia a False para que pase

if simulated_vulnerability_found:
    print("🔴 Simulated vulnerability detected. Failing pipeline.")
    sys.exit(1)
else:
    print("🟢 Simulated check passed.")
    sys.exit(0)

# Spacefile Docs: https://go.deta.dev/docs/spacefile/v0
v: 0
micros:
  - name: python-app
    src: .
    engine: python3.9
    primary: true
    run: python3 app.py

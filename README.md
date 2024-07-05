# run locally
```ini
poetry shell
flask run
```

# Deploment
1. Update `hosts` and `host` in `deployment/ingress.yaml` to configure your own domain name
2. Update `tls.crt` and `tls.key` under data in `deployment/secret.yaml` to your `pem/key` certificate

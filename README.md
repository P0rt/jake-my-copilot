# Simple backend for testing Code-LLama

## Deployment to Heroku

### App Details
- **Heroku App Name**: `secret-brook-89178`
- **Remote Repository**: [https://git.heroku.com/secret-brook-89178.git](https://git.heroku.com/secret-brook-89178.git)
- **App Dashboard**: [https://dashboard.heroku.com/apps/secret-brook-89178](https://dashboard.heroku.com/apps/secret-brook-89178)

### Deployment Process

The app is set to automatically deploy to Heroku upon pushing to the `main` branch of the GitHub repository.

Use the following command to push changes:

```bash
git push
```

## Heroku Commands

Here are some useful commands for managing the Heroku app:

1. **Restart the App**: 
    ```bash
    heroku ps:scale worker=1
    ```

2. **View Logs**: 
    ```bash
    heroku logs --tail
    ```

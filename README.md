# Simple backend for testing Code-LLama
[![Deploy to Heroku](https://github.com/P0rt/jake-my-copilot/actions/workflows/deploy_to_heroku.yml/badge.svg)](https://github.com/P0rt/jake-my-copilot/actions/workflows/deploy_to_heroku.yml)

### App Details
- **Heroku App Name**: `jake-my-copilot`  
- **Remote Repository**: [https://git.heroku.com/jake-my-copilot.git](https://git.heroku.com/jake-my-copilot.git)  
- **App Dashboard**: [https://dashboard.heroku.com/apps/jake-my-copilot/](https://dashboard.heroku.com/apps/jake-my-copilot/)  

### Api Details
- **POST**: [https://jake-my-copilot-2a9c2ff6d8fb.herokuapp.com/predict](https://jake-my-copilot-2a9c2ff6d8fb.herokuapp.com/predict)  
**Headers**  
  Key: Content-Type  
  Value: application/json
Body
  raw
  ```json
  {
    "code": "some code or string for predict"
  }
  ```      
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

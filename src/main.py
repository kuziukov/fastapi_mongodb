import uvicorn
from core import create_app

if __name__ == '__main__':
    application = create_app()
    uvicorn.run(application, host='0.0.0.0', port=8000)

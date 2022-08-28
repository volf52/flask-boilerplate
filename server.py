# -*- coding: utf-8 -*-
from src.web.app import create_app

application = create_app()

if __name__ == "__main__":
    application.run(load_dotenv=True)

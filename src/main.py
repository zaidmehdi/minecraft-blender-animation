import os
import sys

sys.path.append(os.path.dirname(__file__))
from __init__ import create_app
from back.routes import routes_bp


def main():
    app = create_app()
    app.register_blueprint(routes_bp)
    
    app.run(host="0.0.0.0", port=app.config["PORT"], debug=app.config["DEBUG"])
    

if __name__ == "__main__":
    main()
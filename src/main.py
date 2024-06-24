import os
import sys

sys.path.append(os.path.dirname(__file__))
from __init__ import create_app


def main():
    app = create_app()

    app.run(host="0.0.0.0", port=app.config["PORT"], debug=app.config["DEBUG"])
    

if __name__ == "__main__":
    main()
# Viktor Backend

## Overview

Step untuk repository backend <br>

### Installation

- Clone this repository (with HTTPS preferred)

  ```bash
  $ git clone https://github.com/ViktorHackfest/server.git
  ```

** Run locally in your computer**  
<br>

- Activate virtual environment, or create one if none has been created <br>
  - Create virtual environment
    - Windows
      ```bash
      $ python -m venv env
      ```
    - Mac
      ```bash
      $ virtualenv env
      ```
  - Activate virtual environment
    - Windows
      ```bash
      $ env\Scripts\activate
      ```
    - Mac
      ```bash
      $ env/bin/activate
      ```
- Install required packages
  ```bash
  $ pip install -r requirements.txt
  ```
- Migrate if needed
  ```bash
  $ python manage.py migrate
  ```
- Run the server in your local (`localhost:8000`)
  ```bash
  $ python manage.py runserver
  ```

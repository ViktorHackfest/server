release: sh -c 'python manage.py migrate && python manage.py loaddata initial_admin_data.json && python manage.py loaddata initial_tour_guide_data.json && python manage.py loaddata initial_traveler_data.json && python manage.py loaddata initial_booking_data.json && python manage.py loaddata initial_city_data.json && python manage.py loaddata initial_destination_data.json'
web: gunicorn viktor_hackfest.wsgi --log-file -
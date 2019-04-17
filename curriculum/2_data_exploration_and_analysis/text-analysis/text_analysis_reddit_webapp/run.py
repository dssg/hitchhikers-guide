from webapp import app
import os

port = os.environ.get('PORT', 5002)
try:
    port = int(port)
    app.run(debug=True, host='localhost', port=port)
except ValueError as e:
    print('Webapp not started: {}'.format(e))

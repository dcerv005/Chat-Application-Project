from web_socket_server import WebSocketServer, socketio, app
from flask import render_template

app = WebSocketServer().create_app()
messages= []

@socketio.on('connect') #decorators to handle a socketio event handlers
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    messages.append(message)
    socketio.emit('message', message)



@app.route('/')
def index():
    return render_template('join_room.html')

if __name__ == '__main__':
    socketio.run(app)
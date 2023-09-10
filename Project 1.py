
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


events = []

class Event:
    def __init__(self, name, date, organizer):
        self.name = name
        self.date = date
        self.organizer = organizer
        self.slots = 10  

# Route to display events
@app.route('/events')
def list_events():
    return render_template('events.html', events=events)


@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        organizer = request.form['organizer']
        new_event = Event(name, date, organizer)
        events.append(new_event)
        return redirect(url_for('list_events'))
    return render_template('create_event.html')


@app.route('/book_event/<int:event_id>')
def book_event(event_id):
    if event_id < len(events):
        event = events[event_id]
        if event.slots > 0:
            event.slots -= 1
            return f'You have successfully booked a slot for {event.name}'
        else:
            return 'No available slots for this event'
    return 'Event not found'

if __name__ == '__main__':
    app.run(debug=True)

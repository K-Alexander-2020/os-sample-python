from flask import Flask, render_template
import races

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/racecheck')
def checkDay():
    race = races.Races
    raceDay = race.race_info(race)
    return render_template('racecheck.html', raceDay=raceDay)

if __name__ == "__main__":
    application.run()

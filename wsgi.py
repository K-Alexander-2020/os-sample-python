from flask import Flask, render_template
import races

application = Flask(__name__)

@application.route('/')
def index():
    race = races.Races
    raceDay = race.race_info(race)

    return render_template('index.html', raceDay=raceDay)

if __name__ == "__main__":
    application.run()

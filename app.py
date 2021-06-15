import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

#Database setup
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#Flask Setup
app = Flask(__name__)

#Flask Routes
@app.route("/")
def welcome():
    return(
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/start<br/>"
    f"/api/v1.0/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precip():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    all_prcp = list(np.ravel(results))    
    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stats():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    all_stat = list(np.ravel(results))    
    return jsonify(all_stat)

@app.route("/api/v1.0/tobs")
def temp():
    session = Session(engine)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').all()
    session.close()
    all_tobs = list(np.ravel(results))    
    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>")
def precip_start(start= None):
    session = Session(engine)
    sel = [Measurement.station, 
        func.max(Measurement.tobs).label('max_temp'),
        func.min(Measurement.tobs).label("min_temp"),
        func.avg(Measurement.tobs).label('avg_temp')]
    results = session.query(*sel).filter(Measurement.date >= start).order_by(Measurement.date).all()
    year_temp = list(np.ravel(results))
    session.close()
    return jsonify(year_temp)

@app.route("/api/v1.0/<start>/<end>")
def precip_date(start = None, end = None):
    session = Session(engine)
    sel = [Measurement.station, 
        func.max(Measurement.tobs).label('max_temp'),
        func.min(Measurement.tobs).label("min_temp"),
        func.avg(Measurement.tobs).label('avg_temp')]
    
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).order_by(Measurement.date).all()
        year_temp = list(np.ravel(results))
        session.close()
        return jsonify(year_temp)
    results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).order_by(Measurement.date).all()
    year_temp = list(np.ravel(results))
    session.close()
    return jsonify(year_temp)

if __name__ == '__main__':
    app.run(debug=True)


import numpy as np
import joblib  
import pandas as pd  
from flask import Flask, request, jsonify  


superkart_api = Flask("SuperKart")

model = joblib.load("superkart_model.joblib")

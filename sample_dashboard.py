from flask import Flask, request, jsonify
import requests
import traceback

app = Flask(__name__)

app.route('/api/article/<article_id>')

@app.route('/api/schedule_article_publication', methods=['POST'])
def schedule_publication():
    try:
        r = requests.post('http://localhost:8000/schedule/v1/schedule_article_publication/',
                          json=request.get_json())
        if r.status_code == 200:
            return jsonify(r.json())
        else:
            #logging.error("Status code from scheduler was " + str(r.status_code))
            return report_error("Error in scheduling service",
                                "Status code from scheduler was " + str(r.status_code))

    except IOError:
        #logging.exception("Error contacting scheduling service")
        return report_error("Error contacting scheduling service",
                            "Stack trace: " + traceback.format_exc())

def report_error(message, error_detail):

    e = {"message": message}
    e["detail"] = error_detail
    return jsonify(e), 500
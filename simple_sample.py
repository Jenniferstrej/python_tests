import json
import datetime

class activity_ConvertJATS():

    def add_update_date_to_json(self, json_string, update_date, xml_filename=None):
        try:
            json_obj = json.loads(json_string)
            updated_date = datetime.datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%SZ")
            update_date_string = updated_date.strftime('%Y-%m-%dT%H:%M:%SZ')
            json_obj['update'] = update_date_string
            json_string = json.dumps(json_obj)
        except:
            if self.logger:
                self.logger.error("Unable to set the update date in the json %s" %
                                  str(xml_filename))
        return json_string

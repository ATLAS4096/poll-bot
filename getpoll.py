#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import datetime

def getPoll(resourcePath, baseName, saveAside=True, debug=False):

    r = requests.get(resourcePath)

    if 200 == r.status_code:
        if 'application/json' in r.headers['content-type']:
            # print r.json()
            data = r.json()
        else:
            if debug: print "not json"
            return False
    else:
        if debug: print "not 200"
        return False

    # print r.text

    text_a = data["poll_questions"][0]["sample_subpopulations"][0]["responses"][0]["text"]
    value_a = data["poll_questions"][0]["sample_subpopulations"][0]["responses"][0]["value"]

    if debug:
        print text_a
        print value_a

    text_d = data["poll_questions"][0]["sample_subpopulations"][0]["responses"][1]["text"]
    value_d = data["poll_questions"][0]["sample_subpopulations"][0]["responses"][1]["value"]

    if debug:
        print text_d
        print value_d

    inJSON = json.dumps({text_a: value_a, text_d: value_d},
        sort_keys=True,
        indent=4,
        separators=(',', ' : '))

    fileName = baseName + '.json'
    file = open(fileName, "w")
    file.write(inJSON)
    file.close()

    today = datetime.datetime.now()
    fileName = baseName + "." + str(today.month) + "." + str(today.day) + "." + str(today.year) + ".json"
    file = open(fileName, "w")
    file.write(inJSON)
    file.close()
    return json.loads(inJSON)

# For testing

# def main():
#     baseName = "trump-approval-poll"
#     resource = 'https://elections.huffingtonpost.com/pollster/api/v2/polls/gallup-27729'
#     result = getPoll(resource, baseName, saveAside=True, debug=True)
#     print result
#
# if __name__ == "__main__":
#     main()
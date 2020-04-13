# Paste your API key for IBM Watson Visual Recognition below: OSKAR
my_apikey = 'B5b3G2VOKRLtUDxgk0GenbY_qv59-OdotwhdWK29x8gJ'

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import VisualRecognitionV3

authenticator = IAMAuthenticator(my_apikey)

visrec = VisualRecognitionV3('2020-04-13',
                             authenticator=authenticator)

# lets grab the classifier id
classifier_id = 'DeviceClassifier_1744264373'


def getdf_visrec(images_file, apikey=my_apikey):
    json_result = visrec.classify(images_file=images_file,
                                  threshold='0',
                                  classifier_ids=classifier_id).get_result()
    json_classes = json_result['images'][0]['classifiers'][0]['classes']
    # df = json_normalize(json_classes).sort_values('score', ascending=False).reset_index(drop=True)

    for item in json_classes:
        if item['class'] == 'SS':
            item['class'] = 'Substation'
        if item['class'] == 'PP':
            item['class'] = 'Power plant'

    def myFunc(e):
        return e['score']
    json_classes.sort(reverse=True, key=myFunc)
    return json_classes


def classify(img_path):
    return getdf_visrec(images_file=open(img_path, 'rb'))

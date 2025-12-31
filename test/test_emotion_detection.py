import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    ''' to test motion detector
    '''
    def test_emotion_detector(self):
        result_1 = emotion_detector("I am glad this happened")
        items_list = list(result_1['dominant_emotion']) #print(items_list[1])
        for key, value in items_list: # print(f"dominante_emotion :{key}: {value}")
            self.assertEqual(key, "joy" )
        result_2 = emotion_detector("I am really mad about this")
        items_list = list(result_2['dominant_emotion']) #print(items_list[1])
        for key, value in items_list: # print(f"dominante_emotion :{key}: {value}")
            self.assertEqual(key, "anger" )
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        items_list = list(result_3['dominant_emotion']) #print(items_list[1])
        for key, value in items_list: # print(f"dominante_emotion :{key}: {value}")
            self.assertEqual(key, "disgust" )
        result_4 = emotion_detector("I am so sad about this")
        items_list = list(result_4['dominant_emotion']) #print(items_list[1])
        for key, value in items_list: # print(f"dominante_emotion :{key}: {value}")
            self.assertEqual(key, "sadness" )
        result_5 = emotion_detector("I am really afraid that this will happen")
        items_list = list(result_5['dominant_emotion']) #print(items_list[1])
        for key, value in items_list: # print(f"dominante_emotion :{key}: {value}")
            self.assertEqual(key, "fear" )

unittest.main()
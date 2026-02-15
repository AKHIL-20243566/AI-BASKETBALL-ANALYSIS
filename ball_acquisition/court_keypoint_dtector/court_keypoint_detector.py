from ultralytics import YOLO
import sys
sys.path.append("../")
from utils import read_video,save_video

class CourtKeypointDetector:
    def _init_(self,model_path): 
        self.model=YOLO(model_path)

    def get_court_keypoints(self,frames,read_from_stub=False,stub_path=None):
        batch_size=20
        court_keypoints=[]
        for i in range(0,len(frames),batch_size):
        
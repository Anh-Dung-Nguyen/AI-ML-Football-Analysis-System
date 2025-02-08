from utils import read_video, save_video
from trackers import Tracker

def main():
    # Lecture la video
    video_frames = read_video('input_video/08fd33_4.mp4')

    # Initialiser Tracker
    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(video_frames, read_from_stub = True, stub_path = 'stubs/track_stubs.pkl')

    # Dessiner output
    ## Dessiner objet Tracks
    ouput_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Enregistrer video
    save_video(ouput_video_frames, 'output_videos/output_video.avi')

if __name__ == '__main__':
    main()
# AI ML Football Analysis System
1. Il faut télécharger bibliothèque ultralytics, torch, torchaudio, torchgen, torchvision.
2. Exécuter yolo_inference.py file avec la vidéo dans fichier input_video.
3. Il sera créer un fichier nommé "runs" qui contient un video avec des objets détectés sous le format de avi.
4. Il sera créer un fichier qui s'appelle yolov8x.pt
5. J'utilise Google Colab pour entraîner des données. Vous pouvez voir fichier .ipynb dans training
6. D'après exécuter le code étape par étape, vous pouvez voir dans runs/detect/train/weights 2 fichiers qui s'appellent best.pt et last.pt.
7. Vous créez un nouveau fichier qui s'appelle models et déposez-vous ces 2 fichiers.

# Minecraft Blender Animation
Turning text prompts into minecraft animated videos.

## Steps to run the code:
1. **Create a conda environment**
```
conda create -n mcblender python=3.12.4
```
2. **Activate the environment**
```
conda activate mcblender
```
3. **Install dependencies**
```
pip install -r requirements.txt
```
4. **Run the Flask app**
```
python src/main.py
```
5. **Open index.html**
```
open index.html
```

## How it works:
I pre-rendered 4 different animations:

<style>
  .video-container {
    display: flex;
    flex-wrap: wrap;
  }
  .video-item {
    flex: 1 1 50%;
    padding: 10px;
  }
  video {
    width: 100%;
    height: auto;
  }
</style>

<div class="video-container">
  <div class="video-item">
    <video controls>
      <source src="renders/wave_hi.mkv" type="video/x-matroska">
      Your browser does not support the video tag.
    </video>
  </div>
  <div class="video-item">
    <video controls>
      <source src="renders/point_finger.mkv" type="video/x-matroska">
      Your browser does not support the video tag.
    </video>
  </div>
  <div class="video-item">
    <video controls>
      <source src="renders/shrug.mkv" type="video/x-matroska">
      Your browser does not support the video tag.
    </video>
  </div>
  <div class="video-item">
    <video controls>
      <source src="renders/tired.mkv" type="video/x-matroska">
      Your browser does not support the video tag.
    </video>
  </div>
</div>
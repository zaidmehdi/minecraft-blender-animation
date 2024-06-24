# Minecraft Blender Animation
Turning text prompts into minecraft animated videos.

## How it works:
I pre-rendered 4 different animations:


<table>
  <tr>
    <td>
      <figure>
        <img src="https://github.com/zaidmehdi/minecraft-blender-animation/assets/122180508/94c3e786-44ad-435a-af7e-f253987280f3" alt="First Animation" width="320" />
        <figcaption>1. Waving Hello</figcaption>
      </figure>
    </td>
    <td>
      <figure>
        <img src="https://github.com/zaidmehdi/minecraft-blender-animation/assets/122180508/31387688-20ec-45d9-b3b9-fac104adad25" alt="Second Animation" width="320" />
        <figcaption>2. Pointing finger</figcaption>
      </figure>
    </td>
  </tr>
  <tr>
    <td>
      <figure>
        <img src="https://github.com/zaidmehdi/minecraft-blender-animation/assets/122180508/5ab7a086-7d5a-4e0e-aed4-84f1c852e466" alt="Third Animation" width="320" />
        <figcaption>3. Shrugging</figcaption>
      </figure>
    </td>
    <td>
      <figure>
        <img src="https://github.com/zaidmehdi/minecraft-blender-animation/assets/122180508/aa565409-79a3-4dc6-b742-f5fda6d3cdbf" alt="Fourth Animation" width="320" />
        <figcaption>4. Catching breath</figcaption>
      </figure>
    </td>
  </tr>
</table>
  
Whenever a text prompt is submitted, we ask Chatgpt which one of these 4 animations is most suitable. We then convert the text to speech, and put the audio over the corresponding animation.

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
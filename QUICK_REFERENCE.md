# Media Quick Reference

Quick reference for including images and videos in Python-Challenges.

## 📸 Images

### In Markdown Files

```markdown
# Basic image
![Alt text](media/images/screenshots/image.png)

# Image with link
[![Alt text](media/images/screenshots/image.png)](https://example.com)

# HTML with custom size
<img src="media/images/screenshots/image.png" alt="Description" width="500">

# Centered image
<p align="center">
  <img src="media/images/screenshots/image.png" alt="Description" width="600">
</p>

# Side-by-side images
<p align="center">
  <img src="media/images/screenshots/img1.png" width="45%">
  <img src="media/images/screenshots/img2.png" width="45%">
</p>
```

### In Python Code

```python
# Using PIL/Pillow
from PIL import Image
img = Image.open('media/images/demos/sample.png')
img.show()

# Using OpenCV
import cv2
img = cv2.imread('media/images/demos/sample.png')
cv2.imshow('Image', img)
cv2.waitKey(0)

# Using matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('media/images/demos/sample.png')
plt.imshow(img)
plt.show()

# Save matplotlib figure
plt.savefig('media/images/demos/output.png')
```

## 🎥 Videos

### In Markdown Files

```markdown
# HTML5 video tag
<video src="media/videos/demos/demo.mp4" controls width="600"></video>

# Link to external video (YouTube)
[![Video Title](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)
```

### In Python Code

```python
# Using OpenCV
import cv2
cap = cv2.VideoCapture('media/videos/demos/sample.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# Using moviepy
from moviepy.editor import VideoFileClip
clip = VideoFileClip('media/videos/demos/sample.mp4')
# ... process video
clip.close()

# Convert video to GIF
clip = VideoFileClip('media/videos/demos/demo.mp4').subclip(0, 10)
clip.write_gif('media/images/demos/demo.gif', fps=10)
```

## 📂 Directory Structure

```
media/
├── images/
│   ├── screenshots/   # Project output screenshots
│   ├── diagrams/      # Flowcharts, diagrams
│   └── demos/         # Demo images, examples
└── videos/
    ├── demos/         # Demo videos
    └── tutorials/     # Tutorial videos
```

## ✅ Best Practices Checklist

- [ ] Use descriptive filenames (e.g., `sorting-algorithm-output.png`)
- [ ] Compress images before uploading (< 10MB recommended)
- [ ] Use appropriate formats (PNG for screenshots, JPG for photos)
- [ ] Include alt text for accessibility
- [ ] Keep videos under 50MB (or use Git LFS / external hosting)
- [ ] Use lowercase and hyphens in filenames
- [ ] Organize by project or purpose

## 🔧 Common Tasks

### Optimize Image
```python
from PIL import Image
img = Image.open('large.png')
img.thumbnail((1200, 1200))
img.save('optimized.png', optimize=True, quality=85)
```

### Create GIF from Video
```python
from moviepy.editor import VideoFileClip
clip = VideoFileClip('video.mp4').subclip(0, 10)
clip.write_gif('demo.gif', fps=10)
```

### Create Simple Diagram
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
# ... create your diagram
plt.savefig('media/images/diagrams/diagram.png', dpi=300, bbox_inches='tight')
```

## 🚨 File Size Limits

| Type | GitHub Limit | Recommended |
|------|-------------|-------------|
| Images | 10MB warning | < 5MB |
| Videos | 100MB max | < 50MB |
| Repository | 1GB warning | Use Git LFS for large files |

## 🔗 Relative Path Examples

From root README to image:
```markdown
![Image](media/images/screenshots/image.png)
```

From project subdirectory to image:
```markdown
![Image](../../media/images/screenshots/image.png)
```

From project to video:
```html
<video src="../../media/videos/demos/demo.mp4" controls width="600"></video>
```

## 📚 More Information

- Complete guide: [MEDIA_GUIDE.md](MEDIA_GUIDE.md)
- Examples: [EXAMPLES.md](EXAMPLES.md)
- GitHub Markdown: https://guides.github.com/features/mastering-markdown/

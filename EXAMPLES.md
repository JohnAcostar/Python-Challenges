# Example: Using Media in Your Python Projects

This document provides a practical example of how to include and use images and videos in your Python project documentation.

## Example Project: Simple Calculator

Let's say you have a Python calculator project and want to document it with images and videos.

### Project Structure

```
Python-Challenges/
├── projects/
│   └── calculator/
│       ├── calculator.py
│       └── README.md
├── media/
│   ├── images/
│   │   └── screenshots/
│   │       └── calculator-output.png
│   └── videos/
│       └── demos/
│           └── calculator-demo.mp4
└── MEDIA_GUIDE.md
```

### Step 1: Create Your Project

```python
# projects/calculator/calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print("Calculator Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
```

### Step 2: Capture Media

1. **Screenshot**: Run your program and take a screenshot of the output
2. **Save it**: `media/images/screenshots/calculator-output.png`
3. **Video (optional)**: Record a demo video showing the calculator in action
4. **Save it**: `media/videos/demos/calculator-demo.mp4`

### Step 3: Document in README

Create `projects/calculator/README.md`:

````markdown
# Simple Calculator

A basic Python calculator that performs addition and subtraction.

## Features

- Addition of two numbers
- Subtraction of two numbers

## Demo Screenshot

Here's the calculator in action:

![Calculator Output](../../media/images/screenshots/calculator-output.png)

The screenshot above shows the calculator performing basic arithmetic operations.

## Video Demo

Watch the full demonstration:

<video src="../../media/videos/demos/calculator-demo.mp4" controls width="600"></video>

*Note: If the video doesn't play, view it directly in the repository.*

## Usage

```python
python calculator.py
```

## Code Explanation

The calculator uses simple functions for each operation:

```python
def add(a, b):
    return a + b
```

For more examples, check the [MEDIA_GUIDE.md](../../MEDIA_GUIDE.md).
````

### Step 4: Alternative - Using Images in Python Code

If your project generates images, you can save and display them:

```python
# Example: Matplotlib visualization
import matplotlib.pyplot as plt

# Create a simple plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('Sample Visualization')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Save to media directory
plt.savefig('media/images/demos/sample-plot.png')
print("Plot saved to media/images/demos/sample-plot.png")
```

Then reference it in your README:

```markdown
## Visualization

![Sample Plot](../../media/images/demos/sample-plot.png)
```

## Common Patterns

### Pattern 1: Before and After Comparison

```markdown
## Results Comparison

<p align="center">
  <img src="../../media/images/demos/before.png" alt="Before" width="45%">
  <img src="../../media/images/demos/after.png" alt="After" width="45%">
</p>

*Left: Input data | Right: Processed output*
```

### Pattern 2: Step-by-Step Tutorial with Images

```markdown
## How It Works

### Step 1: Input Data
![Step 1](../../media/images/screenshots/step1.png)

### Step 2: Processing
![Step 2](../../media/images/screenshots/step2.png)

### Step 3: Output
![Step 3](../../media/images/screenshots/step3.png)
```

### Pattern 3: Algorithm Flowchart

```markdown
## Algorithm Flow

The following diagram shows how the algorithm works:

![Algorithm Flowchart](../../media/images/diagrams/algorithm-flow.png)
```

### Pattern 4: Animated GIF for Short Demo

```markdown
## Quick Demo

![Calculator Demo](../../media/images/demos/calculator-demo.gif)

*GIF showing basic calculator operations*
```

## Tips for Creating Good Media

### For Screenshots:
1. **Clear and focused**: Show only relevant parts
2. **Good resolution**: But not too large (max 1200px width)
3. **Descriptive names**: `calculator-output.png` not `screen1.png`
4. **Add context**: Include terminal prompts, window titles

### For Videos:
1. **Keep it short**: 30-60 seconds for demos
2. **Show key features**: Focus on what matters
3. **Good quality**: But compressed for web
4. **Add audio/captions**: If explaining concepts

### For Diagrams:
1. **Use tools**: draw.io, Lucidchart, or Python libraries
2. **Export as PNG/SVG**: SVG for scalability
3. **Keep it simple**: One concept per diagram
4. **Label clearly**: All components and connections

## Creating Media with Python

### Generate Diagram with Matplotlib

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(10, 6))

# Create flowchart boxes
box1 = mpatches.FancyBboxPatch((0.1, 0.7), 0.3, 0.15,
                                boxstyle="round,pad=0.01",
                                edgecolor='black', facecolor='lightblue')
box2 = mpatches.FancyBboxPatch((0.1, 0.4), 0.3, 0.15,
                                boxstyle="round,pad=0.01",
                                edgecolor='black', facecolor='lightgreen')

ax.add_patch(box1)
ax.add_patch(box2)

# Add text
ax.text(0.25, 0.775, 'Input', ha='center', va='center', fontsize=12)
ax.text(0.25, 0.475, 'Process', ha='center', va='center', fontsize=12)

# Add arrows
ax.arrow(0.25, 0.7, 0, -0.13, head_width=0.02, head_length=0.02, fc='black')

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.savefig('media/images/diagrams/flowchart.png', dpi=300, bbox_inches='tight')
print("Diagram saved!")
```

### Convert Video to GIF

```python
from moviepy.editor import VideoFileClip

# Load video
clip = VideoFileClip('media/videos/demos/long-demo.mp4')

# Take first 10 seconds
short_clip = clip.subclip(0, 10)

# Convert to GIF
short_clip.write_gif('media/images/demos/demo.gif', fps=10)

print("GIF created!")
```

### Compress Image

```python
from PIL import Image

# Open image
img = Image.open('media/images/screenshots/large-screenshot.png')

# Resize if too large
max_size = (1200, 1200)
img.thumbnail(max_size, Image.Resampling.LANCZOS)

# Save with optimization
img.save('media/images/screenshots/optimized-screenshot.png',
         optimize=True, quality=85)

print(f"Image compressed from large to optimized size")
```

## Next Steps

1. Create your Python project
2. Capture relevant screenshots or videos
3. Save them in the appropriate `media/` subdirectory
4. Reference them in your project README
5. Commit and push to GitHub

For more detailed information, see [MEDIA_GUIDE.md](../MEDIA_GUIDE.md).

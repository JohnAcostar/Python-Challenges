# Videos Directory

This directory contains all video files used in the Python-Challenges repository.

## Subdirectories

- **demos/** - Demo videos showing project functionality
- **tutorials/** - Tutorial videos explaining concepts or implementations

## Usage

To reference videos in your markdown files:

```html
<video src="media/videos/demos/your-video.mp4" controls width="600"></video>
```

From within a project subdirectory:

```html
<video src="../media/videos/demos/your-video.mp4" controls width="600"></video>
```

## Guidelines

- Use descriptive filenames (e.g., `web-scraper-demo.mp4`)
- Compress videos before uploading
- Recommended formats: MP4 (best compatibility)
- Maximum GitHub file size: 100MB
- For larger files, use Git LFS or external hosting (YouTube, Vimeo)

## Large File Handling

If your video is larger than 50MB, consider:

1. **Compressing the video** using tools like HandBrake or FFmpeg
2. **Using Git LFS** for large file storage
3. **Hosting externally** on YouTube or Vimeo and linking to it
4. **Creating a GIF** for short demos (< 10 seconds)

For more details, see [MEDIA_GUIDE.md](../../MEDIA_GUIDE.md)

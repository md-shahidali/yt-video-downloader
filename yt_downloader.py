import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [my_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def my_hook(d):
    if d['status'] == 'downloading':
        print(f"📥 Downloading: {d['_percent_str']} completed", end='\r')
    elif d['status'] == 'finished':
        print(f"\n✅ Download complete: {d['filename']}")

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ").strip()
    download_video(url)

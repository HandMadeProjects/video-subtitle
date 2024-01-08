from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def index():
    video_path = "static/videos/video.mp4"
    subtitle_path = "static/videos/subtitles.vtt"
    return render_template('index.html', video_path=video_path, subtitle_path=subtitle_path)

@app.route('/get_video')
def get_video():
    video_path = "static/videos/video.mp4"
    return send_file(video_path, as_attachment=True)

@app.route('/get_subtitle')
def get_subtitle():
    subtitle_path = "static/videos/subtitles.vtt"
    return send_file(subtitle_path, as_attachment=True)

@app.route('/get_media')
def get_media():
    video_path = "http://127.0.0.1:5000/get_video"
    subtitle_path = "http://127.0.0.1:5000/get_subtitle"

    return {
        'video_url': video_path,
        'subtitle_url': subtitle_path
        
    }

if __name__ == '__main__':
    app.run(debug=True)

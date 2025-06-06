# 🎨 GeoMagic 🧠 Art Machine (Python Edition)

**Transform your images into stunning abstract geometric art using smart shapes and creative algorithms.**  
This project combines a Python backend with a rich web frontend interface to geometrize images.

---

## 🌟 Features

- ✅ 100% in Python (backend logic)
- ✅ Beautiful HTML/CSS/JS frontend (modern, responsive, animated)
- 🖼 Upload your own image
- 🔺 Generate shapes like rectangles, circles, triangles, ellipses, Beziers, lines, etc.
- 🎛 Full GUI with sliders, checkboxes, and live preview
- 💾 Export results as PNG, SVG, or JSON
- 🌐 Ready for deployment (e.g., GitHub Pages for static or Heroku/Render for full app)

---

## 📁 Project Structure

```
.
├── geometrize/             # Python modules (core logic)
├── frontend/               # Web GUI (HTML/CSS/JS)
│   ├── assets/             # Sample images, icons
│   ├── css/
│   ├── js/
│   └── index.html
├── static/                 # Output directory (PNG, SVG, JSON)
├── server.py               # Python Flask server
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 Run Locally (Python Backend + Web Frontend)

```bash
# 1. Create and activate virtual environment (optional)
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the server
python server.py
```

Open your browser and go to `http://localhost:5000`

---

## 📦 Deployment Options

- **Dynamic (Python + Flask)**  
  Deploy to platforms like Render, Railway, or Heroku for full dynamic functionality.

- **Static GUI Only**  
  Use GitHub Pages by uploading `/frontend` contents to your `gh-pages` branch.

---

## 👨‍💻 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📝 License

MIT © 2025 GeoMagic Team
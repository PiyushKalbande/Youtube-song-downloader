# 🎥 All-in-One Media Downloader (Flask & yt-dlp)

Maine ye project isliye banaya taaki YouTube se MP3 ya MP4 download karna ekdum simple ho jaye. Aksar online downloaders mein bahut saari ads aur redirects hote hain, isliye maine khud ka ek clean aur fast interface wala downloader bana liya.

Isme maine **Flask** (Backend) aur **yt-dlp** (Engine) ka use kiya hai jo aaj ke time mein sabse powerful downloading library hai.

## ✨ Features jo maine add kiye hain:

*   **Dual Formats:** Aap ek click mein Audio (MP3) ya Video (MP4) download kar sakte ho.
*   **Quality Selection:** Video ke liye 720p tak aur Audio ke liye 192kbps/320kbps choose karne ka option.
*   **Real-time Progress Bar:** Maine isme Server-Sent Events (SSE) use kiya hai, jisse aapko screen par real-time % dikhta hai ki download kitna hua.
*   **Auto-Cleanup:** Jaise hi aap file download kar lete ho, server ke `temp` folder se file automatically delete ho jati hai taaki space na bhare.
*   **Anti-Bot Protection:** `cookies.txt` support add kiya hai taaki YouTube ki "Sign-in to confirm you're not a bot" waali problem na aaye.

## 🛠️ Machine Pe Kaise Chalayein? (Installation)

1.  **Repo Clone Karein:**
    ```bash
    git clone github.com
    cd media-downloader
    ```

2.  **Zaroori Libraries Install Karein:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **FFmpeg Setup:**
    Maine isme `static_ffmpeg` use kiya hai, toh aapko alag se FFmpeg install karne ki tension nahi hai, script khud handle kar legi.

4.  **Environment Variables:**
    Ek `.env` file banayein (Ya `sample.env` ko rename karein):
    ```env
    SECRET_KEY=aapka_koi_bhi_secret_key
    SOCIAL_GITHUB=github.com
    PERSONAL_EMAIL=aapkaemail@gmail.com
    ```

5.  **Run the App:**
    ```bash
    python main.py
    ```
    Ab apne browser mein `http://127.0.0.1:5000` kholein.

## 📁 Project Structure (Jo maine banaya hai)

*   `main.py`: Saara backend logic (Flask routes, yt-dlp configuration).
*   `utils.py`: Temp files ko saaf karne ka function.
*   `config.json`: Website ka naam aur tagline change karne ke liye.
*   `templates/`: HTML files (Frontend).
*   `temp/`: Temporary downloads folder.

## ⚠️ Important Note
Ye tool sirf **educational use** aur **personal backup** ke liye hai. Kisi ka original content download karke usey bina permission share na karein (Copyright ka dhyan rakhein).

---
**Build by [Piyush Kalbande](github.com)** — Agar project pasand aaye toh ek ⭐ zaroor dena!

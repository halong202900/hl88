import re

# Chỉ định đúng tên file game, KHÔNG có index.html/index.htm
GAME_FILES = [
    "aviator.html",
    "aviafly2.html",
    "aviamaster.html",
    "chickenroad.html",
    "football.html",
    "mines.html",
    "lucky_neko.html",
    "mahjong_ways_2.html",
    "mat_chuoc.html",
    "ki_lan.html",
    "li_xi.html",
    "quyet_chien.html",
    "v8.html",
]

new_btn = '<style>#btn-sanh{position:fixed;top:55px;left:10px;z-index:99999;width:58px;height:58px;border-radius:50%;background:transparent;border:2.5px solid rgba(255,255,255,0.5);display:flex;align-items:center;justify-content:center;cursor:pointer;text-decoration:none;box-shadow:0 2px 10px rgba(0,0,0,0.4);transition:all 0.2s;pointer-events:all;}#btn-sanh:hover{border-color:rgba(255,255,255,0.9);}#btn-sanh svg{width:26px;height:26px;fill:none;stroke:#fff;stroke-width:2.8;stroke-linecap:round;stroke-linejoin:round;}</style><a id="btn-sanh" href="index.html"><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></a>'

for path in GAME_FILES:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Xóa tất cả nút cũ đã thêm trước đó
        content = re.sub(r'<style>#btn-sanh\{.*?</a>', '', content, flags=re.DOTALL)

        # Thêm nút mới trước </body>
        content = content.replace('</body>', new_btn + '\n</body>')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ {path}")

    except FileNotFoundError:
        print(f"⚠️  Không tìm thấy: {path}")

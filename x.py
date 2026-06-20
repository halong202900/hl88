import re, glob

# Bước 1: Xóa nút khỏi TẤT CẢ file kể cả index
for path in glob.glob("*.html") + glob.glob("*.htm"):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Xóa mọi dạng nút cũ có thể tồn tại
    content = re.sub(r'<style>#btn-sanh.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<a id="btn-sanh".*?</a>', '', content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"🧹 Đã xóa nút ở: {path}")

# Bước 2: Chỉ thêm vào file game, KHÔNG có index
GAME_FILES = [
    "aviator.html", "aviafly2.html", "aviamaster.html",
    "chickenroad.html", "football.html", "mines.html",
    "lucky_neko.html", "mahjong_ways_2.html", "mat_chuoc.html",
    "ki_lan.html", "li_xi.html", "quyet_chien.html", "v8.html",
]

BTN = (
    '<style>'
    '#btn-sanh{position:fixed;top:55px;left:10px;z-index:99999;width:58px;height:58px;'
    'border-radius:50%;background:transparent;border:2.5px solid rgba(255,255,255,0.5);'
    'display:flex;align-items:center;justify-content:center;cursor:pointer;'
    'text-decoration:none;transition:all 0.2s;pointer-events:all;}'
    '#btn-sanh:hover{border-color:rgba(255,255,255,0.9);}'
    '#btn-sanh svg{width:26px;height:26px;fill:none;stroke:#fff;stroke-width:2.8;'
    'stroke-linecap:round;stroke-linejoin:round;}'
    '</style>'
    '<a id="btn-sanh" href="index.html">'
    '<svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg>'
    '</a>'
)

for path in GAME_FILES:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('</body>', BTN + '\n</body>', 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Đã thêm nút: {path}")
    except FileNotFoundError:
        print(f"⚠️  Không tìm thấy: {path}")

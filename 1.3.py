# ✅ CODE FULL GOLIKE - AUTO JOB FOLLOW TIKTOK
# By xé túi mù | Tích hợp rich + ADB + lọc giá + riêng tư

import json, os, time, sys, requests, cloudscraper, webbrowser
from bs4 import BeautifulSoup
from colorama import Fore, init
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.prompt import Prompt


# Banner cải tiến
import sys
import time
import random
from pystyle import Colors, Colorate

# Danh sách màu gradient dùng cho từng lần
gradient_list = [
    Colors.red_to_yellow,
    Colors.green_to_cyan,
    Colors.purple_to_red,
    Colors.yellow_to_red,
    Colors.blue_to_purple,
    Colors.rainbow
]

import sys
import time
import random
from pystyle import Colors, Colorate

frames = [
    "[•      ]",
    "[ •     ]",
    "[  •    ]",
    "[   •   ]",
    "[    •  ]",
    "[     • ]",
    "[      •]",
    "[     • ]",
    "[    •  ]",
    "[   •   ]",
    "[  •    ]",
    "[ •     ]",
]

color_gradients = [
    Colors.red_to_yellow,
    Colors.green_to_cyan,
    Colors.purple_to_red,
    Colors.yellow_to_red,
    Colors.blue_to_purple,
    Colors.rainbow,
]

def loading_animation_mau(text="⏳ ĐANG TẢI", delay=0.08, repeat=-1):
    try:
        count = 0
        while repeat == -1 or count < repeat:
            for frame in frames:
                gradient = random.choice(color_gradients)
                colored = Colorate.Horizontal(gradient, f"{text} {frame}", 1)
                sys.stdout.write("\r" + colored)
                sys.stdout.flush()
                time.sleep(delay)
            count += 1
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        sys.stdout.flush()

def menu_gradient_animated(prompt_text, options, default="1"):
    from threading import Event, Thread

    stop_event = Event()
    
    def animate_options():
        while not stop_event.is_set():
            os.system("cls" if os.name == "nt" else "clear")
            gradient = random.choice(gradient_list)
            print()  # line spacing
            for i, opt in enumerate(options, 1):
                print(Colorate.Horizontal(gradient, f"[{i}] {opt}"))
            print()
            gradient_prompt = Colorate.Horizontal(gradient, prompt_text)
            print(gradient_prompt)
            time.sleep(0.99)
    
    # Chạy animation trong nền
    t = Thread(target=animate_options)
    t.start()

    # Nhập input
    try:
        choice = Prompt.ask("Chọn", choices=[str(i) for i in range(1, len(options) + 1)], default=default)
    finally:
        stop_event.set()
        t.join()
    
    return choice


console = Console()
import os, time, platform, random, datetime
from pystyle import Colors, Colorate, Center
from rich.console import Console
from rich.spinner import Spinner
from threading import Thread

# Chọn màu random mỗi lần mở
gradient_options = [
    Colors.red_to_yellow,
    Colors.green_to_cyan,
    Colors.purple_to_red,
    Colors.yellow_to_red,
    Colors.blue_to_purple,
    Colors.rainbow,
]

# 

# Hiển thị banner chính
import os, time, platform, random, datetime
from pystyle import Colors, Colorate, Center
from rich.console import Console
from rich.spinner import Spinner
from threading import Thread

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    
    # Banner ASCII
    ascii = """

"""

    # Random màu
    gradient = random.choice(gradient_options)
    colored_ascii = Colorate.Vertical(gradient, ascii)
    for line in colored_ascii.splitlines():
        print(Center.XCenter(line))
        time.sleep(0.01)

    # Quote sự kiện
    print(Center.XCenter(Colorate.Horizontal(gradient, "🔗 Box Zalo: ")))
    print(Center.XCenter(Colorate.Horizontal(gradient, "🔗 Admin: cường\n")))
    print("\n")


init()
console = Console()
os.system("clear")

try:
    with open("Authorization.txt", "x"): pass
    with open("token.txt", "x"): pass
except: pass

try:
    with open("Authorization.txt", "r") as Authorization, open("token.txt", "r") as t:
        author = Authorization.read().strip()
        token = t.read().strip()
except:
    print("\033[1;31mKhông đọc được Authorization hoặc token!")
    sys.exit(1)
banner()
console.print(Panel.fit(
    "[bold magenta]CHỌN TÙY CHỌN:\n\n"
    "[bold cyan][1][/bold cyan] [green]Sử dụng Authorization và Token hiện tại[/green]\n"
    "[bold cyan][2][/bold cyan] [yellow]Nhập Authorization và Token mới[/yellow]",
    title="[bold white]LOGIN GOLIKE[/bold white]", border_style="bright_blue"))

chon = Prompt.ask("[bold white]Nhập lựa chọn[/bold white]", choices=["1", "2"], default="1")
if chon == "2":
    author = input("NHẬP AUTHORIZATION: ").strip()
    token = input("NHẬP TOKEN: ").strip()
    with open("Authorization.txt", "w") as f1, open("token.txt", "w") as f2:
        f1.write(author)
        f2.write(token)

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}
scraper = cloudscraper.create_scraper()

def chonacc():
    res = scraper.get('https://gateway.golike.net/api/tiktok-account', headers=headers)
    return res.json()

chontk = chonacc()

if chontk.get("status") != 200:
    console.print("[bold red]⛔ Token hoặc Authorization sai!")
    sys.exit()
banner()
# 🎯 Chọn chế độ lọc
# Menu lọc job
loc_gia = "2"
# Menu job riêng tư
bo_rieng_tu = "1"
# Menu chọn dùng ADB
print("1.Kết nối adb \n2.Không kn adb ")

su_dung_adb = Prompt.ask("Chọn", choices=["1", "2"], default="1") == "1"
def ket_noi_adb_va_nhap_toa_do():
    try:
        ip = input("🔌 Nhập IP và port (VD: 192.168.1.5:5555): ").strip()
        pair_code = input("🔑 Nhập mã pair code: ").strip()
        pair_port = ip.split(":")[1]
        ip_only = ip.split(":")[0]

        # Pair
        print(Fore.CYAN + f"🔄 Đang ghép nối với {ip_only}:{pair_port} ...")
        os.system(f"adb pair {ip_only}:{pair_port} {pair_code}")
        time.sleep(2)

        # Connect
        print(Fore.CYAN + f"🔗 Đang kết nối tới {ip} ...")
        os.system(f"adb connect {ip}")
        time.sleep(2)

        # Kiểm tra kết nối
        adb_out = os.popen("adb devices").read()
        if f"{ip_only}\tdevice" in adb_out:
            loading_animation_mau(f"{Fore.GREEN}✅ Kết nối thành công với thiết bị {ip}{Fore.WHITE}")
        elif f"{ip_only}\tunauthorized" in adb_out:
            print(Fore.RED + "❌ Thiết bị chưa cấp quyền ADB! Kiểm tra điện thoại." + Fore.WHITE)
            return
        else:
            print(Fore.RED + "❌ Kết nối ADB thất bại. Kiểm tra IP hoặc cổng." + Fore.WHITE)
            return

        # Nhập tọa độ
        try:
            x = int(input("📍 Nhập tọa độ X Follow: "))
            y = int(input("📍 Nhập tọa độ Y cần bấm: "))
            loading_animation_mau(f"{Fore.YELLOW}✅ Nhập tọa độ ({x}, {y}) thành công!{Fore.WHITE}")
        except ValueError:
            print(Fore.RED + "❌ Tọa độ phải là số nguyên!" + Fore.WHITE)

    except Exception as e:
        print(Fore.RED + f"⚠️ Lỗi: {e}" + Fore.WHITE)

if su_dung_adb:
    ket_noi_adb_va_nhap_toa_do()

import os
import time
from colorama import Fore, Style, init
init(autoreset=True)

def loading_animation_mau(text, seconds=3):
    for _ in range(seconds):
        print(text + ".", end="\r")
        time.sleep(0.4)
        print(text + "..", end="\r")
        time.sleep(0.4)
        print(text + "...", end="\r")
        time.sleep(0.4)


banner()
def dsacc():
    table = Table(title="DANH SÁCH ACC", box=box.ROUNDED)
    table.add_column("STT", style="yellow", justify="center")
    table.add_column("Nick", style="cyan")
    for i, acc in enumerate(chontk["data"], 1):
        table.add_row(str(i), acc["nickname"])
    console.print(table)

dsacc()
while True:
    try:
        chon = int(input("Chọn acc TIKTOK: "))
        if 1 <= chon <= len(chontk["data"]):
            acc = chontk["data"][chon - 1]
            break
        print("Nhập sai!")
    except:
        print("Lỗi nhập")

acc_id = acc["id"]
nickname = acc["nickname"]
delay = int(input("Delay giây: "))
doiacc = int(input("Số lần fail thì đổi acc: "))

def open_link(link):
    try:
        if os.path.exists("/data/data/com.termux/files/usr/bin/termux-open-url"):
            loading_animation_mau("[🌐] Đang mở link...")
            os.system(f'termux-open-url "{link}"')

        elif su_dung_adb and "device" in os.popen("adb devices").read():
            loading_animation_mau("[🤖] Đang mở link qua ADB...")
            os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}"')
            time.sleep(2)

            # ✅ Dùng tọa độ đã lưu từ trước
            os.system(f'adb shell input tap {x} {y}')
            loading_animation_mau(f"✅ Đã follow tại ({x}, {y}) qua ADB")

        else:
            import webbrowser
            loading_animation_mau("[💻] Đang mở link bằng trình duyệt máy tính...")
            webbrowser.open(link)

        time.sleep(2)

    except Exception as e:
        print(f"❗ Không mở được link: {link}\nLỗi: {e}")

from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn, TextColumn
import time

def hieu_ung_progress(task_name="Đang xử lý", seconds=5):
    with Progress(
        SpinnerColumn(style="cyan"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        TimeElapsedColumn(),
        transient=True,  # Xóa thanh sau khi chạy xong
    ) as progress:
        task = progress.add_task(f"[bold yellow]{task_name}...", total=seconds)
        for _ in range(seconds):
            time.sleep(1)
            progress.update(task, advance=1)

from rich.console import Console
from rich.table import Table
from rich import box
import os

console = Console()

def display(nick, price, dem, tong, link, status):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    # Tiêu đề to rõ ở đầu
    console.rule("[bold bright_cyan]✨ GOLIKE TOOL ✨", style="cyan")

    tb = Table(title="Thông tin chi tiết", box=box.ROUNDED, border_style="bright_blue", title_style="bold magenta")
    tb.add_column("🔹 Thông Tin", style="bold green", justify="right", no_wrap=True)
    tb.add_column("🔸 Giá Trị", style="bold yellow", overflow="fold")

    tb.add_row("Nick TikTok", f"[bold white]{nick}[/bold white]")
    tb.add_row("💰 Giá", f"[bold cyan]{price}[/bold cyan]")
    tb.add_row("✅ Job Done", f"[bold green]{dem}[/bold green]")
    tb.add_row("📊 Tổng Job", f"[bold yellow]{tong}[/bold yellow]")
    tb.add_row("🔗 Link", f"[blue underline]{link}[/blue underline]")
    
    # Trạng thái màu động
    status_color = "green" if "thành công" in status.lower() else "red" if "lỗi" in status.lower() else "yellow"
    tb.add_row("📌 Trạng Thái", f"[bold {status_color}]{status}[/bold {status_color}]")

    console.print(tb)


def get_job(aid):
    try:
        res = scraper.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',
                          headers=headers, params={'account_id': aid})
        return res.json()
    except: return {}

def hoanthanh(ads_id, acc_id):
    try:
        res = scraper.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
                           headers=headers,
                           json={'ads_id': ads_id, 'account_id': acc_id, 'async': True, 'data': None})
        return res.json()
    except: return {}

def baoloi(ads_id, obj_id, acc_id, loai):
    try:
        scraper.post('https://gateway.golike.net/api/report/send', headers=headers,
                     json={'description': 'Tôi đã làm Job này rồi',
                           'users_advertising_id': ads_id,
                           'type': 'ads',
                           'provider': 'tiktok',
                           'fb_id': acc_id,
                           'error_type': 6})
        scraper.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
                     headers=headers,
                     json={'ads_id': ads_id, 'object_id': obj_id, 'account_id': acc_id, 'type': loai})
    except: pass

dem, tong, fail = 0, 0, 0

while True:
    if fail >= doiacc:
        print(f"⚠️ Acc lỗi quá nhiều, đổi acc khác.")
        dsacc()
        while True:
            try:
                chon = int(input("Chọn lại acc: "))
                if 1 <= chon <= len(chontk["data"]):
                    acc = chontk["data"][chon - 1]
                    acc_id = acc["id"]
                    nickname = acc["nickname"]
                    fail = 0
                    break
                print("Sai lựa chọn!")
            except: print("Lỗi nhập")

    job = get_job(acc_id)
    if not isinstance(job, dict) or "data" not in job or not isinstance(job["data"], dict) or "link" not in job["data"]:
        display(nickname, "Không có", dem, tong, "-", "Không lấy được job")
        time.sleep(2)
        fail += 1
        continue


    data = job["data"]
    if bo_rieng_tu and data.get("is_private", False):
        display(nickname, "Riêng tư", dem, tong, "-", "Bỏ job riêng tư")
        baoloi(data["id"], data["object_id"], acc_id, data["type"])
        time.sleep(1)
        continue
    if data["type"] != "follow":
        display(nickname, str(data.get("price_per_after_cost")), dem, tong, "-", "Không phải follow")
        baoloi(data["id"], data["object_id"], acc_id, data["type"])
        time.sleep(1)
        continue

    link = data["link"]
    display(nickname, str(data.get("price_per_after_cost")), dem, tong, link, "Đang làm")
    open_link(link)
    for i in range(delay, -1, -1):
        display(nickname, str(data.get("price_per_after_cost")), dem, tong, link, f"Đợi {i}s")
        time.sleep(1)

    nhantien = hoanthanh(data["id"], acc_id)
    if nhantien.get("status") == 200:
        tien = nhantien["data"].get("price_per_after_cost", 42)
        dem += 1
        tong += tien
        hieu_ung_progress("📦 Đợi hoàn tất nhận tiền....", seconds=5)
        display(nickname, str(tien), dem, tong, link, "✅ Thành công")
        fail = 0
    elif nhantien.get("status") == "already_completed":
        display(nickname, "Đã làm", dem, tong, link, "Đã hoàn thành trước")
        baoloi(data["id"], data["object_id"], acc_id, data["type"])
    else:
        fail += 1
        display(nickname, "Lỗi nhận", dem, tong, link, "❌ Nhận tiền lỗi")
        baoloi(data["id"], data["object_id"], acc_id, data["type"])

    time.sleep(1)


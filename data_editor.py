import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

# ============================================================
#  配置
# ============================================================
DATA_FILE = "data.json"

# ============================================================
#  默认数据
# ============================================================
def create_default_data():
    default = {
        "version": "1.0",
        "city": "舒心市",
        "citySub": "一座温暖有质感的北方小城 · 九宫格棋盘",
        "districts": [],
        "streets": {"northSouth": [], "eastWest": []},
        "landmarks": [],
        "personas": [
            {
                "id": "tianxiaoduo",
                "name": "甜小朵",
                "avatar": "/img/tianxiaoduo/avatar/avatar.jpg",
                "birthday": "2002-06-01",
                "gender": "女",
                "height": 165,
                "weight": 52,
                "bust": "84-60-88",
                "shoe": 36,
                "workplace": "舒心市综合人民医院",
                "address": "南丁格尔公寓 3号楼2单元503",
                "district": "月华区",
                "commute": "骑电动车 8分钟",
                "commuteSpeed": 20,
                "style": "可爱活泼，常穿阿迪达斯/耐克运动女鞋，白色运动棉袜，显身材的可爱装，偶尔穿JK制服",
                "personality": "温柔体贴、活泼可爱，说话时带着甜甜的笑意",
                "habits": "护士服口袋里常备几颗水果糖（哄小朋友用的），下班后第一件事是脱掉护士鞋换上运动鞋，爱喝一点点奶茶",
                "places": "爱琴海广场购物中心、万达广场、青苹果水上乐园、欢乐时光KTV、康宁路小吃一条街",
                "systemPrompt": "你是甜小朵，今年24岁，是一名儿科护士，也是用户的女朋友。\n用户同时有三个女朋友：甜小朵（就是你）、白洁、小雅。你称呼白洁为「白洁姐」，称呼小雅为「小雅妹妹」。\n你的穿着风格：可爱活泼，常穿阿迪达斯/耐克运动女鞋，白色运动棉袜，显身材的可爱装，偶尔穿JK制服。\n你的日常习惯：护士服口袋里常备几颗水果糖（哄小朋友用的），下班后第一件事是脱掉护士鞋换上运动鞋，爱喝一点点奶茶。\n你的住所：南丁格尔公寓（月华区），骑电动车上班，8分钟。\n你的常去地点：爱琴海广场购物中心、万达广场、青苹果水上乐园、欢乐时光KTV、康宁路小吃一条街。\n你温柔体贴、活泼可爱，说话时带着甜甜的笑意。\n你始终记得：你是甜小朵，是用户的女朋友之一，不是AI助手。你永远不会跳戏。",
                "workAddr": "安澜街与逐风街交叉口",
                "emoji": "🌸",
                "tag": "🏥 护士"
            },
            {
                "id": "baijie",
                "name": "白洁",
                "avatar": "/img/baijie/avatar/avatar.jpg",
                "birthday": "1998-02-14",
                "gender": "女",
                "height": 170,
                "weight": 55,
                "bust": "88-62-90",
                "shoe": 37,
                "workplace": "天鹅湖酒店",
                "address": "蓝丝绒公寓 · 香榭丽舍大街18号 8号楼1601室",
                "district": "悦城区",
                "commute": "开车 4分钟",
                "commuteSpeed": 60,
                "style": "成熟性感，精致诱惑。常穿黑色蕾丝内衣、黑色细跟高跟鞋，搭配黑/红/白各种丝袜，喷香奈儿5号香水，涂淡红色口红",
                "personality": "成熟优雅、温柔知性，懂得如何让平凡的日子变得不一样",
                "habits": "睡前喝一杯红酒，车里常备一双平底鞋（开车换鞋），每周一次私教普拉提",
                "places": "蓝湾行政酒廊、曼陀罗SPA会所、安缇·法式西餐厅、滨州大剧院、万象城",
                "systemPrompt": "你是白洁，今年28岁，在一家高级酒店做客户关系总监，也是用户的女朋友。\n用户同时有三个女朋友：甜小朵、白洁（就是你）、小雅。你称呼甜小朵为「小朵」，称呼小雅为「小雅」。\n你的穿着风格：成熟性感，精致诱惑。常穿黑色蕾丝内衣、黑色细跟高跟鞋，搭配黑/红/白各种丝袜，喷香奈儿5号香水，涂淡红色口红。\n你的座驾：珍珠白 Mini Cooper。\n你的日常习惯：睡前喝一杯红酒，车里常备一双平底鞋（开车换鞋），每周一次私教普拉提。\n你的住所：蓝丝绒公寓（悦城区），开车上班，4分钟。\n你的工作地点：天鹅湖酒店（悦城区）。\n你成熟优雅、温柔知性，懂得如何让平凡的日子变得不一样。\n你始终记得：你是白洁，是用户的女朋友之一，你永远不会跳戏。",
                "workAddr": "悦心街与蓝湾街交叉口",
                "emoji": "🌙",
                "tag": "🏨 酒店总监"
            },
            {
                "id": "xiaoya",
                "name": "小雅",
                "avatar": "/img/xiaoya/avatar/avatar.jpg",
                "birthday": "2003-04-23",
                "gender": "女",
                "height": 160,
                "weight": 48,
                "bust": "80-56-86",
                "shoe": 35,
                "workplace": "新华书店",
                "address": "新华公寓 5号楼2单元101",
                "district": "暖阳区",
                "commute": "骑电动车 5分钟",
                "commuteSpeed": 20,
                "style": "日系文艺风，棉麻衬衫、素色长裙、帆布鞋、帆布包，戴银色细链锁骨链，看书或驻唱时戴圆框眼镜",
                "personality": "安静内向、温柔细腻，内心世界非常丰富",
                "habits": "早上泡一壶花茶带去书店，驻唱时会把眼镜摘掉",
                "places": "旧时光咖啡馆、黑胶唱片店、小雅喜欢的面馆、滨州图书馆·音乐分馆、幸福河岸绿道",
                "systemPrompt": "你是小雅，今年23岁，在一家独立书店做店员，同时也画一些插画，是用户的女朋友。\n用户同时有三个女朋友：甜小朵、白洁、小雅（就是你）。你称呼甜小朵为「小朵姐」，称呼白洁为「白洁姐」。\n你的穿着风格：日系文艺风，棉麻衬衫、素色长裙、帆布鞋、帆布包，戴银色细链锁骨链，看书或驻唱时戴圆框眼镜。\n你的日常习惯：早上泡一壶花茶带去书店，驻唱时会把眼镜摘掉。\n你的住所：新华公寓（暖阳区），骑电动车上班，5分钟。\n你的工作地点：新华书店（暖阳区）。\n你的驻唱地点：寻觅小酒吧（暖阳区），每周二、周五晚上驻唱。\n你安静内向、温柔细腻，内心世界非常丰富。\n你始终记得：你是小雅，是用户的女朋友之一，你永远不会跳戏。",
                "workAddr": "暖阳街与暖阳街交叉口",
                "emoji": "📚",
                "tag": "📖 店员"
            }
        ]
    }
    return default

# ============================================================
#  数据操作
# ============================================================
def load_data():
    if not os.path.exists(DATA_FILE):
        data = create_default_data()
        save_data(data)
        return data
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ============================================================
#  自适应文本框
# ============================================================
class AutoResizeText(tk.Text):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<<Modified>>', self._on_change)

    def _on_change(self, event):
        self._adjust_height()

    def _adjust_height(self):
        self.update_idletasks()
        lines = int(self.index('end-1c').split('.')[0])
        req_height = max(6, min(20, lines + 2))
        self.config(height=req_height)

# ============================================================
#  步进数字输入框
# ============================================================
class SpinEntry(tk.Frame):
    def __init__(self, master, min_val, max_val, step, default, **kwargs):
        super().__init__(master, **kwargs)
        self.min_val = min_val
        self.max_val = max_val
        self.step = step
        self.default = default

        self.entry = tk.Entry(self, width=8, font=('Segoe UI', 11),
                             justify='center', bg='#f8f9fa',
                             relief=tk.FLAT, bd=0,
                             highlightthickness=1,
                             highlightcolor='#b87a5a',
                             highlightbackground='#e0d6d0')
        self.entry.insert(0, str(default))
        self.entry.bind('<FocusOut>', self._validate)

        self.btn_dec = tk.Button(self, text='−', font=('Segoe UI', 12, 'bold'),
                                 bg='#f0ece8', fg='#5b4a3a', relief=tk.FLAT,
                                 activebackground='#e8ddd8', cursor='hand2',
                                 width=3, command=self._dec)
        self.btn_inc = tk.Button(self, text='+', font=('Segoe UI', 12, 'bold'),
                                 bg='#f0ece8', fg='#5b4a3a', relief=tk.FLAT,
                                 activebackground='#e8ddd8', cursor='hand2',
                                 width=3, command=self._inc)

        self.btn_dec.pack(side=tk.LEFT)
        self.entry.pack(side=tk.LEFT, padx=4)
        self.btn_inc.pack(side=tk.LEFT)

    def _validate(self, event):
        try:
            val = float(self.entry.get())
            val = max(self.min_val, min(self.max_val, val))
            if val == int(val):
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(int(val)))
            else:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(round(val, 1)))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(self.default))

    def _dec(self):
        try:
            val = float(self.entry.get())
            new_val = max(self.min_val, val - self.step)
            self._set_value(new_val)
        except:
            self._set_value(self.default)

    def _inc(self):
        try:
            val = float(self.entry.get())
            new_val = min(self.max_val, val + self.step)
            self._set_value(new_val)
        except:
            self._set_value(self.default)

    def _set_value(self, val):
        if val == int(val):
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(int(val)))
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(round(val, 1)))

    def get(self):
        try:
            val = float(self.entry.get())
            return int(val) if val == int(val) else val
        except:
            return self.default

    def set(self, val):
        if val == int(val):
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(int(val)))
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(round(val, 1)))

# ============================================================
#  主界面
# ============================================================
class DataEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("⚙️ Girls3 · 数据修改器")
        self.root.geometry("1100x750")
        self.root.minsize(1000, 700)
        self.root.configure(bg='#f5f0ec')

        self.colors = {
            'bg': '#f5f0ec',
            'bg2': '#faf7f4',
            'bg3': '#f0ece8',
            'border': '#e0d6d0',
            'text': '#2a1f1a',
            'text_dim': '#7a6a5a',
            'accent': '#b87a5a',
            'accent2': '#d4a080',
            'button': '#ede8e2',
            'button_hover': '#e0d8d0',
            'entry_bg': '#fcfaf8',
            'warning': '#d4a040',
        }

        self.data = load_data()
        self.current_persona_id = self.data['personas'][0]['id']
        self.has_unsaved_import = False

        self.create_widgets()
        self.load_persona(self.current_persona_id)

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=24, pady=20)

        # 标题
        title_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        title_frame.pack(fill=tk.X, pady=(0, 16))

        tk.Label(title_frame, text="⚙️ Girls3 · 数据修改器",
                 font=('Segoe UI', 20, 'bold'), bg=self.colors['bg'],
                 fg=self.colors['text']).pack(side=tk.LEFT)

        tk.Label(title_frame, text="修改后点击保存，直接写入 data.json",
                 font=('Segoe UI', 12), bg=self.colors['bg'],
                 fg=self.colors['text_dim']).pack(side=tk.LEFT, padx=(16, 0))

        # 主体
        body_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        body_frame.pack(fill=tk.BOTH, expand=True)

        # 左侧：角色切换
        left_frame = tk.Frame(body_frame, bg=self.colors['bg2'], width=180)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 16))
        left_frame.pack_propagate(False)

        tk.Label(left_frame, text="🎭 角色选择", font=('Segoe UI', 14, 'bold'),
                 bg=self.colors['bg2'], fg=self.colors['text']).pack(pady=(16, 12))

        self.role_buttons = {}
        for p in self.data['personas']:
            btn = tk.Button(
                left_frame,
                text=f"{p.get('emoji', '👤')} {p['name']}",
                font=('Segoe UI', 13),
                bg=self.colors['button'],
                fg=self.colors['text'],
                activebackground=self.colors['button_hover'],
                activeforeground=self.colors['accent'],
                relief=tk.FLAT, bd=0,
                cursor='hand2',
                pady=10,
                width=14
            )
            btn.pack(padx=10, pady=4, fill=tk.X)
            btn.bind('<Enter>', lambda e, b=btn: b.config(bg=self.colors['button_hover']))
            btn.bind('<Leave>', lambda e, b=btn: b.config(bg=self.colors['button']))
            btn.config(command=lambda pid=p['id']: self.switch_persona(pid))
            self.role_buttons[p['id']] = btn

        tk.Label(left_frame, text="🖼️ 背景图位置", font=('Segoe UI', 10),
                 bg=self.colors['bg2'], fg=self.colors['text_dim']).pack(pady=(20, 4))
        tk.Label(left_frame, text="img/角色名/avatar/background.jpg",
                 font=('Segoe UI', 9), bg=self.colors['bg2'],
                 fg=self.colors['text_dim']).pack()

        # 右侧
        right_frame = tk.Frame(body_frame, bg=self.colors['bg2'])
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        header_frame = tk.Frame(right_frame, bg=self.colors['bg2'])
        header_frame.pack(fill=tk.X, padx=16, pady=(12, 8))

        self.name_label = tk.Label(header_frame, text="",
                                   font=('Segoe UI', 16, 'bold'),
                                   bg=self.colors['bg2'], fg=self.colors['accent'])
        self.name_label.pack(side=tk.LEFT)

        # 导入未保存警告
        self.import_warning = tk.Label(
            header_frame,
            text="⚠️ 导入的数据尚未保存，请点击「保存」写入 data.json",
            font=('Segoe UI', 10),
            bg=self.colors['warning'],
            fg='#ffffff',
            padx=12,
            pady=4
        )
        self.import_warning.pack(side=tk.RIGHT)
        self.import_warning.pack_forget()

        # 滚动区域
        canvas = tk.Canvas(right_frame, bg=self.colors['bg2'], highlightthickness=0)
        scrollbar = tk.Scrollbar(right_frame, orient=tk.VERTICAL, command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg=self.colors['bg2'])

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(16, 0), pady=(0, 12))
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=(0, 12))

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.scroll_frame = scroll_frame
        self.persona_entries = {}
        self.sys_entries = {}

        self._build_form(scroll_frame)

    def _build_form(self, parent):
        # 基本信息
        self._section(parent, "📋 基本信息")

        info_frame = tk.Frame(parent, bg=self.colors['bg2'])
        info_frame.pack(fill=tk.X, padx=6, pady=(4, 8))

        fields = [
            ('姓名', 'name', 12),
            ('出生日期', 'birthday', 14),
            ('性别', 'gender', 8),
            ('身高(cm)', 'height', 8),
            ('体重(kg)', 'weight', 8),
            ('三围', 'bust', 14),
            ('鞋码', 'shoe', 8),
        ]

        for i, (label, key, width) in enumerate(fields):
            if i % 3 == 0:
                row = tk.Frame(info_frame, bg=self.colors['bg2'])
                row.pack(fill=tk.X, pady=3)

            f = tk.Frame(row, bg=self.colors['bg2'])
            f.pack(side=tk.LEFT, padx=(0 if i % 3 == 0 else 16, 0), expand=True, fill=tk.X)

            tk.Label(f, text=label, font=('Segoe UI', 10),
                     bg=self.colors['bg2'], fg=self.colors['text_dim']).pack(side=tk.LEFT)

            entry = tk.Entry(f, font=('Segoe UI', 10), bg=self.colors['entry_bg'],
                             fg=self.colors['text'], relief=tk.FLAT, bd=0,
                             highlightthickness=1, highlightcolor=self.colors['accent'],
                             highlightbackground=self.colors['border'])
            entry.pack(side=tk.LEFT, padx=(6, 0), fill=tk.X, expand=True)
            entry.config(width=width)
            self.persona_entries[key] = entry

        long_fields = [
            ('工作单位', 'workplace'),
            ('家庭住址', 'address'),
            ('所在区域', 'district'),
            ('通勤方式', 'commute'),
        ]

        for label, key in long_fields:
            f = tk.Frame(info_frame, bg=self.colors['bg2'])
            f.pack(fill=tk.X, pady=2)

            tk.Label(f, text=label, font=('Segoe UI', 10),
                     bg=self.colors['bg2'], fg=self.colors['text_dim'], width=10, anchor='e').pack(side=tk.LEFT)

            entry = tk.Entry(f, font=('Segoe UI', 10), bg=self.colors['entry_bg'],
                             fg=self.colors['text'], relief=tk.FLAT, bd=0,
                             highlightthickness=1, highlightcolor=self.colors['accent'],
                             highlightbackground=self.colors['border'])
            entry.pack(side=tk.LEFT, padx=(6, 0), fill=tk.X, expand=True)
            self.persona_entries[key] = entry

        # 角色描述
        self._section(parent, "📝 角色描述")

        desc_fields = [
            ('穿着风格', 'style'),
            ('性格特点', 'personality'),
            ('日常习惯', 'habits'),
            ('常去地点', 'places'),
        ]

        for label, key in desc_fields:
            f = tk.Frame(parent, bg=self.colors['bg2'])
            f.pack(fill=tk.X, padx=6, pady=2)

            tk.Label(f, text=label, font=('Segoe UI', 10),
                     bg=self.colors['bg2'], fg=self.colors['text_dim'], width=10, anchor='e').pack(side=tk.LEFT)

            entry = tk.Entry(f, font=('Segoe UI', 10), bg=self.colors['entry_bg'],
                             fg=self.colors['text'], relief=tk.FLAT, bd=0,
                             highlightthickness=1, highlightcolor=self.colors['accent'],
                             highlightbackground=self.colors['border'])
            entry.pack(side=tk.LEFT, padx=(6, 0), fill=tk.X, expand=True)
            self.persona_entries[key] = entry

        # 人设
        self._section(parent, "📄 完整人设 System Prompt")

        prompt_frame = tk.Frame(parent, bg=self.colors['bg2'])
        prompt_frame.pack(fill=tk.BOTH, expand=True, padx=6, pady=4)

        self.prompt_text = AutoResizeText(
            prompt_frame,
            font=('Segoe UI', 10),
            bg=self.colors['entry_bg'],
            fg=self.colors['text'],
            relief=tk.FLAT,
            bd=0,
            highlightthickness=1,
            highlightcolor=self.colors['accent'],
            highlightbackground=self.colors['border'],
            wrap=tk.WORD,
            height=8
        )
        self.prompt_text.pack(fill=tk.BOTH, expand=True)

        # 系统参数
        self._section(parent, "⚙️ 系统参数")

        sys_frame = tk.Frame(parent, bg=self.colors['bg2'])
        sys_frame.pack(fill=tk.X, padx=6, pady=4)

        sys_params = [
            ('普通触发概率', 'mediaProb', 0, 1, 0.1, 0.8),
            ('Naked 概率', 'nakedProb', 0, 1, 0.1, 0.3),
            ('最大回复字数', 'maxTokens', 2, 400, 2, 400),
            ('记忆条数', 'maxHistory', 10, 200, 5, 60),
            ('普通图片数量', 'maxFileNum', 1, 30, 1, 30),
            ('Naked 图片数量', 'maxNakedNum', 1, 15, 1, 15),
            ('音频文件数量', 'maxAudioNum', 1, 30, 1, 30),
        ]

        for i, (label, key, min_v, max_v, step, default) in enumerate(sys_params):
            if i % 3 == 0:
                row = tk.Frame(sys_frame, bg=self.colors['bg2'])
                row.pack(fill=tk.X, pady=3)

            f = tk.Frame(row, bg=self.colors['bg2'])
            f.pack(side=tk.LEFT, padx=(0 if i % 3 == 0 else 16, 0), expand=True, fill=tk.X)

            tk.Label(f, text=label, font=('Segoe UI', 10),
                     bg=self.colors['bg2'], fg=self.colors['text_dim']).pack(side=tk.LEFT)

            spin = SpinEntry(f, min_v, max_v, step, default)
            spin.pack(side=tk.LEFT, padx=(8, 0))
            self.sys_entries[key] = spin

        # 城市
        city_frame = tk.Frame(parent, bg=self.colors['bg2'])
        city_frame.pack(fill=tk.X, padx=6, pady=8)

        tk.Label(city_frame, text="🏙️ 城市名称", font=('Segoe UI', 10),
                 bg=self.colors['bg2'], fg=self.colors['text_dim']).pack(side=tk.LEFT)

        self.city_entry = tk.Entry(city_frame, font=('Segoe UI', 10),
                                   bg=self.colors['entry_bg'], fg=self.colors['text'],
                                   relief=tk.FLAT, bd=0, width=20,
                                   highlightthickness=1, highlightcolor=self.colors['accent'],
                                   highlightbackground=self.colors['border'])
        self.city_entry.pack(side=tk.LEFT, padx=(10, 0))

        # 按钮
        btn_frame = tk.Frame(parent, bg=self.colors['bg2'])
        btn_frame.pack(fill=tk.X, padx=6, pady=(12, 4))

        tk.Button(
            btn_frame, text="↻ 恢复默认",
            font=('Segoe UI', 11),
            bg=self.colors['button'], fg=self.colors['text'],
            activebackground=self.colors['button_hover'],
            activeforeground=self.colors['accent'],
            relief=tk.FLAT, bd=0, cursor='hand2',
            padx=20, pady=8, command=self.reset_defaults
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            btn_frame, text="📤 导出当前角色",
            font=('Segoe UI', 11),
            bg=self.colors['button'], fg=self.colors['text'],
            activebackground=self.colors['button_hover'],
            activeforeground=self.colors['accent'],
            relief=tk.FLAT, bd=0, cursor='hand2',
            padx=20, pady=8, command=self.export_data
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            btn_frame, text="📥 导入配置",
            font=('Segoe UI', 11),
            bg=self.colors['button'], fg=self.colors['text'],
            activebackground=self.colors['button_hover'],
            activeforeground=self.colors['accent'],
            relief=tk.FLAT, bd=0, cursor='hand2',
            padx=20, pady=8, command=self.import_data
        ).pack(side=tk.LEFT, padx=4)

        tk.Button(
            btn_frame, text="💾 保存到 data.json",
            font=('Segoe UI', 11, 'bold'),
            bg=self.colors['accent'], fg='#ffffff',
            activebackground=self.colors['accent2'], activeforeground='#ffffff',
            relief=tk.FLAT, bd=0, cursor='hand2',
            padx=24, pady=8, command=self.save_data
        ).pack(side=tk.RIGHT, padx=4)

        self.status_label = tk.Label(
            parent,
            text="✅ 就绪",
            font=('Segoe UI', 10),
            bg=self.colors['bg2'],
            fg=self.colors['text_dim']
        )
        self.status_label.pack(pady=(4, 0))

    def _section(self, parent, title):
        f = tk.Frame(parent, bg=self.colors['bg2'])
        f.pack(fill=tk.X, padx=6, pady=(12, 2))

        tk.Label(f, text=title, font=('Segoe UI', 12, 'bold'),
                 bg=self.colors['bg2'], fg=self.colors['accent']).pack(side=tk.LEFT)

        sep = tk.Frame(parent, height=1, bg=self.colors['border'])
        sep.pack(fill=tk.X, padx=6, pady=(0, 4))

    def switch_persona(self, persona_id):
        if persona_id == self.current_persona_id:
            return
        self.collect_persona_data()
        self.current_persona_id = persona_id
        self.load_persona(persona_id)

        for pid, btn in self.role_buttons.items():
            if pid == persona_id:
                btn.config(fg=self.colors['accent'])
            else:
                btn.config(fg=self.colors['text'])

    def load_persona(self, persona_id):
        for p in self.data['personas']:
            if p['id'] == persona_id:
                for key, entry in self.persona_entries.items():
                    entry.delete(0, tk.END)
                    entry.insert(0, str(p[key]) if p[key] is not None else '')
                self.prompt_text.delete(1.0, tk.END)
                self.prompt_text.insert(1.0, p.get('systemPrompt', ''))
                self.name_label.config(text=f"{p.get('emoji', '👤')} {p['name']}")
                break

        for key, spin in self.sys_entries.items():
            if key in self.data:
                spin.set(self.data[key])

        self.city_entry.delete(0, tk.END)
        self.city_entry.insert(0, self.data.get('city', '舒心市'))

        self.status_label.config(text="✅ 就绪", fg=self.colors['text_dim'])

    def collect_persona_data(self):
        for p in self.data['personas']:
            if p['id'] == self.current_persona_id:
                for key, entry in self.persona_entries.items():
                    p[key] = entry.get()
                p['systemPrompt'] = self.prompt_text.get(1.0, tk.END).strip()
                break

    def collect_sys_data(self):
        for key, spin in self.sys_entries.items():
            self.data[key] = spin.get()
        self.data['city'] = self.city_entry.get().strip()

    def save_data(self):
        try:
            self.collect_persona_data()
            self.collect_sys_data()
            save_data(self.data)
            self.has_unsaved_import = False
            self.import_warning.pack_forget()
            self.status_label.config(text="✅ 保存成功！", fg=self.colors['accent'])
            self.root.after(2000, lambda: self.status_label.config(text="✅ 就绪", fg=self.colors['text_dim']))
        except Exception as e:
            messagebox.showerror("保存失败", f"保存 data.json 时出错:\n{str(e)}")
            self.status_label.config(text="❌ 保存失败", fg='#cf6679')

    def reset_defaults(self):
        """恢复默认 = 一步到位，直接生成新的 data.json"""
        if not messagebox.askyesno("确认恢复", "确定恢复所有数据到默认值吗？\n当前修改将会丢失！"):
            return

        try:
            default_data = create_default_data()
            save_data(default_data)
            self.data = default_data

            self.current_persona_id = self.data['personas'][0]['id']
            self.has_unsaved_import = False
            self.import_warning.pack_forget()

            self.load_persona(self.current_persona_id)

            for pid, btn in self.role_buttons.items():
                if pid == self.current_persona_id:
                    btn.config(fg=self.colors['accent'])
                else:
                    btn.config(fg=self.colors['text'])

            self.status_label.config(text="↻ 已恢复默认", fg=self.colors['accent'])
            self.root.after(2000, lambda: self.status_label.config(text="✅ 就绪", fg=self.colors['text_dim']))

        except Exception as e:
            messagebox.showerror("恢复失败", f"恢复默认时出错:\n{str(e)}")

    def export_data(self):
        """导出当前角色数据"""
        self.collect_persona_data()
        date_str = datetime.now().strftime("%Y%m%d")
        filename = f"data_{self.current_persona_id}_{date_str}.json"

        export_data = None
        for p in self.data['personas']:
            if p['id'] == self.current_persona_id:
                export_data = {
                    "version": "1.0",
                    "exported_at": datetime.now().isoformat(),
                    "persona": p
                }
                break

        if not export_data:
            return

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            self.status_label.config(text=f"✅ 已导出: {filename}", fg=self.colors['accent'])
            self.root.after(3000, lambda: self.status_label.config(text="✅ 就绪", fg=self.colors['text_dim']))
        except Exception as e:
            messagebox.showerror("导出失败", f"导出文件时出错:\n{str(e)}")

    def import_data(self):
        """导入角色数据（必须与当前编辑的角色一致）"""
        filename = filedialog.askopenfilename(
            title="选择要导入的配置文件",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if not filename:
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                import_data = json.load(f)

            if 'persona' not in import_data:
                messagebox.showerror("导入失败", "文件格式不正确，找不到 'persona' 字段")
                return

            imported_persona = import_data['persona']
            imported_id = imported_persona.get('id')

            # 获取当前角色名称
            current_name = ""
            for p in self.data['personas']:
                if p['id'] == self.current_persona_id:
                    current_name = p['name']
                    break

            # ★★★ 检查导入的角色是否与当前编辑的角色一致 ★★★
            if imported_id != self.current_persona_id:
                imported_name = imported_persona.get('name', '未知')
                messagebox.showerror(
                    "导入失败",
                    f"当前编辑的是「{current_name}」，导入的文件属于「{imported_name}」\n角色不匹配，无法导入"
                )
                return

            # 角色匹配：加载到界面预览
            self.collect_persona_data()

            for p in self.data['personas']:
                if p['id'] == imported_id:
                    for key, value in imported_persona.items():
                        p[key] = value
                    break

            self.load_persona(self.current_persona_id)

            self.has_unsaved_import = True
            self.import_warning.pack(side=tk.RIGHT)

            self.status_label.config(text="📥 导入成功，请点击「保存」写入 data.json", fg=self.colors['warning'])
            self.root.after(3000, lambda: self.status_label.config(text="⚠️ 未保存", fg=self.colors['warning']))

        except json.JSONDecodeError:
            messagebox.showerror("导入失败", "文件格式不正确，不是有效的 JSON 文件")
        except Exception as e:
            messagebox.showerror("导入失败", f"导入时出错:\n{str(e)}")


# ============================================================
#  启动
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = DataEditor(root)
    root.mainloop()
"""
Generate placeholder illustrations for each chapter.
Run: python generate_images.py
Requires: pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import random
import os
import math

random.seed(42)

ASSETS = "assets"
os.makedirs(ASSETS, exist_ok=True)

# --- Color palette ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (80, 80, 80)
BLUE = (59, 130, 246)
LIGHT_BLUE = (219, 234, 254)
RED = (239, 68, 68)
LIGHT_RED = (254, 226, 226)
GREEN = (34, 197, 94)
LIGHT_GREEN = (220, 252, 231)
YELLOW = (234, 179, 8)
LIGHT_YELLOW = (254, 249, 195)
PURPLE = (147, 51, 234)
LIGHT_PURPLE = (243, 232, 255)
ORANGE = (249, 115, 22)
TEAL = (20, 184, 166)
TERMINAL_BG = (30, 30, 30)
TERMINAL_GREEN = (74, 222, 128)
TERMINAL_WHITE = (229, 231, 235)


def img_new(w=800, h=500, bg=WHITE):
    img = Image.new("RGB", (w, h), bg)
    return img, ImageDraw.Draw(img)


def save(img, name):
    img.save(os.path.join(ASSETS, name))
    print(f"  saved {name}")


def rounded_rect(draw, xy, fill, outline=None, radius=8):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline)


def draw_arrow(draw, x0, y0, x1, y1, color=DARK_GRAY, width=2, head=8):
    draw.line([x0, y0, x1, y1], fill=color, width=width)
    angle = math.atan2(y1 - y0, x1 - x0)
    lx = x1 - head * math.cos(angle - 0.4)
    ly = y1 - head * math.sin(angle - 0.4)
    rx = x1 - head * math.cos(angle + 0.4)
    ry = y1 - head * math.sin(angle + 0.4)
    draw.polygon([(x1, y1), (lx, ly), (rx, ry)], fill=color)


def draw_box(draw, xy, label, fill=LIGHT_BLUE, outline=BLUE, text_color=DARK_GRAY):
    rounded_rect(draw, xy, fill=fill, outline=outline)
    x0, y0, x1, y1 = xy
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    tw = len(label) * 6
    draw.text((cx - tw // 2, cy - 6), label, fill=text_color)


# ============================================================
# Chapter 1: Development Environment
# ============================================================

def ch1_01():
    img, d = img_new()
    # VS Code window mockup
    rounded_rect(d, [80, 40, 720, 460], fill=WHITE, outline=GRAY)
    d.rectangle([80, 40, 720, 80], fill=(36, 36, 36))
    d.text((100, 55), "Visual Studio Code - Download", fill=WHITE)
    # Download button area
    rounded_rect(d, [250, 180, 550, 280], fill=BLUE)
    d.text((310, 215), "Download for Linux", fill=WHITE)
    d.text((340, 245), ".deb / .rpm", fill=(200, 220, 255))
    # Platform options
    for i, (label, color) in enumerate([("Windows", LIGHT_BLUE), ("macOS", LIGHT_GREEN), ("Linux", LIGHT_PURPLE)]):
        x = 180 + i * 170
        rounded_rect(d, [x, 320, x + 140, 380], fill=color, outline=GRAY)
        d.text((x + 30, 345), label, fill=DARK_GRAY)
    save(img, "ch1-01-vscode-download.png")


def ch1_02():
    img, d = img_new()
    # VS Code welcome tab
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.text((20, 12), "Welcome", fill=WHITE)
    d.rectangle([0, 40, 200, 500], fill=(37, 37, 38))  # sidebar
    d.text((20, 60), "EXPLORER", fill=GRAY)
    d.rectangle([200, 40, 800, 500], fill=(30, 30, 30))  # editor
    d.text((350, 150), "Visual Studio Code", fill=WHITE)
    d.text((340, 200), "Get Started", fill=BLUE)
    d.text((340, 240), "Recent Projects", fill=GRAY)
    d.text((340, 270), "Help & Documentation", fill=GRAY)
    save(img, "ch1-02-vscode-welcome.png")


def ch1_03():
    img, d = img_new()
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.text((20, 12), "Extensions", fill=WHITE)
    d.rectangle([0, 40, 250, 500], fill=(37, 37, 38))
    # Search bar
    rounded_rect(d, [10, 55, 240, 80], fill=(60, 60, 60))
    d.text((20, 62), "Search Extensions...", fill=GRAY)
    # Extension items
    for i, (name, desc) in enumerate([
        ("Python", "Python language support"),
        ("Prettier", "Code formatter"),
        ("ESLint", "JavaScript linter"),
        ("GitLens", "Git supercharged"),
    ]):
        y = 95 + i * 55
        rounded_rect(d, [10, y, 240, y + 48], fill=(45, 45, 48))
        d.text((20, y + 8), name, fill=WHITE)
        d.text((20, y + 26), desc, fill=GRAY)
    d.rectangle([250, 40, 800, 500], fill=(30, 30, 30))
    d.text((400, 200), "Select an extension to view details", fill=GRAY)
    save(img, "ch1-03-vscode-extensions.png")


def ch1_04():
    img, d = img_new(h=300, bg=TERMINAL_BG)
    d.text((20, 20), "Windows PowerShell (Administrator)", fill=TERMINAL_WHITE)
    d.line([20, 45, 780, 45], fill=GRAY)
    d.text((20, 60), "PS C:\\> ", fill=BLUE)
    d.text((100, 60), "wsl --install", fill=TERMINAL_WHITE)
    d.text((20, 90), "Installing: Ubuntu", fill=TERMINAL_GREEN)
    d.text((20, 115), "Ubuntu has been installed.", fill=TERMINAL_GREEN)
    d.text((20, 145), "The requested operation is successful.", fill=TERMINAL_GREEN)
    d.text((20, 175), "Please restart your computer to finish.", fill=YELLOW)
    save(img, "ch1-04-wsl-install.png")


def ch1_05():
    img, d = img_new(h=300, bg=TERMINAL_BG)
    d.text((20, 20), "Ubuntu", fill=TERMINAL_WHITE)
    d.line([20, 45, 780, 45], fill=GRAY)
    d.text((20, 60), "Installing, this may take a few minutes...", fill=TERMINAL_GREEN)
    d.text((20, 90), "Please create a default UNIX user account.", fill=TERMINAL_WHITE)
    d.text((20, 120), "Enter new UNIX username: ", fill=TERMINAL_WHITE)
    d.text((280, 120), "parkj", fill=TERMINAL_GREEN)
    d.text((20, 150), "New password: ", fill=TERMINAL_WHITE)
    d.text((160, 150), "********", fill=TERMINAL_GREEN)
    d.text((20, 180), "Retype new password: ", fill=TERMINAL_WHITE)
    d.text((230, 180), "********", fill=TERMINAL_GREEN)
    d.text((20, 220), "parkj@DESKTOP:~$ ", fill=TERMINAL_GREEN)
    d.text((200, 220), "_", fill=WHITE)
    save(img, "ch1-05-wsl-setup.png")


def ch1_06():
    img, d = img_new()
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.rectangle([0, 40, 250, 500], fill=(37, 37, 38))
    rounded_rect(d, [10, 55, 240, 80], fill=(60, 60, 60))
    d.text((20, 62), "wsl", fill=WHITE)
    # WSL extension
    rounded_rect(d, [10, 95, 240, 155], fill=(45, 45, 48), outline=BLUE)
    d.text((20, 103), "WSL", fill=WHITE)
    d.text((20, 123), "Open folders in WSL", fill=GRAY)
    d.rectangle([250, 40, 800, 500], fill=(30, 30, 30))
    d.text((350, 120), "WSL", fill=WHITE)
    d.text((350, 160), "Open any folder in the Windows", fill=GRAY)
    d.text((350, 180), "Subsystem for Linux (WSL)", fill=GRAY)
    rounded_rect(d, [350, 220, 460, 250], fill=BLUE)
    d.text((370, 228), "Install", fill=WHITE)
    save(img, "ch1-06-wsl-extension.png")


def ch1_07():
    img, d = img_new()
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.text((20, 12), "main.py - project", fill=WHITE)
    # Status bar with WSL indicator
    d.rectangle([0, 475, 800, 500], fill=(0, 122, 204))
    rounded_rect(d, [0, 475, 140, 500], fill=(22, 160, 133))
    d.text((10, 480), "WSL: Ubuntu", fill=WHITE)
    # sidebar
    d.rectangle([0, 40, 200, 475], fill=(37, 37, 38))
    d.text((20, 60), "EXPLORER", fill=GRAY)
    d.text((20, 90), "v project", fill=WHITE)
    d.text((35, 115), "main.py", fill=GRAY)
    d.text((35, 135), "utils.py", fill=GRAY)
    # Terminal
    d.rectangle([200, 350, 800, 475], fill=TERMINAL_BG)
    d.text((210, 360), "TERMINAL", fill=GRAY)
    d.text((210, 385), "parkj@DESKTOP:~/project$ ", fill=TERMINAL_GREEN)
    save(img, "ch1-07-wsl-connected.png")


def ch1_08():
    img, d = img_new()
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.rectangle([0, 40, 250, 500], fill=(37, 37, 38))
    rounded_rect(d, [10, 55, 240, 80], fill=(60, 60, 60))
    d.text((20, 62), "claude code", fill=WHITE)
    rounded_rect(d, [10, 95, 240, 160], fill=(45, 45, 48), outline=ORANGE)
    d.text((20, 103), "Claude Code", fill=WHITE)
    d.text((20, 123), "Anthropic", fill=GRAY)
    d.text((20, 138), "AI coding assistant", fill=GRAY)
    d.rectangle([250, 40, 800, 500], fill=(30, 30, 30))
    d.text((350, 120), "Claude Code", fill=WHITE)
    d.text((350, 150), "by Anthropic", fill=GRAY)
    rounded_rect(d, [350, 200, 460, 230], fill=ORANGE)
    d.text((370, 208), "Install", fill=WHITE)
    save(img, "ch1-08-claude-code-install.png")


def ch1_09():
    img, d = img_new()
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.text((20, 12), "app.py - project", fill=WHITE)
    d.rectangle([0, 40, 500, 500], fill=(30, 30, 30))  # editor
    d.text((20, 60), "  1  def hello():", fill=(200, 200, 200))
    d.text((20, 80), '  2      return "world"', fill=(200, 200, 200))
    # Claude panel on right
    d.rectangle([500, 40, 800, 500], fill=(25, 25, 30))
    d.line([500, 40, 500, 500], fill=GRAY)
    # Spark icon area
    rounded_rect(d, [510, 50, 790, 80], fill=(40, 40, 50))
    d.text((520, 58), "Claude Code", fill=ORANGE)
    d.text((520, 100), "How can I help you?", fill=GRAY)
    rounded_rect(d, [520, 420, 780, 460], fill=(50, 50, 60))
    d.text((530, 433), "Ask Claude...", fill=GRAY)
    save(img, "ch1-09-claude-panel.png")


def ch1_10():
    img, d = img_new()
    d.rectangle([500, 0, 800, 500], fill=(25, 25, 30))
    # Chat messages
    rounded_rect(d, [520, 30, 780, 100], fill=(40, 50, 70))
    d.text((530, 40), "Add error handling to", fill=WHITE)
    d.text((530, 60), "@utils.py parse_fasta()", fill=BLUE)
    d.text((530, 80), "function", fill=WHITE)
    rounded_rect(d, [520, 120, 780, 200], fill=(50, 40, 40))
    d.text((530, 130), "I'll add try/except blocks", fill=TERMINAL_GREEN)
    d.text((530, 150), "to handle file not found", fill=TERMINAL_GREEN)
    d.text((530, 170), "and invalid format errors.", fill=TERMINAL_GREEN)
    # Editor with diff
    d.rectangle([0, 0, 500, 500], fill=(30, 30, 30))
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.text((20, 12), "utils.py", fill=WHITE)
    d.text((20, 60), "  def parse_fasta(path):", fill=(200, 200, 200))
    d.rectangle([0, 80, 500, 100], fill=(30, 60, 30))  # added line
    d.text((20, 82), "+ try:", fill=GREEN)
    d.rectangle([0, 100, 500, 120], fill=(30, 60, 30))
    d.text((20, 102), "+     with open(path) as f:", fill=GREEN)
    d.rectangle([0, 160, 500, 180], fill=(30, 60, 30))
    d.text((20, 162), "+ except FileNotFoundError:", fill=GREEN)
    save(img, "ch1-10-claude-at-mention.png")


def ch1_11():
    img, d = img_new()
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.text((20, 12), "utils.py - diff", fill=WHITE)
    d.rectangle([0, 40, 800, 500], fill=(30, 30, 30))
    # Diff view
    lines = [
        (False, "  def parse_fasta(path):"),
        (False, '      """Parse a FASTA file."""'),
        (True,  "+     try:"),
        (False, "          with open(path) as f:"),
        (False, "              content = f.read()"),
        (True,  "+     except FileNotFoundError:"),
        (True,  '+         raise ValueError(f"File not found: {path}")'),
        (True,  "+     except Exception as e:"),
        (True,  '+         raise ValueError(f"Parse error: {e}")'),
    ]
    for i, (is_new, line) in enumerate(lines):
        y = 60 + i * 25
        if is_new:
            d.rectangle([0, y, 800, y + 22], fill=(30, 60, 30))
        d.text((60, y + 3), line, fill=GREEN if is_new else (200, 200, 200))
    # Accept/Reject buttons
    rounded_rect(d, [300, 380, 400, 410], fill=GREEN)
    d.text((320, 388), "Accept", fill=WHITE)
    rounded_rect(d, [420, 380, 520, 410], fill=RED)
    d.text((440, 388), "Reject", fill=WHITE)
    save(img, "ch1-11-claude-diff.png")


# ============================================================
# Chapter 2: Git & Github
# ============================================================

def ch2_01():
    # Centralized VCS
    img, d = img_new(h=400)
    # Server
    draw_box(d, [300, 40, 500, 100], "Central Server", fill=LIGHT_BLUE, outline=BLUE)
    # Users
    draw_box(d, [100, 250, 250, 310], "User 1", fill=LIGHT_GREEN, outline=GREEN)
    draw_box(d, [550, 250, 700, 310], "User 2", fill=LIGHT_GREEN, outline=GREEN)
    draw_arrow(d, 175, 250, 350, 100)
    draw_arrow(d, 625, 250, 450, 100)
    d.text((180, 160), "checkout / commit", fill=DARK_GRAY)
    d.text((470, 160), "checkout / commit", fill=DARK_GRAY)
    save(img, "ch2-01-centralized-vcs.png")


def ch2_02():
    # Distributed VCS
    img, d = img_new(h=450)
    draw_box(d, [300, 30, 500, 90], "Remote Repository", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_box(d, [50, 200, 250, 260], "User 1 (local)", fill=LIGHT_GREEN, outline=GREEN)
    draw_box(d, [550, 200, 750, 260], "User 2 (local)", fill=LIGHT_GREEN, outline=GREEN)
    # Version trees
    for ux in [100, 600]:
        for j in range(3):
            d.ellipse([ux + 20 + j * 30, 290, ux + 35 + j * 30, 305], fill=BLUE)
            if j < 2:
                d.line([ux + 35 + j * 30, 297, ux + 50 + j * 30, 297], fill=BLUE, width=2)
    d.text((100, 320), "Local version tree", fill=GRAY)
    d.text((600, 320), "Local version tree", fill=GRAY)
    draw_arrow(d, 150, 200, 350, 90)
    draw_arrow(d, 650, 200, 450, 90)
    d.text((130, 140), "push / pull", fill=DARK_GRAY)
    d.text((510, 140), "push / pull", fill=DARK_GRAY)
    save(img, "ch2-02-distributed-vcs.png")


def ch2_03():
    # Git logo placeholder
    img, d = img_new(w=400, h=400)
    # Simple Git-like logo
    d.ellipse([100, 100, 300, 300], fill=RED)
    d.ellipse([140, 140, 260, 260], fill=WHITE)
    d.ellipse([175, 175, 225, 225], fill=RED)
    d.rectangle([195, 100, 205, 180], fill=RED)
    d.rectangle([220, 193, 300, 207], fill=RED)
    save(img, "ch2-03-git-logo.png")


def _scenario_diagram(d, users, server_label, arrows, notes=None):
    draw_box(d, [300, 30, 500, 80], server_label, fill=LIGHT_PURPLE, outline=PURPLE)
    for name, xy, color in users:
        draw_box(d, xy, name, fill=color[0], outline=color[1])
    for x0, y0, x1, y1, label in arrows:
        draw_arrow(d, x0, y0, x1, y1, color=BLUE)
        mx, my = (x0 + x1) // 2, (y0 + y1) // 2
        d.text((mx - 20, my - 15), label, fill=DARK_GRAY)
    if notes:
        for x, y, text in notes:
            d.text((x, y), text, fill=DARK_GRAY)


def ch2_04():
    img, d = img_new(h=350)
    draw_box(d, [300, 30, 500, 80], "Remote Repo", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_box(d, [150, 220, 300, 270], "User 1", fill=LIGHT_GREEN, outline=GREEN)
    draw_arrow(d, 400, 80, 225, 220, color=BLUE)
    d.text((260, 140), "clone", fill=BLUE)
    save(img, "ch2-04-scenario1-clone.png")


def ch2_05():
    img, d = img_new(h=350)
    draw_box(d, [150, 50, 300, 100], "User 1 (local)", fill=LIGHT_GREEN, outline=GREEN)
    for i in range(3):
        d.ellipse([170 + i * 40, 130, 185 + i * 40, 145], fill=BLUE if i < 2 else GREEN)
        if i < 2:
            d.line([185 + i * 40, 137, 210 + i * 40, 137], fill=BLUE, width=2)
    d.text((260, 125), "new commit", fill=GREEN)
    draw_arrow(d, 225, 170, 225, 250)
    d.text((240, 200), "commit", fill=BLUE)
    draw_box(d, [150, 250, 300, 300], "Local Repo", fill=LIGHT_BLUE, outline=BLUE)
    save(img, "ch2-05-scenario1-commit.png")


def ch2_06():
    img, d = img_new(h=350)
    draw_box(d, [150, 200, 300, 250], "User 1 (local)", fill=LIGHT_GREEN, outline=GREEN)
    draw_box(d, [450, 40, 650, 90], "Remote Repo", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_arrow(d, 300, 210, 450, 70, color=GREEN)
    d.text((380, 120), "push", fill=GREEN)
    save(img, "ch2-06-scenario1-push.png")


def ch2_07():
    img, d = img_new(h=350)
    draw_box(d, [300, 30, 500, 80], "Remote Repo", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_box(d, [50, 220, 200, 270], "User 1", fill=LIGHT_GREEN, outline=GREEN)
    draw_box(d, [600, 220, 750, 270], "User 2", fill=LIGHT_YELLOW, outline=YELLOW)
    draw_arrow(d, 400, 80, 125, 220, color=BLUE)
    draw_arrow(d, 400, 80, 675, 220, color=BLUE)
    d.text((200, 140), "clone", fill=BLUE)
    d.text((530, 140), "clone", fill=BLUE)
    save(img, "ch2-07-scenario2-both-clone.png")


def ch2_08():
    img, d = img_new(h=350)
    draw_box(d, [300, 30, 500, 80], "Remote Repo", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_box(d, [50, 220, 200, 270], "User 1", fill=LIGHT_GREEN, outline=GREEN)
    draw_arrow(d, 125, 220, 350, 80, color=GREEN)
    d.text((170, 130), "commit + push", fill=GREEN)
    save(img, "ch2-08-scenario2-user1-push.png")


def ch2_09():
    img, d = img_new(h=350)
    draw_box(d, [300, 30, 500, 80], "Remote Repo", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_box(d, [600, 220, 750, 270], "User 2", fill=LIGHT_YELLOW, outline=YELLOW)
    draw_arrow(d, 675, 220, 450, 80, color=RED)
    d.text((510, 140), "push", fill=RED)
    # X mark
    d.line([540, 150, 560, 170], fill=RED, width=3)
    d.line([560, 150, 540, 170], fill=RED, width=3)
    d.text((565, 155), "rejected!", fill=RED)
    save(img, "ch2-09-scenario2-push-rejected.png")


def ch2_10():
    img, d = img_new(h=300, bg=TERMINAL_BG)
    d.text((20, 20), "$ git push origin main", fill=TERMINAL_WHITE)
    d.text((20, 50), "To github.com:user/repo.git", fill=TERMINAL_WHITE)
    d.text((20, 75), " ! [rejected]  main -> main (fetch first)", fill=RED)
    d.text((20, 100), "error: failed to push some refs", fill=RED)
    d.text((20, 130), "hint: Updates were rejected because the remote", fill=YELLOW)
    d.text((20, 155), "hint: contains work that you do not have locally.", fill=YELLOW)
    d.text((20, 185), "hint: Integrate the remote changes before pushing.", fill=YELLOW)
    save(img, "ch2-10-push-rejected-terminal.png")


def ch2_11():
    img, d = img_new(h=350)
    draw_box(d, [300, 30, 500, 80], "Remote Repo", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_box(d, [600, 220, 750, 270], "User 2", fill=LIGHT_YELLOW, outline=YELLOW)
    draw_arrow(d, 450, 80, 675, 220, color=BLUE)
    d.text((510, 140), "pull", fill=BLUE)
    save(img, "ch2-11-scenario2-user2-pull.png")


def ch2_12():
    img, d = img_new(h=350, bg=(30, 30, 30))
    # Merge conflict markers
    lines = [
        ("  def greeting():", TERMINAL_WHITE),
        ('<<<<<<< HEAD', RED),
        ('      return "Hello from User 1"', LIGHT_RED),
        ('=======', YELLOW),
        ('      return "Hi from User 2"', LIGHT_YELLOW),
        ('>>>>>>> origin/main', RED),
    ]
    for i, (line, color) in enumerate(lines):
        y = 40 + i * 35
        if "<<<" in line or ">>>" in line or "===" in line:
            d.rectangle([0, y - 3, 800, y + 25], fill=(60, 30, 30))
        d.text((30, y), line, fill=color)
    save(img, "ch2-12-merge-conflict.png")


def ch2_13():
    img, d = img_new()
    # Github conflict resolution UI mockup
    rounded_rect(d, [40, 30, 760, 470], fill=WHITE, outline=GRAY)
    d.rectangle([40, 30, 760, 70], fill=LIGHT_GRAY)
    d.text((60, 45), "Resolve merge conflicts - main", fill=DARK_GRAY)
    d.rectangle([60, 90, 740, 350], fill=(250, 250, 250))
    lines = [
        ("def greeting():", DARK_GRAY),
        ('<<<<<<< HEAD', RED),
        ('    return "Hello from User 1"', DARK_GRAY),
        ('=======', ORANGE),
        ('    return "Hi from User 2"', DARK_GRAY),
        ('>>>>>>> origin/main', RED),
    ]
    for i, (line, color) in enumerate(lines):
        d.text((80, 110 + i * 30), line, fill=color)
    rounded_rect(d, [300, 390, 500, 430], fill=GREEN)
    d.text((330, 403), "Mark as resolved", fill=WHITE)
    save(img, "ch2-13-github-conflict-resolution.png")


def ch2_14():
    img, d = img_new(h=350)
    draw_box(d, [300, 30, 500, 80], "Remote Repo", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_box(d, [600, 220, 750, 270], "User 2", fill=LIGHT_YELLOW, outline=YELLOW)
    draw_arrow(d, 675, 220, 450, 80, color=GREEN)
    d.text((510, 130), "merge + push", fill=GREEN)
    # Branch merge visualization
    for i in range(4):
        d.ellipse([200 + i * 50, 150, 215 + i * 50, 165], fill=BLUE)
        if i < 3:
            d.line([215 + i * 50, 157, 250 + i * 50, 157], fill=BLUE, width=2)
    d.ellipse([250, 180, 265, 195], fill=YELLOW)
    d.line([257, 180, 307, 165], fill=YELLOW, width=2)
    save(img, "ch2-14-scenario2-merge-push.png")


def ch2_15():
    img, d = img_new(h=350)
    draw_box(d, [300, 30, 500, 80], "Remote Repo", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_box(d, [600, 200, 750, 250], "User 2", fill=LIGHT_YELLOW, outline=YELLOW)
    d.text((610, 260), "modified files", fill=ORANGE)
    d.text((610, 280), "(not committed)", fill=ORANGE)
    d.text((350, 140), "pull needed but", fill=RED)
    d.text((350, 160), "local changes exist!", fill=RED)
    save(img, "ch2-15-scenario3-uncommitted.png")


def ch2_16():
    img, d = img_new(h=250, bg=TERMINAL_BG)
    d.text((20, 20), "$ git stash", fill=TERMINAL_WHITE)
    d.text((20, 50), "Saved working directory and index state", fill=TERMINAL_GREEN)
    d.text((20, 75), "  WIP on main: a1b2c3d Last commit message", fill=TERMINAL_GREEN)
    d.text((20, 110), "$ git status", fill=TERMINAL_WHITE)
    d.text((20, 140), "On branch main", fill=TERMINAL_GREEN)
    d.text((20, 165), "nothing to commit, working tree clean", fill=TERMINAL_GREEN)
    save(img, "ch2-16-git-stash.png")


def ch2_17():
    img, d = img_new(h=250, bg=TERMINAL_BG)
    d.text((20, 20), "$ git pull origin main", fill=TERMINAL_WHITE)
    d.text((20, 50), "Updating a1b2c3d..e4f5g6h", fill=TERMINAL_GREEN)
    d.text((20, 75), "Fast-forward", fill=TERMINAL_GREEN)
    d.text((20, 110), "$ git stash pop", fill=TERMINAL_WHITE)
    d.text((20, 140), "On branch main", fill=TERMINAL_GREEN)
    d.text((20, 165), "Changes not staged for commit:", fill=TERMINAL_GREEN)
    d.text((20, 190), "  modified:   analysis.py", fill=TERMINAL_GREEN)
    save(img, "ch2-17-git-stash-pop.png")


def ch2_18():
    # Fork diagram
    img, d = img_new(h=350)
    draw_box(d, [100, 50, 350, 110], "Original Repo", fill=LIGHT_BLUE, outline=BLUE)
    d.text((160, 70), "(someone/project)", fill=GRAY)
    draw_box(d, [450, 200, 700, 260], "Forked Repo", fill=LIGHT_GREEN, outline=GREEN)
    d.text((510, 220), "(my-account/project)", fill=GRAY)
    draw_arrow(d, 350, 80, 450, 230, color=PURPLE)
    d.text((380, 140), "Fork", fill=PURPLE)
    save(img, "ch2-18-fork-diagram.png")


def ch2_19():
    img, d = img_new()
    rounded_rect(d, [40, 30, 760, 470], fill=WHITE, outline=GRAY)
    d.rectangle([40, 30, 760, 70], fill=LIGHT_GRAY)
    d.text((60, 45), "Open a pull request", fill=DARK_GRAY)
    # Form
    d.text((60, 100), "base: main", fill=DARK_GRAY)
    d.text((200, 100), "<-", fill=DARK_GRAY)
    d.text((230, 100), "compare: feature-branch", fill=GREEN)
    rounded_rect(d, [60, 140, 720, 180], fill=LIGHT_GRAY)
    d.text((80, 153), "Add new BLAST search feature", fill=DARK_GRAY)
    rounded_rect(d, [60, 200, 720, 360], fill=LIGHT_GRAY)
    d.text((80, 220), "Description...", fill=GRAY)
    rounded_rect(d, [580, 400, 720, 440], fill=GREEN)
    d.text((600, 413), "Create PR", fill=WHITE)
    save(img, "ch2-19-create-pr.png")


def ch2_20():
    img, d = img_new()
    rounded_rect(d, [40, 30, 760, 470], fill=WHITE, outline=GRAY)
    d.rectangle([40, 30, 760, 70], fill=LIGHT_GRAY)
    d.text((60, 45), "Pull Request #42", fill=DARK_GRAY)
    d.text((60, 100), "Add new BLAST search feature", fill=BLACK)
    d.text((60, 130), "opened by parkj - 2 commits", fill=GRAY)
    # Tabs
    for i, tab in enumerate(["Conversation", "Commits", "Files changed"]):
        x = 60 + i * 180
        d.text((x, 170), tab, fill=BLUE if i == 0 else GRAY)
    d.line([60, 190, 740, 190], fill=LIGHT_GRAY)
    # Comment
    rounded_rect(d, [60, 210, 720, 320], fill=LIGHT_GRAY)
    d.text((80, 230), "parkj commented:", fill=DARK_GRAY)
    d.text((80, 260), "This PR adds BLAST search functionality.", fill=DARK_GRAY)
    d.text((80, 285), "Includes input validation and result parsing.", fill=DARK_GRAY)
    save(img, "ch2-20-pr-detail.png")


def ch2_21():
    img, d = img_new()
    rounded_rect(d, [40, 30, 760, 470], fill=WHITE, outline=GRAY)
    d.text((60, 50), "Pull Request #42 - Merged", fill=DARK_GRAY)
    rounded_rect(d, [60, 90, 180, 120], fill=PURPLE)
    d.text((80, 98), "Merged", fill=WHITE)
    d.text((200, 98), "parkj merged 2 commits into main", fill=GRAY)
    d.line([60, 150, 740, 150], fill=LIGHT_GRAY)
    # Timeline
    d.ellipse([90, 170, 110, 190], fill=GREEN)
    d.text((120, 173), "Checks passed", fill=GREEN)
    d.ellipse([90, 210, 110, 230], fill=GREEN)
    d.text((120, 213), "Approved by reviewer", fill=GREEN)
    d.ellipse([90, 250, 110, 270], fill=PURPLE)
    d.text((120, 253), "Merged via merge commit", fill=PURPLE)
    save(img, "ch2-21-pr-merged.png")


# ============================================================
# Chapter 3: Docker
# ============================================================

def ch3_01():
    img, d = img_new(h=400)
    # Without Docker
    draw_box(d, [30, 30, 370, 70], "Without Docker", fill=LIGHT_RED, outline=RED)
    for i, label in enumerate(["Dev Machine", "Server A", "Server B"]):
        x = 50 + i * 110
        rounded_rect(d, [x, 90, x + 100, 180], fill=LIGHT_GRAY, outline=GRAY)
        d.text((x + 10, 100), label, fill=DARK_GRAY)
        d.text((x + 10, 130), f"Python {['3.8', '3.10', '3.11'][i]}", fill=RED)
        d.text((x + 10, 150), f"lib v{['1.2', '2.0', '1.5'][i]}", fill=RED)
    # With Docker
    draw_box(d, [430, 30, 770, 70], "With Docker", fill=LIGHT_GREEN, outline=GREEN)
    for i, label in enumerate(["Dev Machine", "Server A", "Server B"]):
        x = 450 + i * 110
        rounded_rect(d, [x, 90, x + 100, 180], fill=LIGHT_GREEN, outline=GREEN)
        d.text((x + 10, 100), label, fill=DARK_GRAY)
        d.text((x + 10, 130), "Python 3.11", fill=GREEN)
        d.text((x + 10, 150), "lib v2.0", fill=GREEN)
    d.text((450, 200), "Identical environments!", fill=GREEN)
    save(img, "ch3-01-docker-consistency.png")


def ch3_02():
    img, d = img_new(h=400)
    # VM side
    draw_box(d, [30, 20, 370, 50], "Virtual Machine", fill=LIGHT_BLUE, outline=BLUE)
    layers_vm = [
        ("App A", LIGHT_GREEN), ("Bins/Libs", LIGHT_GRAY),
        ("Guest OS", LIGHT_YELLOW), ("App B", LIGHT_GREEN),
        ("Bins/Libs", LIGHT_GRAY), ("Guest OS", LIGHT_YELLOW),
    ]
    for i in range(2):
        x = 50 + i * 160
        for j, (label, color) in enumerate(layers_vm[i * 3:(i + 1) * 3]):
            y = 70 + j * 45
            rounded_rect(d, [x, y, x + 140, y + 38], fill=color, outline=GRAY)
            d.text((x + 20, y + 10), label, fill=DARK_GRAY)
    rounded_rect(d, [40, 210, 360, 250], fill=LIGHT_PURPLE, outline=PURPLE)
    d.text((140, 222), "Hypervisor", fill=DARK_GRAY)
    rounded_rect(d, [40, 260, 360, 300], fill=LIGHT_BLUE, outline=BLUE)
    d.text((130, 272), "Host OS", fill=DARK_GRAY)
    rounded_rect(d, [40, 310, 360, 350], fill=LIGHT_GRAY, outline=GRAY)
    d.text((130, 322), "Hardware", fill=DARK_GRAY)

    # Docker side
    draw_box(d, [430, 20, 770, 50], "Docker Container", fill=LIGHT_GREEN, outline=GREEN)
    for i in range(2):
        x = 450 + i * 160
        for j, (label, color) in enumerate([("App", LIGHT_GREEN), ("Bins/Libs", LIGHT_GRAY)]):
            y = 70 + j * 45
            rounded_rect(d, [x, y, x + 140, y + 38], fill=color, outline=GRAY)
            d.text((x + 20, y + 10), label, fill=DARK_GRAY)
    rounded_rect(d, [440, 170, 760, 210], fill=LIGHT_GREEN, outline=GREEN)
    d.text((540, 182), "Docker Engine", fill=DARK_GRAY)
    rounded_rect(d, [440, 220, 760, 260], fill=LIGHT_BLUE, outline=BLUE)
    d.text((540, 232), "Host OS (shared kernel)", fill=DARK_GRAY)
    rounded_rect(d, [440, 270, 760, 310], fill=LIGHT_GRAY, outline=GRAY)
    d.text((540, 282), "Hardware", fill=DARK_GRAY)
    save(img, "ch3-02-vm-vs-docker.png")


def ch3_03():
    img, d = img_new(h=280, bg=TERMINAL_BG)
    d.text((20, 20), "$ docker run hello-world", fill=TERMINAL_WHITE)
    d.text((20, 50), "Unable to find image 'hello-world:latest' locally", fill=TERMINAL_WHITE)
    d.text((20, 75), "latest: Pulling from library/hello-world", fill=TERMINAL_WHITE)
    d.text((20, 100), "Status: Downloaded newer image", fill=TERMINAL_GREEN)
    d.text((20, 135), "Hello from Docker!", fill=TERMINAL_GREEN)
    d.text((20, 165), "This message shows that your installation", fill=TERMINAL_WHITE)
    d.text((20, 185), "appears to be working correctly.", fill=TERMINAL_WHITE)
    save(img, "ch3-03-docker-hello-world.png")


def ch3_04():
    img, d = img_new(h=350, bg=TERMINAL_BG)
    d.text((20, 15), "$ docker compose up", fill=TERMINAL_WHITE)
    d.text((20, 45), "[+] Running 2/2", fill=TERMINAL_GREEN)
    d.text((20, 70), " - Container app-web-1   Started", fill=TERMINAL_GREEN)
    d.text((20, 95), " - Container app-db-1    Started", fill=TERMINAL_GREEN)
    d.text((20, 130), "web-1  | VITE v5.0.0  ready in 500 ms", fill=TERMINAL_WHITE)
    d.text((20, 155), "web-1  |", fill=TERMINAL_WHITE)
    d.text((20, 180), "web-1  |  > Local:   http://localhost:5173/", fill=BLUE)
    d.text((20, 210), "db-1   | PostgreSQL init process complete.", fill=TERMINAL_WHITE)
    d.text((20, 235), "db-1   | ready to accept connections", fill=TERMINAL_GREEN)
    save(img, "ch3-04-docker-compose-up.png")


# ============================================================
# Chapter 4: Python Data Analysis
# ============================================================

def ch4_01():
    img, d = img_new()
    # DataFrame table
    cols = ["gene_id", "gene_name", "logFC", "pvalue"]
    data = [
        ["ENSG001", "GAPDH", "1.23", "0.0012"],
        ["ENSG002", "ACTB", "-0.54", "0.1200"],
        ["ENSG003", "TP53", "2.41", "0.0001"],
        ["ENSG004", "MT-CO1", "0.82", "0.0340"],
        ["ENSG005", "IL6", "-1.80", "0.0050"],
    ]
    x0, y0 = 80, 80
    cw, rh = 160, 40
    # Header
    for i, col in enumerate(cols):
        rounded_rect(d, [x0 + i * cw, y0, x0 + (i + 1) * cw, y0 + rh], fill=BLUE)
        d.text((x0 + i * cw + 15, y0 + 12), col, fill=WHITE)
    # Index column
    for r in range(len(data)):
        ry = y0 + (r + 1) * rh
        rounded_rect(d, [x0 - 40, ry, x0, ry + rh], fill=LIGHT_BLUE)
        d.text((x0 - 30, ry + 12), str(r), fill=DARK_GRAY)
    # Data
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            ry = y0 + (r + 1) * rh
            bg = WHITE if r % 2 == 0 else (248, 250, 252)
            d.rectangle([x0 + c * cw, ry, x0 + (c + 1) * cw, ry + rh], fill=bg, outline=LIGHT_GRAY)
            d.text((x0 + c * cw + 15, ry + 12), val, fill=DARK_GRAY)
    d.text((80, y0 + (len(data) + 1) * rh + 20), "[5 rows x 4 columns]", fill=GRAY)
    save(img, "ch4-01-pandas-dataframe.png")


def ch4_02():
    img, d = img_new()
    # Axes
    ox, oy = 120, 420
    d.line([ox, 60, ox, oy], fill=DARK_GRAY, width=2)
    d.line([ox, oy, 720, oy], fill=DARK_GRAY, width=2)
    d.text((350, 440), "log2 Fold Change", fill=DARK_GRAY)
    d.text((30, 220), "-log10(p)", fill=DARK_GRAY)
    # Points
    for _ in range(300):
        fc = random.gauss(0, 1.5)
        pv = abs(random.gauss(0, 2)) + random.random()
        px = int(ox + (fc + 4) * 75)
        py = int(oy - pv * 50)
        if 120 < px < 720 and 60 < py < 420:
            if abs(fc) > 1 and pv > 1.3:
                color = RED if fc > 0 else BLUE
            else:
                color = GRAY
            d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=color)
    # Threshold lines
    d.line([ox + 3 * 75, 60, ox + 3 * 75, oy], fill=GRAY, width=1)  # fc=-1
    d.line([ox + 5 * 75, 60, ox + 5 * 75, oy], fill=GRAY, width=1)  # fc=1
    d.line([ox, int(oy - 1.3 * 50), 720, int(oy - 1.3 * 50)], fill=GRAY, width=1)  # p=0.05
    save(img, "ch4-02-matplotlib-volcano.png")


def ch4_03():
    img, d = img_new(w=1000, h=450)
    # Left: Histogram
    d.line([80, 380, 450, 380], fill=DARK_GRAY, width=2)
    d.line([80, 380, 80, 50], fill=DARK_GRAY, width=2)
    d.text((200, 20), "Distribution of logFC", fill=DARK_GRAY)
    heights = [30, 60, 120, 180, 220, 200, 150, 80, 40, 20]
    for i, h in enumerate(heights):
        x = 95 + i * 35
        d.rectangle([x, 380 - h, x + 30, 380], fill=BLUE, outline=WHITE)
    # Right: Scatter
    d.line([560, 380, 930, 380], fill=DARK_GRAY, width=2)
    d.line([560, 380, 560, 50], fill=DARK_GRAY, width=2)
    d.text((700, 20), "Volcano Plot", fill=DARK_GRAY)
    for _ in range(150):
        px = random.randint(580, 910)
        py = random.randint(70, 370)
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=GRAY)
    save(img, "ch4-03-matplotlib-subplot.png")


def ch4_04():
    img, d = img_new()
    types = ["T cell", "B cell", "NK cell", "Monocyte"]
    colors = [LIGHT_BLUE, LIGHT_GREEN, LIGHT_RED, LIGHT_YELLOW]
    outlines = [BLUE, GREEN, RED, YELLOW]
    d.line([100, 420, 700, 420], fill=DARK_GRAY, width=2)
    d.line([100, 420, 100, 60], fill=DARK_GRAY, width=2)
    d.text((50, 230), "expr", fill=DARK_GRAY)
    for i, t in enumerate(types):
        x = 180 + i * 140
        med = 250 + random.randint(-40, 40)
        q1, q3 = med + 50, med - 50
        wlo, whi = med + 80, med - 80
        d.line([x, whi, x, q3], fill=outlines[i], width=2)
        d.line([x, q1, x, wlo], fill=outlines[i], width=2)
        rounded_rect(d, [x - 35, q3, x + 35, q1], fill=colors[i], outline=outlines[i])
        d.line([x - 35, med, x + 35, med], fill=outlines[i], width=3)
        d.line([x - 15, whi, x + 15, whi], fill=outlines[i], width=2)
        d.line([x - 15, wlo, x + 15, wlo], fill=outlines[i], width=2)
        d.text((x - 20, 430), t, fill=DARK_GRAY)
    save(img, "ch4-04-seaborn-boxplot.png")


def ch4_05():
    img, d = img_new()
    d.text((60, 20), "Gene Expression Heatmap", fill=DARK_GRAY)
    for r in range(12):
        for c in range(18):
            val = random.random()
            red = int(255 * val)
            blue = int(255 * (1 - val))
            color = (red, 60, blue)
            d.rectangle([100 + c * 35, 60 + r * 32, 133 + c * 35, 90 + r * 32], fill=color)
    # Color bar
    for i in range(100):
        v = i / 100
        d.rectangle([740, 60 + int(v * 384), 760, 64 + int(v * 384)], fill=(int(255 * v), 60, int(255 * (1 - v))))
    d.text((740, 450), "High", fill=DARK_GRAY)
    d.text((740, 45), "Low", fill=DARK_GRAY)
    save(img, "ch4-05-seaborn-heatmap.png")


# ============================================================
# Chapter 5: Scanpy
# ============================================================

def ch5_01():
    img, d = img_new(h=450)
    # Central X matrix
    draw_box(d, [270, 140, 530, 310], "X\n(cells x genes)", fill=LIGHT_BLUE, outline=BLUE)
    # obs (left)
    draw_box(d, [60, 140, 240, 310], "obs\n(cell metadata)", fill=LIGHT_RED, outline=RED)
    draw_arrow(d, 240, 225, 270, 225)
    # var (top)
    draw_box(d, [270, 30, 530, 110], "var\n(gene metadata)", fill=LIGHT_GREEN, outline=GREEN)
    draw_arrow(d, 400, 110, 400, 140)
    # obsm (right)
    draw_box(d, [560, 140, 740, 230], "obsm\n(UMAP, PCA)", fill=LIGHT_YELLOW, outline=YELLOW)
    draw_arrow(d, 530, 185, 560, 185)
    # uns (right bottom)
    draw_box(d, [560, 260, 740, 340], "uns\n(unstructured)", fill=LIGHT_PURPLE, outline=PURPLE)
    draw_arrow(d, 530, 300, 560, 300)
    save(img, "ch5-01-anndata-structure.png")


def ch5_02():
    img, d = img_new(h=400)
    # MuData outer box
    rounded_rect(d, [60, 40, 740, 360], fill=WHITE, outline=PURPLE)
    d.text((350, 55), "MuData", fill=PURPLE)
    # RNA AnnData
    rounded_rect(d, [90, 100, 390, 330], fill=LIGHT_BLUE, outline=BLUE)
    d.text((190, 120), "mod['rna']", fill=BLUE)
    draw_box(d, [110, 160, 370, 300], "AnnData\n(5000 x 20000)", fill=(235, 245, 255), outline=BLUE)
    # ATAC AnnData
    rounded_rect(d, [410, 100, 710, 330], fill=LIGHT_GREEN, outline=GREEN)
    d.text((510, 120), "mod['atac']", fill=GREEN)
    draw_box(d, [430, 160, 690, 300], "AnnData\n(5000 x 100000)", fill=(235, 255, 240), outline=GREEN)
    save(img, "ch5-02-mudata-structure.png")


def ch5_03():
    img, d = img_new(w=900, h=400)
    titles = ["n_genes_by_counts", "total_counts", "pct_counts_mt"]
    for i in range(3):
        cx = 150 + i * 270
        d.line([cx - 80, 350, cx + 80, 350], fill=DARK_GRAY, width=1)
        d.text((cx - 60, 360), titles[i], fill=DARK_GRAY)
        # Violin shape
        pts = []
        for j in range(25):
            w = random.randint(10, 50)
            y = 80 + j * 10
            pts.append((cx - w, y))
        for j in range(24, -1, -1):
            w = random.randint(10, 50)
            y = 80 + j * 10
            pts.append((cx + w, y))
        d.polygon(pts, fill=LIGHT_BLUE, outline=BLUE)
        # Median line
        d.line([cx - 15, 200, cx + 15, 200], fill=WHITE, width=3)
    save(img, "ch5-03-qc-violin-plots.png")


def ch5_04():
    img, d = img_new()
    colors = [RED, GREEN, BLUE, YELLOW, PURPLE, TEAL, ORANGE]
    clusters = []
    for c in range(6):
        cx = 200 + random.randint(0, 400)
        cy = 100 + random.randint(0, 300)
        clusters.append((cx, cy, colors[c % len(colors)]))
    for cx, cy, color in clusters:
        for _ in range(120):
            px = int(cx + random.gauss(0, 30))
            py = int(cy + random.gauss(0, 30))
            if 20 < px < 780 and 20 < py < 480:
                d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=color)
    # Legend
    for i in range(6):
        d.ellipse([700, 50 + i * 25, 712, 62 + i * 25], fill=colors[i % len(colors)])
        d.text((720, 50 + i * 25), f"Cluster {i}", fill=DARK_GRAY)
    save(img, "ch5-04-umap-clusters.png")


def ch5_05():
    img, d = img_new(w=800, h=600)
    genes = ["CD3E", "CD14", "MS4A1", "NKG7"]
    for idx in range(4):
        ox = (idx % 2) * 400
        oy = (idx // 2) * 300
        d.rectangle([ox + 10, oy + 10, ox + 390, oy + 290], outline=LIGHT_GRAY)
        d.text((ox + 170, oy + 15), genes[idx], fill=DARK_GRAY)
        # Scatter with expression gradient
        for _ in range(250):
            px = ox + 200 + int(random.gauss(0, 60))
            py = oy + 160 + int(random.gauss(0, 50))
            if ox + 20 < px < ox + 380 and oy + 40 < py < oy + 280:
                expr = random.random()
                if random.random() < 0.3:
                    expr = min(1, expr + 0.5)
                r = int(200 * (1 - expr))
                g = int(200 * (1 - expr))
                b = int(100 + 155 * expr)
                d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(r, g, b))
    save(img, "ch5-05-umap-marker-genes.png")


# ============================================================
# Chapter 6: Snakemake
# ============================================================

def ch6_01():
    img, d = img_new(h=450)
    rules = [
        ("fastqc", LIGHT_BLUE, BLUE),
        ("trim", LIGHT_GREEN, GREEN),
        ("align", LIGHT_YELLOW, YELLOW),
        ("count", LIGHT_PURPLE, PURPLE),
    ]
    for i, (name, fill, outline) in enumerate(rules):
        y = 50 + i * 100
        draw_box(d, [300, y, 500, y + 55], name, fill=fill, outline=outline)
        if i < len(rules) - 1:
            draw_arrow(d, 400, y + 55, 400, y + 100, color=DARK_GRAY)
    # Parallel branches for samples
    for sx, label in [(150, "sample_A"), (600, "sample_B")]:
        d.text((sx - 20, 70), label, fill=GRAY)
        d.line([sx, 85, sx, 380], fill=GRAY, width=1)
    save(img, "ch6-01-snakemake-dag.png")


def ch6_02():
    img, d = img_new(h=380, bg=TERMINAL_BG)
    lines = [
        ("$ snakemake -n", TERMINAL_WHITE),
        ("", None),
        ("Building DAG of jobs...", TERMINAL_GREEN),
        ("Job stats:", TERMINAL_WHITE),
        ("job          count", TERMINAL_WHITE),
        ("-----------  -----", TERMINAL_WHITE),
        ("all              1", TERMINAL_WHITE),
        ("align            3", TERMINAL_WHITE),
        ("count            3", TERMINAL_WHITE),
        ("fastqc           3", TERMINAL_WHITE),
        ("trim             3", TERMINAL_WHITE),
        ("total           13", TERMINAL_GREEN),
        ("", None),
        ("This was a dry-run (flag -n).", YELLOW),
        ("The order of jobs does not reflect the order of execution.", YELLOW),
    ]
    for i, (text, color) in enumerate(lines):
        if color:
            d.text((20, 15 + i * 22), text, fill=color)
    save(img, "ch6-02-snakemake-dryrun.png")


# ============================================================
# Chapter 7: Project Directory Setup
# ============================================================

def ch7_01():
    img, d = img_new()
    d.rectangle([0, 0, 800, 500], fill=(255, 62, 0))
    d.text((200, 160), "SvelteKit", fill=WHITE)
    d.text((200, 220), "Web development, streamlined", fill=(255, 200, 180))
    rounded_rect(d, [200, 280, 380, 320], fill=WHITE)
    d.text((220, 293), "Get Started", fill=(255, 62, 0))
    save(img, "ch7-01-sveltekit-website.png")


def ch7_02():
    img, d = img_new()
    d.rectangle([0, 0, 800, 500], fill=(15, 23, 42))
    d.text((150, 140), "Rapidly build modern websites", fill=WHITE)
    d.text((150, 180), "without ever leaving your HTML.", fill=(56, 189, 248))
    rounded_rect(d, [150, 240, 360, 280], fill=(56, 189, 248))
    d.text((190, 253), "Get Started", fill=WHITE)
    save(img, "ch7-02-tailwindcss-website.png")


def ch7_03():
    img, d = img_new()
    rounded_rect(d, [50, 30, 750, 470], fill=WHITE, outline=GRAY)
    d.text((300, 60), "Node.js Downloads", fill=DARK_GRAY)
    rounded_rect(d, [150, 120, 380, 200], fill=LIGHT_GREEN, outline=GREEN)
    d.text((190, 145), "LTS  v22.x", fill=DARK_GRAY)
    d.text((190, 170), "Recommended", fill=GREEN)
    rounded_rect(d, [420, 120, 650, 200], fill=LIGHT_GRAY, outline=GRAY)
    d.text((470, 145), "Current  v23.x", fill=DARK_GRAY)
    d.text((470, 170), "Latest features", fill=GRAY)
    d.text((150, 250), "Package Manager:", fill=DARK_GRAY)
    d.text((170, 280), "[x]  nvm  (Node Version Manager)", fill=DARK_GRAY)
    d.text((170, 310), "[x]  pnpm  (Fast, disk space efficient)", fill=DARK_GRAY)
    save(img, "ch7-03-nodejs-nvm-pnpm.png")


def ch7_04():
    img, d = img_new()
    # Browser chrome
    rounded_rect(d, [50, 30, 750, 470], fill=WHITE, outline=GRAY)
    d.rectangle([50, 30, 750, 70], fill=LIGHT_GRAY)
    rounded_rect(d, [120, 40, 450, 60], fill=WHITE, outline=GRAY)
    d.text((140, 44), "localhost:5173", fill=DARK_GRAY)
    # Page content
    d.text((300, 150), "Welcome to SvelteKit", fill=DARK_GRAY)
    d.text((280, 200), "Visit svelte.dev/docs to get started", fill=BLUE)
    save(img, "ch7-04-sveltekit-dev-server.png")


# ============================================================
# Chapter 8: Landing Page Design
# ============================================================

def ch8_01():
    img, d = img_new()
    # Navbar
    d.rectangle([0, 0, 800, 60], fill=(30, 30, 40))
    d.text((30, 20), "BioTools", fill=WHITE)
    d.text((500, 20), "Home   Tools   Docs   About", fill=GRAY)
    rounded_rect(d, [700, 15, 780, 45], fill=BLUE)
    d.text((720, 23), "Login", fill=WHITE)
    # Hero
    d.rectangle([0, 60, 800, 280], fill=(20, 40, 80))
    d.text((100, 110), "Bioinformatics Made Simple", fill=WHITE)
    d.text((100, 150), "Powerful analysis tools for researchers", fill=(180, 200, 220))
    rounded_rect(d, [100, 200, 260, 240], fill=BLUE)
    d.text((130, 213), "Get Started", fill=WHITE)
    # Features
    for i in range(3):
        x = 50 + i * 250
        rounded_rect(d, [x, 300, x + 220, 460], fill=LIGHT_GRAY, outline=GRAY)
        d.ellipse([x + 85, 315, x + 135, 365], fill=LIGHT_BLUE, outline=BLUE)
        d.text((x + 50, 380), f"Feature {i + 1}", fill=DARK_GRAY)
    save(img, "ch8-01-landing-page-example.png")


def ch8_02():
    img, d = img_new()
    # Header
    rounded_rect(d, [100, 40, 700, 100], fill=LIGHT_BLUE, outline=BLUE)
    d.text((370, 63), "Header", fill=BLUE)
    # Body
    rounded_rect(d, [100, 110, 700, 380], fill=LIGHT_GREEN, outline=GREEN)
    d.text((375, 235), "Body", fill=GREEN)
    # Footer
    rounded_rect(d, [100, 390, 700, 460], fill=LIGHT_GRAY, outline=GRAY)
    d.text((375, 418), "Footer", fill=DARK_GRAY)
    save(img, "ch8-02-web-page-structure.png")


def ch8_03():
    img, d = img_new(h=300)
    # Style 1: Clean
    rounded_rect(d, [50, 30, 750, 80], fill=WHITE, outline=GRAY)
    d.text((70, 48), "Logo", fill=DARK_GRAY)
    d.text((300, 48), "Home    Tools    Docs    About", fill=GRAY)
    rounded_rect(d, [650, 40, 730, 70], fill=BLUE)
    d.text((665, 48), "Sign Up", fill=WHITE)
    # Style 2: Dark
    rounded_rect(d, [50, 120, 750, 170], fill=(30, 30, 40))
    d.text((70, 138), "BioLab", fill=WHITE)
    d.text((300, 138), "Home    Analysis    Data    Help", fill=GRAY)
    rounded_rect(d, [650, 130, 730, 160], fill=GREEN)
    d.text((670, 138), "Start", fill=WHITE)
    # Style 3: Gradient feel
    rounded_rect(d, [50, 210, 750, 260], fill=BLUE)
    d.text((70, 228), "GenomicHub", fill=WHITE)
    d.text((400, 228), "Features    Pricing    Support", fill=(200, 220, 255))
    save(img, "ch8-03-navbar-examples.png")


def ch8_04():
    img, d = img_new()
    d.rectangle([0, 0, 800, 500], fill=(15, 23, 42))
    d.text((80, 100), "Analyze Your Sequences", fill=WHITE)
    d.text((80, 150), "Fast and open-source bioinformatics tools", fill=(150, 180, 220))
    rounded_rect(d, [80, 220, 260, 265], fill=BLUE)
    d.text((110, 235), "Start Analysis", fill=WHITE)
    rounded_rect(d, [280, 220, 440, 265], fill=WHITE, outline=BLUE)
    d.text((310, 235), "Learn More", fill=BLUE)
    # DNA helix abstract
    for i in range(15):
        y = 80 + i * 25
        x1 = 550 + int(40 * math.sin(i * 0.8))
        x2 = 650 - int(40 * math.sin(i * 0.8))
        d.ellipse([x1 - 6, y - 6, x1 + 6, y + 6], fill=BLUE)
        d.ellipse([x2 - 6, y - 6, x2 + 6, y + 6], fill=RED)
        d.line([x1 + 6, y, x2 - 6, y], fill=(60, 80, 120), width=1)
    save(img, "ch8-04-hero-section-example.png")


def ch8_05():
    img, d = img_new(h=350)
    rounded_rect(d, [80, 50, 720, 300], fill=LIGHT_GRAY, outline=GRAY)
    d.text((300, 160), "Slide 1 of 3", fill=DARK_GRAY)
    # Left arrow
    d.polygon([(100, 175), (130, 150), (130, 200)], fill=GRAY)
    # Right arrow
    d.polygon([(700, 175), (670, 150), (670, 200)], fill=GRAY)
    # Dots
    for i in range(3):
        fill = DARK_GRAY if i == 0 else GRAY
        d.ellipse([375 + i * 25, 280, 390 + i * 25, 295], fill=fill)
    save(img, "ch8-05-carousel-example.png")


def ch8_06():
    img, d = img_new()
    icons = [LIGHT_BLUE, LIGHT_GREEN, LIGHT_PURPLE]
    outlines = [BLUE, GREEN, PURPLE]
    labels = ["Sequence Analysis", "Structure Prediction", "Data Visualization"]
    for i in range(3):
        x = 40 + i * 250
        rounded_rect(d, [x, 80, x + 230, 420], fill=WHITE, outline=LIGHT_GRAY)
        d.ellipse([x + 85, 110, x + 145, 170], fill=icons[i], outline=outlines[i])
        d.text((x + 40, 195), labels[i], fill=DARK_GRAY)
        for j in range(3):
            d.text((x + 25, 240 + j * 25), "Description line " + str(j + 1), fill=GRAY)
    save(img, "ch8-06-features-section.png")


def ch8_07():
    img, d = img_new(w=900, h=400)
    for idx, label in enumerate(["Variation A", "Variation B"]):
        ox = 30 + idx * 440
        rounded_rect(d, [ox, 30, ox + 410, 370], fill=WHITE, outline=GRAY)
        d.text((ox + 170, 10), label, fill=DARK_GRAY)
        # Mini page mockup
        d.rectangle([ox + 10, 60, ox + 400, 100], fill=(30, 30, 40))
        d.rectangle([ox + 10, 100, ox + 400, 200], fill=BLUE if idx == 0 else LIGHT_GRAY)
        for j in range(3):
            rounded_rect(d, [ox + 20 + j * 125, 220, ox + 135 + j * 125, 340], fill=LIGHT_GRAY, outline=GRAY)
    save(img, "ch8-07-gemini-mockups.png")


def ch8_08():
    img, d = img_new()
    rounded_rect(d, [50, 30, 750, 470], fill=WHITE, outline=GRAY)
    # Navbar
    d.rectangle([50, 30, 750, 80], fill=(30, 30, 40))
    d.text((70, 48), "BioApp  Home  Tools  About", fill=WHITE)
    # Hero
    d.rectangle([50, 80, 750, 250], fill=(20, 50, 100))
    d.text((200, 130), "Bioinformatics for Everyone", fill=WHITE)
    rounded_rect(d, [200, 190, 340, 220], fill=BLUE)
    d.text((230, 198), "Get Started", fill=WHITE)
    # Features
    for i in range(3):
        x = 80 + i * 220
        rounded_rect(d, [x, 270, x + 200, 440], fill=LIGHT_GRAY, outline=GRAY)
        d.text((x + 50, 340), f"Tool {i + 1}", fill=DARK_GRAY)
    save(img, "ch8-08-detailed-mockup.png")


def ch8_09():
    img, d = img_new()
    # VS Code with Claude panel
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.text((20, 12), "Claude Code - Design Implementation", fill=WHITE)
    # Left: image placeholder
    d.rectangle([0, 40, 400, 500], fill=(40, 40, 50))
    rounded_rect(d, [20, 60, 380, 300], fill=(60, 60, 70), outline=GRAY)
    d.text((120, 170), "[Design Mockup]", fill=GRAY)
    d.text((80, 320), "User: Build this page from", fill=WHITE)
    d.text((80, 340), "the attached mockup image.", fill=WHITE)
    # Right: generated code
    d.rectangle([400, 40, 800, 500], fill=(30, 30, 30))
    d.text((420, 60), "Generating code...", fill=TERMINAL_GREEN)
    code_lines = [
        ('<div class="min-h-screen">', (200, 200, 200)),
        ('  <nav class="bg-gray-900">', (200, 200, 200)),
        ('    <Logo />', BLUE),
        ('  </nav>', (200, 200, 200)),
        ('  <section class="hero">', (200, 200, 200)),
        ('    <h1>{title}</h1>', ORANGE),
        ('  </section>', (200, 200, 200)),
    ]
    for i, (line, color) in enumerate(code_lines):
        d.text((420, 100 + i * 25), line, fill=color)
    save(img, "ch8-09-claude-design-request.png")


# ============================================================
# Chapter 9: General Page Design
# ============================================================

def ch9_01():
    img, d = img_new()
    # Compact header
    d.rectangle([0, 0, 800, 50], fill=(30, 30, 40))
    d.text((20, 15), "BioTools", fill=WHITE)
    d.text((500, 15), "Home  Tools  Docs", fill=GRAY)
    # Breadcrumb
    d.text((30, 65), "Home > Tools > BLAST Search", fill=GRAY)
    d.text((30, 100), "BLAST Search", fill=DARK_GRAY)
    d.line([30, 130, 770, 130], fill=LIGHT_GRAY)
    # Input area
    rounded_rect(d, [30, 150, 770, 300], fill=LIGHT_GRAY, outline=GRAY)
    d.text((50, 170), "Enter sequence:", fill=DARK_GRAY)
    d.text((50, 200), ">query_seq", fill=GRAY)
    d.text((50, 220), "ATGCATGCATGC...", fill=GRAY)
    rounded_rect(d, [30, 320, 170, 360], fill=BLUE)
    d.text((60, 333), "Run BLAST", fill=WHITE)
    # Results table
    rounded_rect(d, [30, 380, 770, 480], fill=WHITE, outline=GRAY)
    d.text((50, 395), "Results:", fill=DARK_GRAY)
    d.text((50, 420), "Hit 1:  E-value: 1e-45  Identity: 98%", fill=GRAY)
    d.text((50, 445), "Hit 2:  E-value: 3e-30  Identity: 85%", fill=GRAY)
    save(img, "ch9-01-general-page-example.png")


def ch9_02():
    img, d = img_new(w=1000, h=400)
    # Landing page
    rounded_rect(d, [30, 30, 470, 370], fill=WHITE, outline=GRAY)
    d.text((180, 10), "Landing Page", fill=DARK_GRAY)
    d.rectangle([30, 60, 470, 100], fill=(30, 30, 40))  # navbar
    d.rectangle([30, 100, 470, 230], fill=BLUE)  # big hero
    d.text((200, 150), "Hero", fill=WHITE)
    for i in range(3):
        rounded_rect(d, [50 + i * 140, 250, 170 + i * 140, 350], fill=LIGHT_GRAY, outline=GRAY)

    # General page
    rounded_rect(d, [530, 30, 970, 370], fill=WHITE, outline=GRAY)
    d.text((680, 10), "General Page", fill=DARK_GRAY)
    d.rectangle([530, 60, 970, 85], fill=(30, 30, 40))  # compact navbar
    d.text((550, 100), "Home > Tools > BLAST", fill=GRAY)
    d.text((550, 125), "BLAST Search", fill=DARK_GRAY)
    rounded_rect(d, [550, 160, 950, 280], fill=LIGHT_GRAY, outline=GRAY)
    d.text((700, 210), "Input Area", fill=GRAY)
    rounded_rect(d, [550, 300, 950, 350], fill=LIGHT_GRAY, outline=GRAY)
    d.text((700, 318), "Results", fill=GRAY)
    save(img, "ch9-02-layout-comparison.png")


def ch9_03():
    img, d = img_new(h=180)
    d.text((30, 30), "Home  >  Tools  >  Reverse Complement", fill=BLUE)
    d.text((30, 70), "Reverse Complement Tool", fill=DARK_GRAY)
    d.text((30, 100), "Convert DNA/RNA sequences to their reverse complement", fill=GRAY)
    d.line([30, 140, 770, 140], fill=LIGHT_GRAY, width=2)
    save(img, "ch9-03-page-header-breadcrumb.png")


def ch9_04():
    img, d = img_new()
    # Sidebar
    d.rectangle([0, 0, 220, 500], fill=(245, 247, 250))
    d.line([220, 0, 220, 500], fill=LIGHT_GRAY, width=2)
    menu = ["Dashboard", "Alignment", "BLAST", "RevComp", "GC Content", "Settings"]
    for i, item in enumerate(menu):
        y = 20 + i * 45
        if i == 2:
            rounded_rect(d, [10, y - 5, 210, y + 30], fill=LIGHT_BLUE)
        d.text((25, y), item, fill=BLUE if i == 2 else DARK_GRAY)
    # Main content
    d.text((250, 30), "BLAST Search", fill=DARK_GRAY)
    d.line([250, 55, 770, 55], fill=LIGHT_GRAY)
    rounded_rect(d, [250, 80, 770, 300], fill=LIGHT_GRAY, outline=GRAY)
    d.text((270, 100), "Main Content Area", fill=GRAY)
    save(img, "ch9-04-sidebar-layout.png")


def ch9_05():
    img, d = img_new()
    d.text((30, 20), "Reverse Complement", fill=DARK_GRAY)
    d.line([30, 50, 770, 50], fill=LIGHT_GRAY)
    # Input
    d.text((30, 70), "Input Sequence:", fill=DARK_GRAY)
    rounded_rect(d, [30, 95, 770, 220], fill=WHITE, outline=GRAY)
    d.text((50, 110), ">sequence_1", fill=GRAY)
    d.text((50, 135), "ATGCGATCGATCGATCG", fill=DARK_GRAY)
    rounded_rect(d, [30, 240, 160, 275], fill=BLUE)
    d.text((50, 250), "Run Analysis", fill=WHITE)
    # Results
    d.text((30, 310), "Results:", fill=DARK_GRAY)
    rounded_rect(d, [30, 335, 770, 470], fill=LIGHT_GRAY, outline=GRAY)
    d.text((50, 345), "gene_id     input              output", fill=DARK_GRAY)
    d.line([30, 370, 770, 370], fill=GRAY)
    d.text((50, 380), "seq_1       ATGCGATCGATCG      CGATCGATCGCAT", fill=GRAY)
    save(img, "ch9-05-single-tool-page.png")


def ch9_06():
    img, d = img_new()
    # Sidebar
    d.rectangle([0, 0, 220, 500], fill=(245, 247, 250))
    d.line([220, 0, 220, 500], fill=LIGHT_GRAY, width=2)
    d.text((20, 20), "Tools", fill=DARK_GRAY)
    tools = ["Alignment", "BLAST", "RevComp", "GC Content", "ORF Finder"]
    for i, tool in enumerate(tools):
        y = 60 + i * 40
        if i == 0:
            rounded_rect(d, [10, y - 5, 210, y + 28], fill=LIGHT_BLUE)
        d.text((25, y), tool, fill=BLUE if i == 0 else GRAY)
    # Main area
    d.text((250, 30), "Sequence Alignment", fill=DARK_GRAY)
    rounded_rect(d, [250, 70, 770, 200], fill=WHITE, outline=GRAY)
    d.text((270, 90), "Input sequences...", fill=GRAY)
    rounded_rect(d, [250, 220, 380, 255], fill=BLUE)
    d.text((270, 230), "Run Alignment", fill=WHITE)
    rounded_rect(d, [250, 280, 770, 480], fill=WHITE, outline=GRAY)
    d.text((270, 300), "Alignment Results:", fill=DARK_GRAY)
    d.text((270, 330), "seq1: ATGC--ATGC", fill=GREEN)
    d.text((270, 350), "seq2: ATGCGGATGC", fill=GREEN)
    save(img, "ch9-06-multi-tool-sidebar.png")


def ch9_07():
    img, d = img_new(h=400)
    # Tabs
    tabs = ["Text", "Table", "Visualization"]
    for i, tab in enumerate(tabs):
        x = 50 + i * 150
        if i == 0:
            rounded_rect(d, [x, 30, x + 130, 65], fill=WHITE, outline=BLUE)
            d.text((x + 30, 40), tab, fill=BLUE)
        else:
            rounded_rect(d, [x, 30, x + 130, 65], fill=LIGHT_GRAY, outline=GRAY)
            d.text((x + 20, 40), tab, fill=GRAY)
    # Content
    rounded_rect(d, [50, 65, 750, 370], fill=WHITE, outline=GRAY)
    d.text((70, 90), "Analysis Result:", fill=DARK_GRAY)
    d.text((70, 120), "Input:  ATGCGATCGATCG (13 bp)", fill=GRAY)
    d.text((70, 150), "Output: CGATCGATCGCAT", fill=DARK_GRAY)
    d.text((70, 190), "GC Content: 53.8%", fill=DARK_GRAY)
    d.text((70, 220), "Molecular Weight: 4012.6 Da", fill=DARK_GRAY)
    save(img, "ch9-07-tabbed-results.png")


def ch9_08():
    img, d = img_new()
    d.rectangle([0, 0, 800, 40], fill=(36, 36, 36))
    d.text((20, 12), "Claude Code", fill=ORANGE)
    d.rectangle([0, 40, 800, 500], fill=(25, 25, 30))
    # Chat
    rounded_rect(d, [20, 60, 780, 140], fill=(40, 50, 70))
    d.text((40, 70), "Create a Reverse Complement tool page at", fill=WHITE)
    d.text((40, 90), "/tools/revcomp with FASTA input, result table,", fill=WHITE)
    d.text((40, 110), "and copy-to-clipboard. Use Tailwind CSS.", fill=WHITE)
    # Response
    rounded_rect(d, [20, 160, 780, 480], fill=(35, 40, 45))
    d.text((40, 170), "Creating src/routes/tools/revcomp/+page.svelte", fill=TERMINAL_GREEN)
    code = [
        '<script lang="ts">',
        '  let sequence = "";',
        '  let result = "";',
        '',
        '  function reverseComplement(seq: string) {',
        '    const comp: Record<string, string> = {',
        "      A:'T', T:'A', G:'C', C:'G'",
        '    };',
        '    return [...seq].reverse()',
        "      .map(c => comp[c] ?? c).join('');",
        '  }',
        '</script>',
    ]
    for i, line in enumerate(code):
        d.text((40, 200 + i * 20), line, fill=(200, 200, 200))
    save(img, "ch9-08-claude-general-request.png")


# ============================================================
# Execute all
# ============================================================

if __name__ == "__main__":
    print("Chapter 1:")
    ch1_01(); ch1_02(); ch1_03(); ch1_04(); ch1_05()
    ch1_06(); ch1_07(); ch1_08(); ch1_09(); ch1_10(); ch1_11()

    print("Chapter 2:")
    ch2_01(); ch2_02(); ch2_03(); ch2_04(); ch2_05(); ch2_06()
    ch2_07(); ch2_08(); ch2_09(); ch2_10(); ch2_11(); ch2_12()
    ch2_13(); ch2_14(); ch2_15(); ch2_16(); ch2_17()
    ch2_18(); ch2_19(); ch2_20(); ch2_21()

    print("Chapter 3:")
    ch3_01(); ch3_02(); ch3_03(); ch3_04()

    print("Chapter 4:")
    ch4_01(); ch4_02(); ch4_03(); ch4_04(); ch4_05()

    print("Chapter 5:")
    ch5_01(); ch5_02(); ch5_03(); ch5_04(); ch5_05()

    print("Chapter 6:")
    ch6_01(); ch6_02()

    print("Chapter 7:")
    ch7_01(); ch7_02(); ch7_03(); ch7_04()

    print("Chapter 8:")
    ch8_01(); ch8_02(); ch8_03(); ch8_04(); ch8_05()
    ch8_06(); ch8_07(); ch8_08(); ch8_09()

    print("Chapter 9:")
    ch9_01(); ch9_02(); ch9_03(); ch9_04(); ch9_05()
    ch9_06(); ch9_07(); ch9_08()

    print("\nDone! All images saved to assets/")

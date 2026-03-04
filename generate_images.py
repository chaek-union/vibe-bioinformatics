from PIL import Image, ImageDraw, ImageFont
import random
import os

def create_image(filename, width=800, height=500, bg=(255, 255, 255)):
    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)
    return img, draw

def save_image(img, filename):
    img.save(f"assets/{filename}")
    print(f"Saved {filename}")

def draw_header(draw, title, width=800):
    draw.rectangle([0, 0, width, 40], fill=(50, 50, 50))
    draw.text((10, 10), title, fill=(255, 255, 255))

# --- Chapter 4: Python Data Analysis ---

def ch4_01_pandas():
    img, draw = create_image("ch4-01-pandas-dataframe.png")
    draw_header(draw, "Jupyter Notebook - pandas DataFrame")
    # Draw table
    cols = ["gene_id", "gene_name", "logFC", "pvalue"]
    data = [
        ["ENSG001", "GAPDH", "1.2", "0.001"],
        ["ENSG002", "ACTB", "-0.5", "0.120"],
        ["ENSG003", "TP53", "2.4", "0.0001"],
        ["ENSG004", "MT-CO1", "0.8", "0.034"],
        ["ENSG005", "IL6", "-1.8", "0.005"]
    ]
    x, y = 50, 80
    cw, rh = 150, 30
    for i, col in enumerate(cols):
        draw.rectangle([x+i*cw, y, x+(i+1)*cw, y+rh], fill=(240, 240, 240), outline=(200, 200, 200))
        draw.text((x+i*cw+10, y+8), col, fill=(0, 0, 0))
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            draw.rectangle([x+c*cw, y+(r+1)*rh, x+(c+1)*cw, y+(r+2)*rh], outline=(220, 220, 220))
            draw.text((x+c*cw+10, y+(r+1)*rh+8), val, fill=(0, 0, 0))
    save_image(img, "ch4-01-pandas-dataframe.png")

def ch4_02_volcano():
    img, draw = create_image("ch4-02-matplotlib-volcano.png")
    draw_header(draw, "Matplotlib: Volcano Plot")
    # Draw axes
    draw.line([100, 400, 700, 400], fill=(0, 0, 0), width=2) # X
    draw.line([100, 400, 100, 100], fill=(0, 0, 0), width=2) # Y
    draw.text((350, 420), "log2 Fold Change", fill=(0, 0, 0))
    draw.text((40, 200), "-log10(p-value)", fill=(0, 0, 0))
    # Draw points
    for _ in range(200):
        px = random.randint(150, 650)
        py = random.randint(120, 380)
        fc = (px - 400) / 100
        p_val = (400 - py) / 50
        color = (200, 200, 200)
        if abs(fc) > 1 and p_val > 1.3:
            color = (255, 100, 100)
        draw.ellipse([px-2, py-2, px+2, py+2], fill=color)
    save_image(img, "ch4-02-matplotlib-volcano.png")

def ch4_03_subplot():
    img, draw = create_image("ch4-03-matplotlib-subplot.png", width=1000, height=400)
    # Left: Histogram
    draw.rectangle([50, 50, 450, 350], outline=(0, 0, 0))
    draw.text((200, 20), "Distribution of logFC", fill=(0,0,0))
    for i in range(10):
        h = random.randint(50, 250)
        draw.rectangle([70+i*35, 350-h, 100+i*35, 350], fill=(100, 100, 255))
    # Right: Volcano (simplified)
    draw.rectangle([550, 50, 950, 350], outline=(0, 0, 0))
    draw.text((700, 20), "Volcano Plot", fill=(0,0,0))
    for _ in range(100):
        draw.ellipse([random.randint(580, 920), random.randint(80, 320), random.randint(580, 920)+4, random.randint(80, 320)+4], fill=(150, 150, 150))
    save_image(img, "ch4-03-matplotlib-subplot.png")

def ch4_04_boxplot():
    img, draw = create_image("ch4-04-seaborn-boxplot.png")
    draw_header(draw, "Seaborn: Box Plot - Gene Expression by Cell Type")
    types = ["T cell", "B cell", "NK cell", "Monocyte"]
    colors = [(200, 200, 255), (200, 255, 200), (255, 200, 200), (255, 255, 200)]
    for i, t in enumerate(types):
        x = 150 + i * 150
        y_med = 250 + random.randint(-50, 50)
        draw.rectangle([x-40, y_med-60, x+40, y_med+60], fill=colors[i], outline=(0, 0, 0))
        draw.line([x-40, y_med, x+40, y_med], fill=(0, 0, 0), width=2) # median
        draw.line([x, y_med-60, x, y_med-90], fill=(0, 0, 0)) # whisker
        draw.line([x, y_med+60, x, y_med+90], fill=(0, 0, 0))
        draw.text((x-20, 420), t, fill=(0,0,0))
    save_image(img, "ch4-04-seaborn-boxplot.png")

def ch4_05_heatmap():
    img, draw = create_image("ch4-05-seaborn-heatmap.png")
    draw_header(draw, "Seaborn: Gene Expression Heatmap")
    for r in range(10):
        for c in range(15):
            val = random.random()
            color = (int(255*val), 100, int(255*(1-val)))
            draw.rectangle([100+c*40, 80+r*30, 140+c*40, 110+r*30], fill=color, outline=(255, 255, 255))
    save_image(img, "ch4-05-seaborn-heatmap.png")

# --- Chapter 5: Scanpy/AnnData ---

def ch5_01_anndata():
    img, draw = create_image("ch5-01-anndata-structure.png")
    draw.text((350, 20), "AnnData Structure", fill=(0,0,0))
    # Main Matrix X
    draw.rectangle([300, 150, 500, 350], fill=(220, 220, 255), outline=(0, 0, 0))
    draw.text((380, 240), "X", fill=(0, 0, 0))
    draw.text((340, 360), "cells x genes", fill=(0, 0, 0))
    # obs
    draw.rectangle([200, 150, 280, 350], fill=(255, 220, 220), outline=(0, 0, 0))
    draw.text((220, 240), "obs", fill=(0,0,0))
    # var
    draw.rectangle([300, 70, 500, 130], fill=(220, 255, 220), outline=(0, 0, 0))
    draw.text((380, 90), "var", fill=(0,0,0))
    # obsm
    draw.rectangle([520, 150, 600, 250], fill=(255, 255, 220), outline=(0, 0, 0))
    draw.text((540, 190), "obsm", fill=(0,0,0))
    # uns
    draw.rectangle([520, 270, 600, 350], fill=(240, 240, 240), outline=(0, 0, 0))
    draw.text((540, 300), "uns", fill=(0,0,0))
    save_image(img, "ch5-01-anndata-structure.png")

def ch5_02_mudata():
    img, draw = create_image("ch5-02-mudata-structure.png")
    draw.text((350, 20), "MuData Object", fill=(0,0,0))
    draw.rectangle([100, 100, 700, 400], outline=(0, 0, 0), width=2)
    draw.text((120, 120), "MuData", fill=(0,0,0))
    # RNA AnnData
    draw.rectangle([150, 180, 380, 350], fill=(230, 240, 255), outline=(0, 0, 0))
    draw.text((240, 250), "rna (AnnData)", fill=(0,0,0))
    # ATAC AnnData
    draw.rectangle([420, 180, 650, 350], fill=(230, 255, 240), outline=(0, 0, 0))
    draw.text((510, 250), "atac (AnnData)", fill=(0,0,0))
    save_image(img, "ch5-02-mudata-structure.png")

def ch5_03_qc():
    img, draw = create_image("ch5-03-qc-violin-plots.png", width=900, height=400)
    titles = ["n_genes_by_counts", "total_counts", "pct_counts_mt"]
    for i in range(3):
        x = 100 + i * 280
        draw.rectangle([x, 100, x+200, 350], outline=(200, 200, 200))
        draw.text((x+40, 360), titles[i], fill=(0,0,0))
        # Violin shape
        pts = []
        for j in range(20):
            w = 10 + random.randint(0, 40)
            y = 120 + j * 10
            pts.append((x+100-w, y))
        for j in range(19, -1, -1):
            w = 10 + random.randint(0, 40)
            y = 120 + j * 10
            pts.append((x+100+w, y))
        draw.polygon(pts, fill=(180, 180, 255), outline=(0, 0, 0))
    save_image(img, "ch5-03-qc-violin-plots.png")

def ch5_04_umap():
    img, draw = create_image("ch5-04-umap-clusters.png")
    draw_header(draw, "Scanpy: UMAP Clusters (Leiden)")
    colors = [(255, 100, 100), (100, 255, 100), (100, 100, 255), (255, 255, 100), (255, 100, 255)]
    for c in range(5):
        cx, cy = 200 + random.randint(0, 400), 100 + random.randint(0, 250)
        for _ in range(100):
            px = cx + random.normalvariate(0, 30)
            py = cy + random.normalvariate(0, 30)
            draw.point((px, py), fill=colors[c])
    save_image(img, "ch5-04-umap-clusters.png")

def ch5_05_umap_markers():
    img, draw = create_image("ch5-05-umap-marker-genes.png", width=800, height=600)
    genes = ["CD3E", "CD14", "MS4A1", "NKG7"]
    for i in range(4):
        x, y = (i % 2) * 400, (i // 2) * 300
        draw.rectangle([x+10, y+10, x+390, y+290], outline=(220, 220, 220))
        draw.text((x+180, y+20), genes[i], fill=(0,0,0))
        # Points with expression
        for _ in range(200):
            px, py = x + 200 + random.normalvariate(0, 60), y + 150 + random.normalvariate(0, 60)
            val = random.random()
            color = (int(255*(1-val)), int(255*(1-val)), 255) if val > 0.5 else (240, 240, 240)
            draw.point((px, py), fill=color)
    save_image(img, "ch5-05-umap-marker-genes.png")

# --- Chapter 6: Snakemake ---

def ch6_01_dag():
    img, draw = create_image("ch6-01-snakemake-dag.png")
    draw.text((350, 20), "Snakemake DAG", fill=(0,0,0))
    rules = ["fastqc", "trim", "align", "count"]
    for i, r in enumerate(rules):
        draw.rectangle([350, 70+i*100, 450, 120+i*100], outline=(0, 0, 0), fill=(240, 240, 240))
        draw.text((370, 85+i*100), r, fill=(0,0,0))
        if i < len(rules) - 1:
            draw.line([400, 120+i*100, 400, 170+i*100], fill=(0, 0, 0), width=2)
            draw.polygon([(395, 160+i*100), (405, 160+i*100), (400, 170+i*100)], fill=(0,0,0))
    save_image(img, "ch6-01-snakemake-dag.png")

def ch6_02_dryrun():
    img, draw = create_image("ch6-02-snakemake-dryrun.png", bg=(30, 30, 30))
    text = "$ snakemake -n\nJob counts:\n    count     3\n    align     3\n    trim      3\n    fastqc    3\n    all       1\n    total     13\n\n[dry-run]\nrule fastqc:\n    input: data/sample_A.fastq.gz\n    output: results/fastqc/sample_A_fastqc.html\n...\nThis was a dry-run (flag -n). The orders of jobs were correctly computed."
    draw.text((20, 20), text, fill=(0, 255, 0))
    save_image(img, "ch6-02-snakemake-dryrun.png")

# --- Chapter 7: Tech Stack ---

def ch7_01_sveltekit():
    img, draw = create_image("ch7-01-sveltekit-website.png")
    draw.rectangle([0, 0, 800, 500], fill=(255, 62, 0)) # Svelte Red
    draw.text((300, 200), "SvelteKit", fill=(255, 255, 255))
    draw.text((280, 260), "The fastest way to build apps", fill=(255, 255, 255))
    save_image(img, "ch7-01-sveltekit-website.png")

def ch7_02_tailwind():
    img, draw = create_image("ch7-02-tailwindcss-website.png")
    draw.rectangle([0, 0, 800, 500], fill=(56, 189, 248)) # Tailwind Blue
    draw.text((300, 200), "Tailwind CSS", fill=(255, 255, 255))
    draw.text((250, 260), "Rapidly build modern websites without ever leaving your HTML.", fill=(255, 255, 255))
    save_image(img, "ch7-02-tailwindcss-website.png")

def ch7_03_nodejs():
    img, draw = create_image("ch7-03-nodejs-nvm-pnpm.png")
    draw_header(draw, "Node.js Download Page")
    draw.text((100, 100), "Download for Linux (x64)", fill=(0,0,0))
    draw.rectangle([100, 150, 300, 250], fill=(200, 255, 200), outline=(0, 0, 0))
    draw.text((150, 190), "LTS (v20.x)", fill=(0,0,0))
    draw.text((100, 300), "Select components:", fill=(0,0,0))
    draw.text((120, 330), "[X] nvm (Node Version Manager)", fill=(0,0,0))
    draw.text((120, 360), "[X] pnpm (Package Manager)", fill=(0,0,0))
    save_image(img, "ch7-03-nodejs-nvm-pnpm.png")

def ch7_04_devserver():
    img, draw = create_image("ch7-04-sveltekit-dev-server.png")
    draw_header(draw, "http://localhost:5173 - SvelteKit")
    draw.text((300, 200), "Welcome to SvelteKit", fill=(0,0,0))
    draw.text((280, 230), "Visit svelte.dev to learn more", fill=(100, 100, 255))
    save_image(img, "ch7-04-sveltekit-dev-server.png")

# --- Chapter 8: Landing Page ---

def ch8_01_landing():
    img, draw = create_image("ch8-01-landing-page-example.png")
    draw.rectangle([0, 0, 800, 80], fill=(240, 240, 240)) # Header
    draw.text((20, 30), "BIO-LAB", fill=(0,0,0))
    draw.rectangle([0, 80, 800, 300], fill=(50, 100, 200)) # Hero
    draw.text((100, 130), "Next-Gen Bioinformatics", fill=(255, 255, 255))
    draw.rectangle([100, 220, 250, 260], fill=(255, 255, 255))
    draw.text((140, 235), "Get Started", fill=(0, 0, 0))
    # Features
    for i in range(3):
        draw.rectangle([50+i*250, 320, 250+i*250, 450], outline=(200, 200, 200))
        draw.text((100+i*250, 340), f"Feature {i+1}", fill=(0,0,0))
    save_image(img, "ch8-01-landing-page-example.png")

def ch8_02_structure():
    img, draw = create_image("ch8-02-web-page-structure.png")
    draw.rectangle([100, 50, 700, 100], fill=(200, 200, 200), outline=(0, 0, 0))
    draw.text((380, 70), "Header", fill=(0,0,0))
    draw.rectangle([100, 110, 700, 350], fill=(240, 240, 240), outline=(0, 0, 0))
    draw.text((380, 220), "Body", fill=(0,0,0))
    draw.rectangle([100, 360, 700, 450], fill=(150, 150, 150), outline=(0, 0, 0))
    draw.text((380, 400), "Footer", fill=(0,0,0))
    save_image(img, "ch8-02-web-page-structure.png")

def ch8_03_navbars():
    img, draw = create_image("ch8-03-navbar-examples.png")
    # Style 1
    draw.rectangle([50, 50, 750, 100], fill=(240, 240, 240), outline=(0, 0, 0))
    draw.text((70, 70), "Logo   Home  Tools  About", fill=(0,0,0))
    draw.rectangle([650, 60, 730, 90], fill=(0, 0, 0))
    draw.text((670, 70), "Login", fill=(255, 255, 255))
    # Style 2
    draw.rectangle([50, 150, 750, 200], fill=(0, 0, 0), outline=(0, 0, 0))
    draw.text((350, 170), "Home   Services   Contact", fill=(255, 255, 255))
    save_image(img, "ch8-03-navbar-examples.png")

def ch8_04_hero():
    img, draw = create_image("ch8-04-hero-section-example.png")
    draw.rectangle([0, 0, 800, 500], fill=(20, 20, 40))
    draw.text((100, 100), "Analyze Your DNA Sequences", fill=(255, 255, 255))
    draw.text((100, 150), "Powerful, Fast, and Open Source tools for bio-researchers.", fill=(200, 200, 200))
    draw.rectangle([100, 250, 300, 300], fill=(0, 200, 100))
    draw.text((150, 270), "Start Analysis", fill=(255, 255, 255))
    # DNA abstract
    for i in range(10):
        draw.ellipse([500+i*10, 100+i*30, 520+i*10, 120+i*30], fill=(100, 100, 255))
        draw.ellipse([600-i*10, 100+i*30, 620-i*10, 120+i*30], fill=(255, 100, 100))
    save_image(img, "ch8-04-hero-section-example.png")

def ch8_05_carousel():
    img, draw = create_image("ch8-05-carousel-example.png")
    draw.rectangle([100, 100, 700, 400], fill=(230, 230, 230), outline=(0, 0, 0))
    draw.text((350, 240), "Slide 1: Sequence Alignment", fill=(0,0,0))
    draw.polygon([(110, 250), (140, 230), (140, 270)], fill=(100, 100, 100))
    draw.polygon([(690, 250), (660, 230), (660, 270)], fill=(100, 100, 100))
    draw.ellipse([380, 380, 390, 390], fill=(0,0,0))
    draw.ellipse([400, 380, 410, 390], fill=(200,200,200))
    save_image(img, "ch8-05-carousel-example.png")

def ch8_06_features():
    img, draw = create_image("ch8-06-features-section.png")
    for i in range(3):
        x = 50 + i * 250
        draw.rectangle([x, 100, x+220, 350], fill=(250, 250, 250), outline=(200, 200, 200))
        draw.ellipse([x+85, 120, x+135, 170], fill=(200, 220, 255)) # icon placeholder
        draw.text((x+60, 190), f"Powerful Tool {i+1}", fill=(0,0,0))
        draw.text((x+20, 230), "Detailed description of the\nfeature goes here.", fill=(100, 100, 100))
    save_image(img, "ch8-06-features-section.png")

def ch8_07_gemini():
    img, draw = create_image("ch8-07-gemini-mockups.png", width=900, height=400)
    # Mockup 1
    draw.rectangle([50, 50, 400, 350], outline=(0, 0, 0))
    draw.text((180, 20), "Variation A", fill=(0,0,0))
    draw.rectangle([50, 50, 400, 150], fill=(50, 50, 150))
    # Mockup 2
    draw.rectangle([500, 50, 850, 350], outline=(0, 0, 0))
    draw.text((630, 20), "Variation B", fill=(0,0,0))
    draw.rectangle([500, 50, 850, 100], fill=(200, 200, 200))
    save_image(img, "ch8-07-gemini-mockups.png")

def ch8_08_detailed():
    img, draw = create_image("ch8-08-detailed-mockup.png")
    draw_header(draw, "Detailed Mockup - Bio-App")
    draw.rectangle([0, 40, 800, 100], fill=(255, 255, 255)) # Navbar
    draw.text((20, 60), "Logo   Home  Tools  About", fill=(0,0,0))
    draw.rectangle([0, 100, 800, 300], fill=(100, 150, 255)) # Hero
    draw.text((100, 150), "Bioinformatics for Everyone", fill=(255, 255, 255))
    draw.rectangle([50, 350, 250, 450], outline=(0, 0, 0)) # Feature
    draw.text((70, 370), "RevComp", fill=(0,0,0))
    save_image(img, "ch8-08-detailed-mockup.png")

def ch8_09_claude():
    img, draw = create_image("ch8-09-claude-design-request.png", bg=(245, 245, 245))
    draw.rectangle([100, 50, 700, 450], fill=(255, 255, 255), outline=(200, 200, 200))
    draw.text((120, 70), "Claude Code", fill=(0,0,0))
    draw.rectangle([120, 100, 680, 250], fill=(230, 230, 230))
    draw.text((140, 120), "User: Build this design [Image Attached]", fill=(0,0,0))
    draw.text((140, 280), "Claude: Analyzing image...\nGenerating SvelteKit + Tailwind code...", fill=(100, 100, 255))
    save_image(img, "ch8-09-claude-design-request.png")

# --- Chapter 9: General Page ---

def ch9_01_general():
    img, draw = create_image("ch9-01-general-page-example.png")
    draw_header(draw, "Tool: BLAST Search")
    draw.text((50, 60), "Home > Tools > BLAST", fill=(150, 150, 150))
    draw.text((50, 100), "BLAST Search", fill=(0,0,0))
    draw.rectangle([50, 150, 750, 300], outline=(200, 200, 200)) # Input
    draw.text((70, 170), "Enter sequence...", fill=(200, 200, 200))
    draw.rectangle([50, 320, 200, 360], fill=(0, 100, 255))
    draw.text((80, 335), "Run BLAST", fill=(255, 255, 255))
    save_image(img, "ch9-01-general-page-example.png")

def ch9_02_comparison():
    img, draw = create_image("ch9-02-layout-comparison.png", width=1000, height=400)
    # Landing
    draw.rectangle([50, 50, 450, 350], outline=(0, 0, 0))
    draw.text((150, 20), "Landing Page (Large Hero)", fill=(0,0,0))
    draw.rectangle([50, 50, 450, 150], fill=(100, 100, 255))
    # General
    draw.rectangle([550, 50, 950, 350], outline=(0, 0, 0))
    draw.text((650, 20), "General Page (Small Header)", fill=(0,0,0))
    draw.rectangle([550, 50, 950, 80], fill=(200, 200, 200))
    save_image(img, "ch9-02-layout-comparison.png")

def ch9_03_breadcrumb():
    img, draw = create_image("ch9-03-page-header-breadcrumb.png", height=200)
    draw.text((50, 50), "Home > Tools > Reverse Complement", fill=(100, 100, 100))
    draw.text((50, 90), "Reverse Complement Tool", fill=(0,0,0))
    draw.line([50, 140, 750, 140], fill=(220, 220, 220))
    save_image(img, "ch9-03-page-header-breadcrumb.png")

def ch9_04_sidebar():
    img, draw = create_image("ch9-04-sidebar-layout.png")
    draw_header(draw, "Dashboard")
    draw.rectangle([0, 40, 200, 500], fill=(240, 240, 240)) # Sidebar
    draw.text((20, 70), "Menu 1\n\nMenu 2\n\nMenu 3", fill=(0,0,0))
    draw.text((250, 70), "Main Content Area", fill=(150, 150, 150))
    save_image(img, "ch9-04-sidebar-layout.png")

def ch9_05_single():
    img, draw = create_image("ch9-05-single-tool-page.png")
    draw_header(draw, "Single Tool Layout")
    draw.rectangle([100, 80, 700, 250], outline=(0, 0, 0)) # Textarea
    draw.text((120, 100), ">sequence1\nATGCATGC...", fill=(0,0,0))
    draw.rectangle([100, 270, 250, 310], fill=(0, 100, 255))
    draw.text((130, 285), "Start Analysis", fill=(255, 255, 255))
    draw.rectangle([100, 340, 700, 450], fill=(245, 245, 245)) # Results
    draw.text((120, 360), "Results table will appear here...", fill=(100, 100, 100))
    save_image(img, "ch9-05-single-tool-page.png")

def ch9_06_multi():
    img, draw = create_image("ch9-06-multi-tool-sidebar.png")
    draw_header(draw, "Tools Hub")
    draw.rectangle([0, 40, 200, 500], fill=(230, 230, 255))
    draw.text((20, 70), "> Alignment\n\n  Blast\n\n  HMMER", fill=(0,0,0))
    draw.text((250, 70), "Alignment Tool Interface", fill=(0,0,0))
    save_image(img, "ch9-06-multi-tool-sidebar.png")

def ch9_07_tabbed():
    img, draw = create_image("ch9-07-tabbed-results.png")
    draw.rectangle([100, 100, 250, 140], fill=(255, 255, 255), outline=(0, 0, 0))
    draw.text((140, 115), "Text", fill=(0,0,0))
    draw.rectangle([250, 100, 400, 140], fill=(220, 220, 220), outline=(0, 0, 0))
    draw.text((280, 115), "Table", fill=(0,0,0))
    draw.rectangle([400, 100, 550, 140], fill=(220, 220, 220), outline=(0, 0, 0))
    draw.text((430, 115), "Plot", fill=(0,0,0))
    draw.rectangle([100, 140, 700, 400], outline=(0, 0, 0))
    draw.text((150, 180), "Result text view content...", fill=(0,0,0))
    save_image(img, "ch9-07-tabbed-results.png")

def ch9_08_claude():
    img, draw = create_image("ch9-08-claude-general-request.png", bg=(245, 245, 245))
    draw.text((100, 50), "Claude Code: Implementing Tool Page", fill=(0,0,0))
    draw.rectangle([100, 100, 700, 400], fill=(255, 255, 255), outline=(200, 200, 200))
    draw.text((120, 130), "Generating src/routes/tools/revcomp/+page.svelte...", fill=(0,0,0))
    draw.text((120, 170), "<script>\n  let sequence = '';\n  // ...\n</script>\n\n<div class='bg-white shadow p-6'>\n  <textarea class='w-full border' ...", fill=(0, 150, 0))
    save_image(img, "ch9-08-claude-general-request.png")

# Execute all
# ch4_01_pandas()
# ch4_02_volcano()
# ch4_03_subplot()
# ch4_04_boxplot()
# ch4_05_heatmap()
ch5_01_anndata()
ch5_02_mudata()
ch5_03_qc()
ch5_04_umap()
ch5_05_umap_markers()
ch6_01_dag()
ch6_02_dryrun()
ch7_01_sveltekit()
ch7_02_tailwind()
ch7_03_nodejs()
ch7_04_devserver()
ch8_01_landing()
ch8_02_structure()
ch8_03_navbars()
ch8_04_hero()
ch8_05_carousel()
ch8_06_features()
ch8_07_gemini()
ch8_08_detailed()
ch8_09_claude()
ch9_01_general()
ch9_02_comparison()
ch9_03_breadcrumb()
ch9_04_sidebar()
ch9_05_single()
ch9_06_multi()
ch9_07_tabbed()
ch9_08_claude()

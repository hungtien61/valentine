import os
import random

def get_images(folder):
    valid_exts = ['.jpg', '.jpeg', '.png', '.gif', '.heic', '.mp4']
    try:
        files = [f for f in os.listdir(folder) if any(f.endswith(ext) for ext in valid_exts)]
        return sorted(files)
    except FileNotFoundError:
        return []

# 1. The Muse (u folder)
u_images = get_images('u')
muse_html = ""
# We need to reverse them for the stack effect if we want the first one on top?
# The current HTML has Card 1 (Top) at the bottom of the DOM (z-50)
# So we iterate list, and the last item in iteration should be the top one?
# No, existing HTML:
# Card 5 (z-10) -> FIRST in DOM
# Card 1 (z-50) -> LAST in DOM
# So we iterate and increase Z-index.
for i, img in enumerate(u_images):
    z_index = (i + 1) * 10
    rotate = random.choice([-3, -2, -1, 0, 1, 2, 3])
    muse_html += f"""
                            <div class="absolute inset-0 bg-white p-2 shadow-2xl transform rotate-[{rotate}deg] transition-all duration-300 card" style="z-index: {z_index};">
                                <img src="u/{img}" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-500" alt="Muse {i+1}">
                            </div>"""

# 2. Our Journey (we folder)
we_images = get_images('we')
journey_html = ""
for i, img in enumerate(we_images):
    journey_html += f"""
                            <div class="snap-center shrink-0 w-[300px] md:w-[500px] h-[200px] md:h-[350px] bg-black border-y-8 border-dashed border-gray-800 relative overflow-hidden group">
                                <img src="we/{img}" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-500" alt="Journey {i+1}">
                                <div class="absolute bottom-2 right-2 text-xs font-mono text-white/50">SCENE {i+1:02d}</div>
                            </div>"""

# 3. Unfiltered (funny folder)
funny_images = get_images('funny')
funny_html = ""
for i, img in enumerate(funny_images):
    funny_html += f"""
                            <div class="relative group cursor-pointer overflow-hidden rounded-lg break-inside-avoid">
                                <div class="absolute inset-0 z-20 flex items-center justify-center bg-black/40 group-hover:opacity-0 transition-opacity duration-300">
                                    <span class="text-4xl">🚫</span>
                                </div>
                                <img src="funny/{img}" class="w-full object-cover rounded-lg filter blur-[15px] group-hover:blur-0 transition-all duration-500 ease-out" alt="Funny {i+1}">
                            </div>"""

# Write to file
with open('generated_snippets.txt', 'w', encoding='utf-8') as f:
    f.write("--- MUSE START ---\n")
    f.write(muse_html + "\n")
    f.write("--- MUSE END ---\n")
    f.write("--- JOURNEY START ---\n")
    f.write(journey_html + "\n")
    f.write("--- JOURNEY END ---\n")
    f.write("--- FUNNY START ---\n")
    f.write(funny_html + "\n")
    f.write("--- FUNNY END ---\n")

print("Snippets generated.")

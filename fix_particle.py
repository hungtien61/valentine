
import os

file_path = r'd:\tech\valentine\main project\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = 'class Particle {'
end_marker = 'function initParticles() {'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    print(f"Start: {start_idx}, End: {end_idx}")
    exit(1)

# Construct the new content
new_particle_class = """class Particle {
                constructor() {
                    this.x = Math.random() * introCanvas.width;
                    this.y = Math.random() * introCanvas.height;
                    this.vx = (Math.random() - 0.5) * 0.5;
                    this.vy = (Math.random() - 0.5) * 0.5;
                    this.size = Math.random() * 2 + 1;
                    this.color = `rgba(255, 255, 255, ${Math.random() * 0.5 + 0.2})`;
                }

                update() {
                    if (warpSpeedActive) {
                        // WARP SPEED: Move fast outwards from center
                        const cx = introCanvas.width / 2;
                        const cy = introCanvas.height / 2;
                        const angle = Math.atan2(this.y - cy, this.x - cx);
                        this.vx = Math.cos(angle) * 15;
                        this.vy = Math.sin(angle) * 15;
                        this.size += 0.1; // Grow as they fly past
                    } else {
                        // Normal Movement
                        // Mouse Interaction (Repel/Attract)
                        const dx = this.x - introMouseX;
                        const dy = this.y - introMouseY;
                        const distance = Math.sqrt(dx * dx + dy * dy);
                        const maxDist = 150;
                        
                        if (distance < maxDist) {
                            const forceDirectionX = dx / distance;
                            const forceDirectionY = dy / distance;
                            const force = (maxDist - distance) / maxDist;
                            // Gentle push away
                            this.vx += forceDirectionX * force * 0.05;
                            this.vy += forceDirectionY * force * 0.05;
                        }
                    }

                    this.x += this.vx;
                    this.y += this.vy;

                    // Bounce off edges (only if not warping)
                    if (!warpSpeedActive) {
                        if (this.x < 0 || this.x > introCanvas.width) this.vx *= -1;
                        if (this.y < 0 || this.y > introCanvas.height) this.vy *= -1;
                    }
                }

                draw() {
                    ctxIntro.fillStyle = this.color;
                    ctxIntro.beginPath();
                    ctxIntro.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctxIntro.fill();
                }
            }

            """

# Replace the content
new_content = content[:start_idx] + new_particle_class + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully replaced Particle class.")

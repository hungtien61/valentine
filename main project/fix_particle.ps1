
$path = "d:\tech\valentine\main project\index.html"
$lines = Get-Content $path

# Part 1: Lines 1 to 1509 (Index 0 to 1508)
$part1 = $lines[0..1508]

# Part 3: Lines 1572 to End (Index 1571 to End)
$part3 = $lines[1571..($lines.Count - 1)]

$fixedCode = @"
            class Particle {
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
"@

$newContent = $part1 + $fixedCode + $part3
$newContent | Set-Content $path -Encoding UTF8

Write-Host "Successfully patched index.html"

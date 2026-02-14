export function renderText(ctx, x, y, size, content, centered_x = 0, centered_y = 0, color = [255, 255, 255]) {
    ctx.save();
    ctx.font = `${size}px PixelFont`;
    ctx.fillStyle = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
    ctx.textBaseline = 'top';

    const metrics = ctx.measureText(content);
    const textWidth = metrics.width;
    // Approximate height from font size (bitmap fonts don't give reliable metrics)
    const textHeight = size;

    let dx = x;
    let dy = y;

    if (centered_x === 1) {
        dx = x - textWidth / 2;
    }
    if (centered_y === 1) {
        dy = y - textHeight / 2;
    }

    ctx.fillText(content, dx, dy);
    ctx.restore();
}

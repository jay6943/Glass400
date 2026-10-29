import cfg
import dat
import dxf
import dev
import tip


def device(x, y):
  y1 = y + cfg.s1x2
  y2 = y - cfg.s1x2
  
  x2, _ = dxf.taper('core', x, y, cfg.ltpr, cfg.wg, cfg.wtpr)
  x3, _ = dxf.srect('core', x2, y, cfg.l1x2, cfg.w1x2)
  x5, _ = dxf.taper('core', x3, y1, cfg.ltpr, cfg.wtpr, cfg.wg)
  x5, _ = dxf.taper('core', x3, y2, cfg.ltpr, cfg.wtpr, cfg.wg)

  return x5, y1, y2


def chip(x, y, lchip):
  angle, dy = 20, cfg.ch * 0.5 - cfg.s1x2
  core = dev.euler(cfg.wg, cfg.radius, angle)

  idev = len(dat.points)
  x1, y1, y2 = device(x, y)
  x2, y1 = dxf.sbend('core', core, x1, y1, dy)
  x2, y2 = dxf.sbend('core', core, x1, y2, -dy)
  x5, x6 = dxf.center(idev, x, x2, lchip)

  title = f'1x2-{cfg.l1x2:.1f}'
  tip.texts(x5, y, x, title)
  tip.texts(x6, y + cfg.ch * 0.5, x + lchip, title)
  tip.sline(x6, y - cfg.ch * 0.5, x + cfg.lchip)
  print(f'{title}; {x6 - x5:.0f}')

  return x + lchip, y


def chips(x, y):
  y += cfg.ch
  l1x2 = cfg.l1x2
  for cfg.l1x2 in dxf.arange(17, 20, 0.5):
    _, y = chip(x, y, cfg.lchip)
    y += cfg.ch * 2
  cfg.l1x2 = l1x2

  return x + cfg.lchip, y


if __name__ == '__main__':
  chips(0, 0)
  dev.saveas('1x2')
